import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime, timedelta
from urllib.parse import quote_plus

# ===============================================
# 数据库连接配置 (请替换为您的实际信息)
# ===============================================
DB_USER = "readonly"
DB_PASS = quote_plus("xxxxxxx")
DB_HOST = "xxxxxxxx"
DB_PORT = "30096"
DB_NAME = "db_ro3_operation_log"
# 使用 PyMySQL 驱动
DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# ===============================================
# 分析参数配置
# ===============================================
ITEM_ID = 24600065
START_DATE_STR = "2025-09-25"
END_DATE_STR = "2025-10-15"
OUTPUT_FILENAME = "item_log_analysis_20250925_to_20251015.xlsx"

def date_range(start_date, end_date):
    """生成指定日期范围内的所有日期（包含起始和结束日期）"""
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def generate_analysis_query(table_name, item_id):
    """
    生成针对特定表和道具ID的分析SQL语句。
    
    这里的核心逻辑是计算 (num - left) 或 (left - num) 来获得实际的变动量 (change_amount)，
    然后利用条件聚合 (CASE WHEN) 来区分增加和减少的统计。
    """
    
    sql_template = f"""
    SELECT
        T.sid,
        -- 统计增加人数 (change_type = 2)
        COUNT(DISTINCT CASE WHEN T.change_type = 2 THEN T.uid END) AS '增加的总人数',
        -- 统计增加道具总数 (变化量为正)
        SUM(CASE WHEN T.change_type = 2 THEN T.change_amount ELSE 0 END) AS '增加的道具总数',
        
        -- 统计减少人数 (change_type = 1)
        COUNT(DISTINCT CASE WHEN T.change_type = 1 THEN T.uid END) AS '减少的总人数',
        -- 统计减少道具总数 (变化量为正)
        SUM(CASE WHEN T.change_type = 1 THEN T.change_amount ELSE 0 END) AS '减少的道具总数'
    FROM
        (
            SELECT
                sid,
                uid,
                change_type,
                -- 计算实际的变化量
                CASE
                    WHEN change_type = 2 THEN (`num`) -- 增加量
                    WHEN change_type = 1 THEN (`num`) -- 减少量
                    ELSE 0
                END AS change_amount
            FROM
                `{table_name}`
            WHERE
                itemid = {item_id}
                -- 筛选 sid 以 4 开头的服务器 (假设为 40000 到 49999 范围)
                AND sid BETWEEN 40000 AND 49999 
                AND change_type IN (1, 2)
        ) AS T
    GROUP BY
        T.sid
    ORDER BY
        T.sid;
    """
    return sql_template

def process_logs():
    """主函数：连接数据库，迭代日期，执行查询，并将结果写入Excel"""
    
    print("尝试连接数据库...")
    engine = create_engine(DATABASE_URL)
    
    start_date = datetime.strptime(START_DATE_STR, "%Y-%m-%d").date()
    end_date = datetime.strptime(END_DATE_STR, "%Y-%m-%d").date()
    
    
    all_dataframes = {}
    
    # 1. 遍历日期范围并执行查询
    for single_date in date_range(start_date, end_date):
        date_str = single_date.strftime("%Y-%m-%d")
        table_name = f"item_log_{date_str}"
        sheet_name = date_str # 用作 Excel Sheet 名称
        
        sql_query = generate_analysis_query(table_name, ITEM_ID)
        
        print(f"--- 正在处理表: {table_name} ---")
        
        try:
            # 使用 Pandas 读取 SQL 查询结果到 DataFrame
            df = pd.read_sql_query(text(sql_query), engine)
            
            if df.empty:
                print(f"警告: 表 {table_name} 存在但没有匹配的筛选数据。")
            else:
                all_dataframes[sheet_name] = df
                print(f"成功获取 {len(df)} 条记录。")

        except Exception as e:
            # 捕获表不存在或其他数据库错误
            if "Table" in str(e) and "doesn't exist" in str(e):
                 print(f"跳过: 表 {table_name} 不存在。")
            else:
                 print(f"处理 {table_name} 时发生错误: {e}")
            continue

    # 2. 将所有 DataFrame 写入多页 Excel 文件
    if not all_dataframes:
        print("未获取到任何数据，文件未生成。")
        return

    print(f"\n--- 正在写入 Excel 文件: {OUTPUT_FILENAME} ---")
    
    # 使用 ExcelWriter 写入多张 Sheet
    with pd.ExcelWriter(OUTPUT_FILENAME, engine='openpyxl') as writer:
        for sheet_name, df in all_dataframes.items():
            # 写入时避免索引列
            df.to_excel(writer, sheet_name=sheet_name, index=False)
            print(f"已写入 Sheet: {sheet_name}")

    print("\n任务完成！")

if __name__ == "__main__":
    process_logs()