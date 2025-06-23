import pandas as pd

def parse_and_sum_items(gsitem_str):
    """
    解析gsitems字符串 (例如 '24603052,1,1001847,1')，
    并返回'神格碎片'和'诸神黄昏'的数量。
    """
    shen_ge_count = 0
    huang_hun_count = 0

    if not isinstance(gsitem_str, str) or gsitem_str.strip() == '':
        return pd.Series([0, 0], index=['神格碎片', '诸神黄昏'])

    parts = gsitem_str.split(',')
    
    for i in range(0, len(parts), 2):
        if i + 1 < len(parts):
            item_id = parts[i].strip()
            
            try:
                item_count = int(parts[i+1].strip())
            except (ValueError, IndexError):
                continue

            if item_id == '24603052':
                shen_ge_count += item_count
            else:
                huang_hun_count += item_count
    
    return pd.Series([shen_ge_count, huang_hun_count], index=['神格碎片', '诸神黄昏'])

def analyze_boss_drops_final(file_path='mvpboss.csv'):
    """
    分析mvpboss.csv文件，按天(日/月/年格式)对'神格碎片'和'诸神黄昏'的
    【总获取数量】进行求和统计。
    """
    try:
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print(f"错误：找不到文件 '{file_path}'。请确保文件名正确。")
        return

    # --- 这里是关键的修改 ---
    # 1. 提取日期，并指明日期在月份前面 (dayfirst=True)
    # 将时间戳字符串转换为datetime对象，并提取日期部分
    df['date'] = pd.to_datetime(df['time_stamp'], dayfirst=True, errors='coerce').dt.date
    
    # 删除时间戳格式不正确或为空的行
    df.dropna(subset=['date'], inplace=True)

    # 2. 解析gsitems列，生成每个类别的数量
    item_counts = df['gsitems'].apply(parse_and_sum_items)
    
    # 3. 将新生成的计数列合并回原始DataFrame
    df = pd.concat([df, item_counts], axis=1)

    # 4. 按日期分组，并对两类道具的数量进行求和
    daily_summary = df.groupby('date')[['神格碎片', '诸神黄昏']].sum()

    # 转换数据类型为整数，方便阅读
    daily_summary = daily_summary.astype(int)

    print("每日道具【总数量】统计报告：")
    print(daily_summary)

# --- 主程序入口 ---
if __name__ == '__main__':
    # 调用函数处理您的文件
    analyze_boss_drops_final('mvpboss.csv')