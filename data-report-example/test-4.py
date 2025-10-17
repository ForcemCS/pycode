from sqlalchemy import create_engine, text
from datetime import date, timedelta
import pandas as pd
from urllib.parse import quote_plus

# === 数据库连接配置 ===
DB_USER = "readonly"
DB_PASS = quote_plus("xxxxx")
DB_HOST = "xxxxxxxxxx"
DB_PORT = "30096"
DB_NAME = "db_ro3_operation_log"
# 使用 PyMySQL 驱动
DB_URI = f"mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DB_URI)

# === 查询条件 ===
itemid = 24600067
change_type = 2
uids = [1019707440028,1066754140107]

start_date = date(2025, 8, 21)
end_date = date(2025, 10, 14)

# === 生成表名列表 ===
table_names = []
current = start_date
while current <= end_date:
    table_names.append(f"item_log_{current.strftime('%Y-%m-%d')}")
    current += timedelta(days=1)

# === 拼接 UNION ALL SQL ===
union_sql_parts = []
for table in table_names:
    sql = f"""
    SELECT *, RIGHT(uid, 5) AS uid_last5
    FROM `{table}`
    WHERE itemid = :itemid
      AND change_type = :change_type
      AND uid IN :uids
    """
    union_sql_parts.append(sql)

union_all_sql = "\nUNION ALL\n".join(union_sql_parts)

# === 最终 SQL ===
final_sql = f"""
SELECT *
FROM (
    {union_all_sql}
) AS all_logs
ORDER BY CAST(uid_last5 AS UNSIGNED);
"""

# === 执行查询并导出为 CSV ===
with engine.connect() as conn:
    df = pd.read_sql(text(final_sql), conn, params={"itemid": itemid, "change_type": change_type, "uids": tuple(uids)})

# === 导出为 CSV 文件 ===
output_path = "item_log_2025-10-01_to_2025-10-17.csv"
df.to_csv(output_path, index=False, encoding="utf-8-sig")

print(f"✅ 查询完成！结果已导出到: {output_path}")
print(f"共 {len(df)} 条记录")