import requests
import time
import json
import logging

ssl_verify = False  # 注意: 使用 False 会跳过 SSL 验证，仅用于开发调试
consul_token = "4994e44d-5c1e-f260-3cd0-4ee3033e1e4e"
consul_addr = "https://10.10.0.203:31670"
url = f"{consul_addr}/v1/catalog/services"

headers = {
    "X-Consul-Token": consul_token
}

SERVICE_PREFIX = "game-" 


# 配置日志记录
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def report_unhealthy_service(instance):
    
    instance_id = instance.get('Service', {}).get('ID', 'N/A')
    service_name = instance.get('Service', {}).get('Service', 'N/A')
    #node = instance.get('Node', {}).get('Node', 'N/A')
    address = instance.get('Service', {}).get('Address', 'N/A')
    sid = instance.get('Service', {}).get('Meta', 'N/A').get('sid', 'N/A')
    #port = instance.get('Service', {}).get('Port', 'N/A')
    
    # 获取详细的健康检查信息
    check_notes = []
    for check in instance.get('Checks', []):
        if check['Status'] != 'passing':
            check_info = f"  - Check '{check['CheckID']}': {check['Status'].upper()} (Output: {check.get('Output', '健康状态存在问题')})"
            check_notes.append(check_info)
    
    notes_str = "\n".join(check_notes)
    
    logging.error(
        f"🚨 UNHEALTHY INSTANCE DETECTED!\n"
        f"  Service: {service_name}\n"
        f"  Instance ID: {instance_id}\n"
        f"  SID: {sid}\n"
        f"  Address: {address}\n"
        f"  Failing Checks:\n{notes_str}"
    )

def watch_unhealthy_services():
    
    # 它的结构是 { 'service_name': {'instance_id_1', 'instance_id_2'} }
    last_known_unhealthy = {}
    
    service_indexes = {} # 为每个服务维护一个独立的 index
    
    WAIT_TIME = "5m" # 阻塞请求最大持续时间的,默认为3分钟，可以显式设置
    
    logging.info(f"Starting to monitor unhealthy services with prefix '{SERVICE_PREFIX}' on {consul_addr}")
    
    while True:
        
        try:
            response = requests.get(url, headers=headers, verify=ssl_verify, timeout=10)
            response.raise_for_status()
            all_services = response.json()
            
            # 1.获取game-xxx services的列表
            game_services = [name for name in all_services if name.startswith(SERVICE_PREFIX)]

            if not game_services:
                logging.info("No services with prefix '%s' found. Waiting...", SERVICE_PREFIX)
                last_known_unhealthy.clear() # 清空状态，以防服务回来
                time.sleep(30)
                continue
            
            current_unhealthy = {}
            
        
            # 2. 逐一查询我们关心的服务的健康状态
            for service_name in game_services:
                last_index = service_indexes.get(service_name, '0') # 默认为 '0' 开始
                
                params = {"wait": WAIT_TIME, "index": last_index}
                health_url = f"{consul_addr}/v1/health/service/{service_name}"
                
                health_response = requests.get(health_url, headers=headers, verify=ssl_verify, params=params, timeout=310) # 超时要比 wait 时间稍长
                health_response.raise_for_status()
                
                

                # --- 应用官方文档的健壮性规则 ---
                new_index_str = health_response.headers.get('X-Consul-Index', '0')
                new_index = int(new_index_str)
                
                # 规则 1: Index 回退检查
                if new_index < int(last_index):
                    logging.warning(f"Consul index for '{service_name}' went backwards ({last_index} -> {new_index}). Resetting index.")
                    service_indexes[service_name] = '0' # 重置
                else:
                    # 规则 2: Index > 0 检查
                    # 如果拿到的 index <= 0，下次查询用 1，否则用拿到的新 index
                    service_indexes[service_name] = str(max(1, new_index))

                unhealthy_instances = [
                    instance for instance in health_response.json()
                    if any(check['Status'] != 'passing' for check in instance.get('Checks', []))
                ]
                 
                if unhealthy_instances:
                    current_unhealthy[service_name] = {inst.get('Service', {}).get('ID') for inst in unhealthy_instances}
                    
                    # 检查是否有新出现的不健康实例
                    last_set = last_known_unhealthy.get(service_name, set())
                    newly_unhealthy = current_unhealthy[service_name] - last_set
                    
                    if newly_unhealthy:
                        # 只对新出现的不健康实例进行告警
                        for instance in unhealthy_instances:
                            if instance.get('Service', {}).get('ID') in newly_unhealthy:
                                report_unhealthy_service(instance)
                        
                 
            ## 3.对全部的服务告警之后，再次对所有的services检查,是否有服务恢复了健康
            ##  last_known_unhealthy 第一次循环还是一个空字典 {}
            for service_name, last_unhealthy_ids in last_known_unhealthy.items():
                current_unhealthy_ids = current_unhealthy.get(service_name, set())
                recovered_ids = last_unhealthy_ids - current_unhealthy_ids
                if recovered_ids:
                    logging.info(f"✅ SERVICE RECOVERED: Service '{service_name}' instances {recovered_ids} are now healthy.")
                    
            # 4. 更新状态，为下一次循环做准备
            last_known_unhealthy = current_unhealthy
            
            # 清理已经消失的服务，防止内存泄漏
            for gone_service in list(service_indexes.keys()):
                if gone_service not in game_services:
                    del service_indexes[gone_service]
                    if gone_service in last_known_unhealthy:
                        del last_known_unhealthy[gone_service]           
        except requests.exceptions.RequestException as e:
            logging.error(f"[请求失败]: {e}. Retrying in 10 seconds.")
            time.sleep(10)

        except Exception as e:
            logging.error(f"[发生未知错误]: {e}. Retrying in 10 seconds.")
            time.sleep(10)

if __name__ == "__main__":
    watch_unhealthy_services()


