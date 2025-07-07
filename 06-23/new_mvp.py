import pandas as pd
import re

def parse_mvp_rewards(reward_str: str) -> set:
    """
    解析 Show_Reward_MVP 字符串，提取除第一个ID外的所有道具ID。
    例如: "{20000001,1,1002640,1,1001849,1}" -> {'1002640', '1001849'}
    """
    if not isinstance(reward_str, str) or reward_str == "{,,,,,,,,,,,,,,}":
        return set()
    
    # 使用正则表达式提取所有数字
    ids_and_counts = re.findall(r'\d+', reward_str)
    
    # 道具ID位于偶数位 (0, 2, 4, ...)
    item_ids = [ids_and_counts[i] for i in range(0, len(ids_and_counts), 2)]
    
    # 根据规则，排除第一个道具ID
    if len(item_ids) > 1:
        return set(item_ids[1:])
    else:
        return set()

def parse_dropped_items(items_str: str) -> set:
    """
    解析 gsitems 字符串，提取所有掉落的道具ID。
    例如: "1002640,2,1001849,1" -> {'1002640', '1001849'}
    """
    if not isinstance(items_str, str) or not items_str:
        return set()
    
    parts = items_str.split(',')
    # 道具ID位于偶数位 (0, 2, 4, ...)
    item_ids = {parts[i] for i in range(0, len(parts), 2)}
    return item_ids

def analyze_mvp_drops(log_file: str, config_file: str) -> pd.DataFrame:
    """
    分析MVP Boss击杀日志，统计总次数和MVP掉落次数。
    """
    try:
        # 1. 读取配置文件并构建 stage_id -> mvp_items 的映射
        df_config = pd.read_csv(config_file)
        stage_to_mvp_map = df_config.set_index('ID')['Show_Reward_MVP'].apply(parse_mvp_rewards).to_dict()
        
        # 2. 读取日志文件
        df_log = pd.read_csv(log_file)
        
        # 3. 数据预处理
        # ==================== 主要修正点 ====================
        # 明确指定日期的格式为 "日/月/年 时:分:秒"
        # 这样 pandas 才能正确解析您的数据
        df_log['date'] = pd.to_datetime(df_log['time_stamp'], format="%d/%m/%Y %H:%M:%S", errors='coerce').dt.date
        # ===================================================
        
        # 删除日期转换失败或关键列为空的行
        df_log.dropna(subset=['sid', 'date', 'stage_id', 'gsitems'], inplace=True)
        
        # 4. 判断每次击杀是否掉落了MVP道具
        results = []
        for index, row in df_log.iterrows():
            stage_id = int(row['stage_id'])
            sid = int(row['sid'])
            date = row['date']
            
            valid_mvp_ids = stage_to_mvp_map.get(stage_id, set())
            dropped_ids = parse_dropped_items(row['gsitems'])
            is_mvp_drop = 1 if not valid_mvp_ids.isdisjoint(dropped_ids) else 0
            
            results.append({
                'sid': sid,
                'date': date,
                'is_mvp_drop': is_mvp_drop
            })

        if not results:
            print("没有可分析的数据，请检查日志文件内容和日期格式。")
            return pd.DataFrame()
            
        # 5. 聚合统计
        df_results = pd.DataFrame(results)
        grouped = df_results.groupby(['sid', 'date'])
        summary = grouped.agg(
            总次数=('sid', 'size'),
            高端装备=('is_mvp_drop', 'sum')
        ).reset_index()
        
        # 格式化date列为 'YYYY-MM-DD' 字符串
        summary['date'] = summary['date'].apply(lambda x: x.strftime('%Y-%m-%d'))
        
        summary = summary.sort_values(by=['sid', 'date']).reset_index(drop=True)
        
        return summary

    except FileNotFoundError as e:
        print(f"错误: 文件未找到 -> {e}")
        return pd.DataFrame()
    except Exception as e:
        print(f"处理过程中发生错误: {e}")
        return pd.DataFrame()

# --- 主程序 ---
if __name__ == "__main__":
    log_filename = 'mvpboss.csv'
    config_filename = 'MVP_Boss_Stage.csv'
    
    final_summary = analyze_mvp_drops(log_filename, config_filename)
    
    if not final_summary.empty:
        print("MVP Boss击杀与掉落统计结果:")
        print(final_summary.to_string(index=False))
        
        output_filename = 'mvp_kill_summary.csv'
        final_summary.to_csv(output_filename, index=False, encoding='utf-8-sig')
        print(f"\n结果已保存到文件: {output_filename}")