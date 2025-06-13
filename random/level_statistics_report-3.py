import pandas as pd
import matplotlib.pyplot as plt

# --- 文件与图表配置 ---
level_file_path = 'level-0612.csv'
users_file_path = '12.csv'
output_csv_path = 'level_statistics_report.csv'
output_chart_path = 'level_distribution_chart.png'

# --- 数据筛选条件 ---
target_registration_date = '2025-06-12'


# --- 中文显示配置 ---
try:
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.rcParams['axes.unicode_minus'] = False
except Exception as e:
    print(f"警告：设置中文字体失败 ({e})。图表中的中文可能显示为方块。")

def create_level_distribution_chart(report_df, output_path):
    """
    根据统计报告DataFrame生成并保存柱状图。
    【已修改】此函数现在只绘制40-75级的数据。
    """
    
    # --- 步骤 1: 【新增】筛选出图表所需的数据 (40-75级) ---
    chart_data = report_df[
        (report_df['等级(after_lv)'] >= 40) & 
        (report_df['等级(after_lv)'] <= 75)
    ].copy() # 使用 .copy() 避免 SettingWithCopyWarning
    
    # --- 步骤 2: 【新增】检查筛选后是否还有数据 ---
    if chart_data.empty:
        print("\n警告：在 40-75 级范围内没有找到数据，无法生成图表。")
        return # 直接退出函数
        
    print("\n正在生成图表 (40-75级)...")
    
    # --- 步骤 3: 【修改】使用筛选后的 chart_data 进行绘图 ---
    levels = chart_data['等级(after_lv)']
    counts = chart_data['人数']
    
    # 颜色逻辑保持不变，它会自动应用于筛选后的数据
    colors = ['skyblue'] * len(levels)
    for i, level in enumerate(levels):
        if 60 <= level <= 75:
            colors[i] = 'orange'
    
    plt.figure(figsize=(12, 7))
    bars = plt.bar(levels, counts, color=colors)
    
    for bar in bars:
        yval = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2.0, yval, int(yval), va='bottom', ha='center')

    # --- 步骤 4: 【修改】更新图表标题，使其更明确 ---
    plt.title(f'"{target_registration_date}" 注册玩家等级分布图 (40-75级)', fontsize=16)
    
    plt.xlabel('玩家等级 (after_lv)', fontsize=12)
    plt.ylabel('人数', fontsize=12)
    # X轴刻度现在只会显示40-75级范围内的等级，更清晰
    plt.xticks(levels) 
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    
    # 图例逻辑保持不变
    import matplotlib.patches as mpatches
    orange_patch = mpatches.Patch(color='orange', label='60-75级玩家')
    skyblue_patch = mpatches.Patch(color='skyblue', label='其他等级玩家')
    plt.legend(handles=[orange_patch, skyblue_patch])

    plt.savefig(output_path, bbox_inches='tight')
    print(f"[成功] 图表已保存到文件: '{output_path}'")


# --- 主逻辑 (无需任何修改) ---
try:
    # 步骤 1: 读取CSV文件并清理列名
    df_level = pd.read_csv(level_file_path)
    df_users = pd.read_csv(users_file_path)
    df_level.columns = df_level.columns.str.strip()
    df_users.columns = df_users.columns.str.strip()

    # 步骤 2: 应用注册日期筛选条件
    df_users['regist_time_dt'] = pd.to_datetime(df_users['regist_time'], dayfirst=True)
    target_date_obj = pd.to_datetime(target_registration_date).date()
    filtered_users = df_users[df_users['regist_time_dt'].dt.date == target_date_obj]
    
    # 步骤 3: 核心前提过滤
    valid_uids = filtered_users['uid'].unique()
    filtered_df_level = df_level[df_level['uid'].isin(valid_uids)].copy()

    # 步骤 4: 确定每个玩家的最终等级
    player_final_levels = filtered_df_level.groupby('uid')['after_lv'].max().reset_index()

    # 步骤 5: 统计总人数
    total_players = len(player_final_levels)

    if total_players == 0:
        print(f"信息：根据筛选条件，没有找到任何符合条件的玩家。")
        print(f"  - 注册日期: {target_registration_date}")
        print(f"  - 且在 level-0612.csv 中有记录")
    else:
        # 步骤 6: 计算完整的统计数据
        level_counts = player_final_levels['after_lv'].value_counts().reset_index()
        level_counts.columns = ['等级(after_lv)', '人数']
        level_counts['占总人数百分比'] = (level_counts['人数'] / total_players * 100).map('{:.2f}%'.format)
        
        # 步骤 7: 整理并输出完整报告
        final_report = level_counts.sort_values(by='等级(after_lv)').reset_index(drop=True)

        print("--- 统计前提 ---")
        print(f"1. 表1 (level.csv) 中的 uid 必须在 表2 (12x.csv) 中存在。")
        print(f"2. 表2 中的玩家注册时间 (regist_time) 必须是 {target_registration_date}。")
        print("------------------\n")
        print(f"符合所有条件的总人数: {total_players}\n")
        print("各等级人数分布统计结果 (控制台预览):")
        print(final_report.to_string(index=False))

        # 步骤 8: 导出完整的CSV报告
        final_report.to_csv(output_csv_path, index=False, encoding='utf-8-sig')
        print(f"\n[成功] 统计结果已保存到文件: '{output_csv_path}'")

        # 步骤 9: 创建并保存图表
        # 这里传入的是完整的报告，筛选逻辑封装在函数内部了
        create_level_distribution_chart(final_report, output_chart_path)

except FileNotFoundError as e:
    print(f"[文件未找到错误]: {e}")
except KeyError as e:
    print(f"[列名错误]: {e}。请检查CSV文件中的列名(如'uid', 'regist_time')是否正确且无多余空格。")
except Exception as e:
    print(f"[发生未知错误]: {e}")