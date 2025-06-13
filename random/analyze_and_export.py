import pandas as pd

# 输入文件路径
level_file_path = 'level-0612.csv'
users_file_path = '12.csv'
# 输出文件路径
output_file_path = 'level_statistics_report.csv'

try:
    # --- 步骤 1: 读取两个CSV文件 ---
    df_level = pd.read_csv(level_file_path)
    df_users = pd.read_csv(users_file_path)

    # 清理列名中可能存在的前后空格
    df_level.columns = df_level.columns.str.strip()
    df_users.columns = df_users.columns.str.strip()

    # --- 步骤 2: 找出在两个表中都存在的用户 ---
    valid_uids = df_users['uid'].unique()
    filtered_df_level = df_level[df_level['uid'].isin(valid_uids)].copy()

    # --- 步骤 3: 确定每个玩家的最终等级 ---
    # 按 'uid' 分组，并找出每个 'uid' 对应的最大 'after_lv'
    player_final_levels = filtered_df_level.groupby('uid')['after_lv'].max().reset_index()

    # --- 步骤 4: 统计总人数和各等级的人数 ---
    total_players = len(player_final_levels)

    if total_players == 0:
        print("错误：在两个文件中没有找到任何共同的玩家(uid)。")
    else:
        # 统计各等级人数
        level_counts = player_final_levels['after_lv'].value_counts().reset_index()
        level_counts.columns = ['等级(after_lv)', '人数']

        # --- 步骤 5: 计算百分比 ---
        level_counts['占总人数百分比'] = (level_counts['人数'] / total_players * 100).map('{:.2f}%'.format)

        # --- 步骤 6: 排序和在控制台输出结果 ---
        final_report = level_counts.sort_values(by='等级(after_lv)').reset_index(drop=True)

        print(f"统计前提：表1 (level.csv) 中的 uid 必须在 表2 (12x.csv) 中存在。\n")
        print(f"符合条件的总人数: {total_players}\n")
        print("各等级人数分布统计结果 (控制台预览):")
        print(final_report.to_string(index=False))

        # --- 步骤 7: 将结果导出到CSV文件 ---
        # 使用 to_csv 方法保存 DataFrame
        # index=False 表示不将 DataFrame 的索引（0, 1, 2...）写入文件
        # encoding='utf-8-sig' 可以确保中文在Excel中正常显示，避免乱码
        final_report.to_csv(output_file_path, index=False, encoding='utf-8-sig')

        print(f"\n[成功] 统计结果已保存到文件: '{output_file_path}'")


except FileNotFoundError as e:
    print(f"[文件未找到错误]: {e}")
    print(f"请确保 '{level_file_path}' 和 '{users_file_path}' 文件与此Python脚本在同一个目录下。")
except KeyError as e:
    print(f"[列名错误]: {e}。请检查CSV文件中的列名是否正确（例如 'uid', 'after_lv'）。")
except Exception as e:
    print(f"[发生未知错误]: {e}")