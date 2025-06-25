# 1. mean(s) → 算术平均值
#     作用: 计算一个可迭代对象（如列表）中所有数值的算术平均值 (Sum / Count)。
#     示例:
#     data = [1, 2, 3, 4, 10]
#     # 计算 (1 + 2 + 3 + 4 + 10) / 5
#     print(statistics.mean(data))
#     # 输出: 4

#     # 也可以处理浮点数
#     data_float = [2.5, 3.75, 1.25, 6.0]
#     print(statistics.mean(data_float))
#     # 输出: 3.375
# 2. fmean(s) → 快速浮点数平均值
#     作用: 与 mean() 类似，但它首先将所有数据点转换为浮点数 (float)，然后再计算平均值。这使得它在处理纯数字时通常比 mean() 更快。
#     与 mean() 的区别: mean() 在计算前会尝试保留数据的原始类型（如 Fraction 或 Decimal），因此更通用但稍慢。fmean() 则直接“一刀切”转为 float，追求速度。
#     示例:
#     data = [1, 2, 3, 4, 10]
#     print(statistics.fmean(data))
#     # 输出: 4.0 (注意结果是浮点数)
# 3. median(s) → 中位数
#     作用: 计算数据的中位数。中位数是将数据排序后位于最中间位置的那个值。
#     要点:
#     如果数据点数量是 奇数，中位数就是排序后正中间的那个数。
#     如果数据点数量是 偶数，中位数是中间两个数的平均值。因此，中位数本身可能不属于原始数据集（"may not be an element of the iterable"）。
#     示例:
#     # 奇数个数据
#     data_odd = [1, 5, 2, 8, 7] # 排序后: [1, 2, 5, 7, 8]
#     print(statistics.median(data_odd))
#     # 输出: 5 (中间的数)

#     # 偶数个数据
#     data_even = [1, 6, 2, 8] # 排序后: [1, 2, 6, 8]
#     # 中间两个数是 2 和 6，(2 + 6) / 2 = 4
#     print(statistics.median(data_even))
#     # 输出: 4.0 (这个 4.0 并不在原始数据中)
# 4. median_low(s) & median_high(s) → 低/高位中位数
#     作用: 这两个函数解决了当数据量为偶数时 median() 返回一个“新”值的问题。它们确保返回的中位数始终是原始数据集中的一个成员。
#     median_low(s): 当数据量为偶数时，返回中间两个数中较小的那个。
#     median_high(s): 当数据量为偶数时，返回中间两个数中较大的那个。
#     示例: 我们使用上面 median() 的偶数示例 [1, 6, 2, 8]，排序后是 [1, 2, 6, 8]。
#     data_even = [1, 6, 2, 8]

#     # 普通中位数
#     print(f"Median: {statistics.median(data_even)}") # 输出: Median: 4.0

#     # 低位中位数 (中间两个数 2 和 6 中，返回较小的 2)
#     print(f"Median Low: {statistics.median_low(data_even)}") # 输出: Median Low: 2

#     # 高位中位数 (中间两个数 2 和 6 中，返回较大的 6)
#     print(f"Median High: {statistics.median_high(data_even)}"


# 想法
# 展开即可显示模型的想法摘要
# 好的，我们来详细解释一下您图片中展示的 Python statistics 模块中关于 集中趋势度量 (Measures of Central Location) 的函数。

# 这些函数用于描述一个数据集的“中心”或“典型”值。要使用它们，你首先需要导入 statistics 模块：

# import statistics
# 介绍与总览
# → statistics module:
# 解释: 这些函数都属于 Python 的 statistics 标准库模块。
# → s is a non-empty sequence or iterable:
# 解释: 图片中所有函数都接受一个名为 s 的参数。这个 s 必须是一个非空的数据序列（例如列表、元组）。如果传入一个空序列，会引发 StatisticsError。
# 函数详解与示例
# 1. mean(s) → 算术平均值
# 作用: 计算一个可迭代对象（如列表）中所有数值的算术平均值 (Sum / Count)。
# 示例:
# data = [1, 2, 3, 4, 10]
# # 计算 (1 + 2 + 3 + 4 + 10) / 5
# print(statistics.mean(data))
# # 输出: 4

