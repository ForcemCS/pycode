import pandas as pd
import numpy as np

def analyze_recharge_data(main_recharge_file, product_info_file, start_date, end_date):
    """
    根据用户充值记录(overseas.csv)和商品信息表(Recharge.csv)，生成最终的分类汇总报告。
    此版本包含了每个玩家的总额列（所有分类相加）。

    参数:
    main_recharge_file (str): 主充值记录CSV文件 (overseas.csv)。
    product_info_file (str): 商品信息查询CSV文件 (Recharge.csv)。
    start_date (str): 统计开始日期，格式 'YYYY-MM-DD'。
    end_date (str): 统计结束日期，格式 'YYYY-MM-DD'。
    """
    # --- 步骤 1: 加载数据 ---
    try:
        print("正在加载数据...")
        main_df = pd.read_csv(main_recharge_file)
        product_df = pd.read_csv(product_info_file)
        print("数据加载成功！")
    except FileNotFoundError as e:
        print(f"错误: 文件未找到 - {e}。请确保CSV文件与脚本在同一目录下。")
        return None

    # --- 步骤 1.5: 清理并检查列名 ---
    main_df.columns = main_df.columns.str.strip()
    product_df.columns = product_df.columns.str.strip()

    required_main_cols = ['uid', 'server_id', 'product_id', 'amount', 'create_time']
    if not all(col in main_df.columns for col in required_main_cols):
        print(f"错误: 主充值表 '{main_recharge_file}' 的列名不完整。需要: {required_main_cols}")
        return None
    
    required_product_cols = ['ID', 'Name']
    if not all(col in product_df.columns for col in required_product_cols):
        print(f"错误: 商品信息表 '{product_info_file}' 的列名不完整。需要: {required_product_cols}")
        return None

    # --- 步骤 2: 基于下单时间(create_time)筛选订单 ---
    print(f"正在基于'create_time'列筛选 {start_date} 到 {end_date} 之间的订单...")
    
    time_column = 'create_time'
    correct_date_format = '%d/%m/%Y %H:%M:%S'
    
    main_df[time_column] = pd.to_datetime(main_df[time_column], format=correct_date_format, errors='coerce')
    main_df.dropna(subset=[time_column], inplace=True)

    mask = (main_df[time_column].dt.date >= pd.to_datetime(start_date).date()) & \
           (main_df[time_column].dt.date <= pd.to_datetime(end_date).date())
    filtered_main_df = main_df[mask].copy()
    
    if filtered_main_df.empty:
        print("警告: 在指定日期范围内没有找到任何订单。")
        return pd.DataFrame()
    
    print(f"筛选成功！筛选出 {len(filtered_main_df)} 条有效订单。")

    # --- 步骤 3: 关联订单与商品信息 ---
    print("正在合并订单与商品信息...")
    product_df.rename(columns={'ID': 'product_id'}, inplace=True)
    merged_df = pd.merge(filtered_main_df, product_df[['product_id', 'Name']], on='product_id', how='left')
    merged_df['Name'].fillna('未知', inplace=True)

    # --- 步骤 4: 使用 'contains' 逻辑为商品分类 ---
    print("正在为商品分类并汇总订单额度...")
    
    conditions = [
        merged_df['Name'].str.contains('首充|直充', na=False),
        merged_df['Name'].str.contains('月卡', na=False),
        merged_df['Name'].str.contains('vip', na=False, case=False),
        merged_df['Name'].str.contains('礼包', na=False)
    ]
    choices = ['直冲总额', '月卡总额', 'vip总额', '礼包总额']
    merged_df['category'] = np.select(conditions, choices, default='其他')

    # --- 步骤 5 & 6: 汇总计算、格式化并计算总额 ---
    final_summary = merged_df.pivot_table(
        index=['uid', 'server_id'], columns='category', values='amount',
        aggfunc='sum', fill_value=0
    ).reset_index()
    
    print("正在格式化最终报告...")
    
    # 定义分类列
    category_columns = ['直冲总额', '月卡总额', 'vip总额', '礼包总额']
    
    # 确保所有分类列都存在
    for col in category_columns:
        if col not in final_summary.columns:
            final_summary[col] = 0

    # 计算每个玩家的总额（所有分类的总和）
    print("正在计算每行的总额...")
    total_column_name = '总额(单位美分)'
    final_summary[total_column_name] = final_summary[category_columns].sum(axis=1)

    # 定义最终的、包含总额列的完整列顺序
    final_ordered_columns = ['uid', 'server_id'] + category_columns + [total_column_name]
    
    # 按照最终顺序排列DataFrame
    final_summary = final_summary[final_ordered_columns]

    return final_summary

# --- 主程序入口 ---
if __name__ == "__main__":
    MAIN_RECHARGE_FILE = 'overseas.csv'     # 主充值记录表
    PRODUCT_INFO_FILE = 'Recharge.csv'      # 商品信息查询表
    
    START_DATE = '2025-01-17'
    END_DATE = '2025-01-22'
    
    OUTPUT_FILE = 'recharge_summary_with_total.csv'

    summary_df = analyze_recharge_data(
        main_recharge_file=MAIN_RECHARGE_FILE,
        product_info_file=PRODUCT_INFO_FILE,
        start_date=START_DATE,
        end_date=END_DATE
    )

    if summary_df is not None:
        if not summary_df.empty:
            print("\n--- 数据分析结果预览 ---")
            print(summary_df.to_string(index=False))
            try:
                summary_df.to_csv(OUTPUT_FILE, index=False, encoding='utf-8-sig')
                print(f"\n报告已成功保存到文件: {OUTPUT_FILE}")
            except Exception as e:
                print(f"\n保存文件时出错: {e}")
        else:
             print("\n分析完成，但没有生成任何符合条件的数据。")