import pandas as pd
from sqlalchemy import create_engine, text
from datetime import datetime, timedelta
from urllib.parse import quote_plus

# ===============================================
# 数据库连接配置 (请替换为您的实际信息)
# ===============================================
DB_USER = "readonly"
DB_PASS = quote_plus("xxxxx")
DB_HOST = "xxxx"
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
OUTPUT_FILENAME = "combined_item_log_average_analysis.csv"

def date_range(start_date, end_date):
    """生成指定日期范围内的所有日期（包含起始和结束日期）"""
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)

def generate_union_all_query(start_date_str, end_date_str, item_id):
    """
    动态生成包含 UNION ALL 的 SQL 查询。
    使用 Derived Table 结构（FROM 子句中的子查询）以兼容 MySQL 5.7。
    """
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d").date()
    end_date = datetime.strptime(end_date_str, "%Y-%m-%d").date()
    
    # 1. 构建 UNION ALL 子句
    union_clauses = []
    
    for single_date in date_range(start_date, end_date):
        date_str = single_date.strftime("%Y-%m-%d")
        table_name = f"item_log_{date_str}"
        
        # 子查询：计算每条记录的实际变动量，并只选择需要的列
        sub_query = f"""
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
                AND sid BETWEEN 40000 AND 49999
                AND change_type IN (1, 2)
        )
        """
        union_clauses.append(sub_query)

    # 2. 将所有子查询用 UNION ALL 连接起来
    combined_data_union = "\nUNION ALL\n".join(union_clauses)
    
    # 3. 最终聚合查询 (使用 Derived Table 结构)
    final_sql = f"""
    SELECT
        T.sid,
        -- 统计增加人数 (去重)
        COUNT(DISTINCT CASE WHEN T.change_type = 2 THEN T.uid END) AS '增加的总人数',
        -- 统计增加道具总数
        SUM(CASE WHEN T.change_type = 2 THEN T.change_amount ELSE 0 END) AS '增加的道具总数',
        -- 计算增加平均数 (总数 / 总人数)
        (
            SUM(CASE WHEN T.change_type = 2 THEN T.change_amount ELSE 0 END) / 
            NULLIF(COUNT(DISTINCT CASE WHEN T.change_type = 2 THEN T.uid END), 0)
        ) AS '增加平均数',
        
        -- 统计减少人数 (去重)
        COUNT(DISTINCT CASE WHEN T.change_type = 1 THEN T.uid END) AS '减少的总人数',
        -- 统计减少道具总数
        SUM(CASE WHEN T.change_type = 1 THEN T.change_amount ELSE 0 END) AS '减少的道具总数',
        -- 计算减少平均数 (总数 / 总人数)
        (
            SUM(CASE WHEN T.change_type = 1 THEN T.change_amount ELSE 0 END) / 
            NULLIF(COUNT(DISTINCT CASE WHEN T.change_type = 1 THEN T.uid END), 0)
        ) AS '减少平均数'
    FROM
        (
            {combined_data_union}
        ) AS T  /* 这是 MySQL 5.7 兼容的 Derived Table */
    GROUP BY
        T.sid
    ORDER BY
        T.sid;
    """
    return final_sql

def process_combined_logs():
    """主函数：连接数据库，生成合并查询，执行并输出 CSV。"""
    
    print("尝试连接数据库...")
    try:
        engine = create_engine(DATABASE_URL)
    except Exception as e:
        print(f"数据库连接失败: {e}")
        return

    # 生成包含 UNION ALL 的 SQL
    sql_query = generate_union_all_query(START_DATE_STR, END_DATE_STR, ITEM_ID)
    
    print(f"--- 正在执行 {START_DATE_STR} 至 {END_DATE_STR} 的合并查询 ---")
    
    try:
        # 使用 Pandas 读取 SQL 查询结果到 DataFrame
        # 注意：对于大型 UNION ALL 查询，数据库可能会运行较长时间
        df = pd.read_sql_query(text(sql_query), engine)
        
        if df.empty:
            print("未获取到任何数据。")
        else:
            # 输出到 CSV 文件
            df.to_csv(OUTPUT_FILENAME, index=False, encoding='utf-8')
            print(f"成功获取 {len(df)} 条服务器统计数据。")
            print(f"结果已保存到文件: {OUTPUT_FILENAME}")
            
    except Exception as e:
        print(f"执行查询或保存文件时发生错误: {e}")

if __name__ == "__main__":
    process_combined_logs()