# # 也可以处理浮点数
# data_float = [2.5, 3.75, 1.25, 6.0]
# print(statistics.mean(data_float))
# # 输出: 3.375
# 2. fmean(s) → 快速浮点数平均值
# 作用: 与 mean() 类似，但它首先将所有数据点转换为浮点数 (float)，然后再计算平均值。这使得它在处理纯数字时通常比 mean() 更快。
# 与 mean() 的区别: mean() 在计算前会尝试保留数据的原始类型（如 Fraction 或 Decimal），因此更通用但稍慢。fmean() 则直接“一刀切”转为 float，追求速度。
# 示例:
# data = [1, 2, 3, 4, 10]
# print(statistics.fmean(data))
# # 输出: 4.0 (注意结果是浮点数)
# 3. median(s) → 中位数
# 作用: 计算数据的中位数。中位数是将数据排序后位于最中间位置的那个值。
# 要点:
# 如果数据点数量是 奇数，中位数就是排序后正中间的那个数。
# 如果数据点数量是 偶数，中位数是中间两个数的平均值。因此，中位数本身可能不属于原始数据集（"may not be an element of the iterable"）。
# 示例:
# # 奇数个数据
# data_odd = [1, 5, 2, 8, 7] # 排序后: [1, 2, 5, 7, 8]
# print(statistics.median(data_odd))
# # 输出: 5 (中间的数)

# # 偶数个数据
# data_even = [1, 6, 2, 8] # 排序后: [1, 2, 6, 8]
# # 中间两个数是 2 和 6，(2 + 6) / 2 = 4
# print(statistics.median(data_even))
# # 输出: 4.0 (这个 4.0 并不在原始数据中)
# 4. median_low(s) & median_high(s) → 低/高位中位数
# 作用: 这两个函数解决了当数据量为偶数时 median() 返回一个“新”值的问题。它们确保返回的中位数始终是原始数据集中的一个成员。
# median_low(s): 当数据量为偶数时，返回中间两个数中较小的那个。
# median_high(s): 当数据量为偶数时，返回中间两个数中较大的那个。
# 示例: 我们使用上面 median() 的偶数示例 [1, 6, 2, 8]，排序后是 [1, 2, 6, 8]。
# data_even = [1, 6, 2, 8]

# # 普通中位数
# print(f"Median: {statistics.median(data_even)}") # 输出: Median: 4.0

# # 低位中位数 (中间两个数 2 和 6 中，返回较小的 2)
# print(f"Median Low: {statistics.median_low(data_even)}") # 输出: Median Low: 2

# # 高位中位数 (中间两个数 2 和 6 中，返回较大的 6)
# print(f"Median High: {statistics.median_high(data_even)}") # 输出: Median High: 6
# 5. mode(s) → 众数
#     作用: 计算数据集中出现次数最多的值（众数）。
#     要点:
#     它不仅适用于数值型数据 (numeric)，也适用于名义型/类别型数据 (nominal)，比如字符串。
#     注意：如果数据中有多个值出现的频率相同且最高（即有多个众数），mode() 会引发 StatisticsError。如果需要处理这种情况，应该使用 multimode()。
#     示例:
#     # 数值型数据
#     numeric_data = [1, 2, 2, 3, 3, 3, 4, 4]
#     print(statistics.mode(numeric_data))
#     # 输出: 3 (因为 3 出现了 3 次，次数最多)

#     # 名义型/字符串数据
#     nominal_data = ['red', 'blue', 'red', 'green', 'blue', 'red']
#     print(statistics.mode(nominal_data))
#     # 输出: 'red' (因为 'red' 出现了 3 次，次数最多)

#     # 多个众数的情况
#     multi_mode_data = [1, 1, 2, 2, 3]
#     try:
#         statistics.mode(multi_mode_data)
#     except statistics.StatisticsError as e:
#         print(e)
#     # 输出: no unique mode; found 2 equally common values

#     # 正确处理多个众数的方法是使用 multimode()
#     print(statistics.multimode(multi_mode_data))
#     # 输出: [1, 2]