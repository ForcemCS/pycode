import pandas as pd
import numpy as np

data = ['a', 'b', 'c', 'd']
# 但这次我们为它创建一个“显式索引”
idx = ['first', 'second', 'third', 'fourth']

# 创建一个 Pandas Series，把数据和索引绑定起来
s = pd.Series(data, index=idx)
print("Pandas Series s:")
print(s)
# first     a
# second    b
# third     c
# fourth    d
# dtype: object


# 现在，我们有两种方式访问数据：

# (A) 使用我们自己定义的“显式索引”（按标签 Label 访问）
# 这是 Pandas 最推荐的方式，使用 .loc 访问器
print("使用显式索引 (loc):")
print(f"s.loc['second'] -> {s.loc['second']}")  # 访问标签为 'second' 的元素
print(f"s.loc['third']  -> {s.loc['third']}")

# (B) 仍然可以使用像列表一样的“隐式索引”（按位置 Position 访问）
# 为了清晰，Pandas 推荐使用 .iloc 访问器 (integer location)
print("\n使用隐式索引 (iloc):")
print(f"s.iloc[1] -> {s.iloc[1]}") # 访问位置为 1 的元素 (第二个元素)
print(f"s.iloc[2] -> {s.iloc[2]}") # 访问位置为 2 的元素 (第三个元素)


print(f"s.loc['first'] -> {s.loc['first']}")


print("\n" + "="*40 + "\n")
print("--- Pandas Index Object ---")

# 创建一个和幻灯片里一样的 Index 对象
idx_obj = pd.Index([10, 20, 30, 40])
print(f"创建的 Index 对象: {idx_obj}")           # Index([10, 20, 30, 40], dtype='int64')
print(f"它的类型是: {type(idx_obj)}")
print("\n")


# 这个 Index 对象本身也拥有“隐式位置索引” (0, 1, 2, 3)
# 我们可以像操作列表一样操作它

# (A) 使用单个位置索引
val = idx_obj[0]
print(f"idx_obj[0]           -> {val} (类型: {type(val)})")              #idx_obj[0]           -> 10 (类型: <class 'numpy.int64'>)
# 注意：当只取一个元素时，返回的是该元素本身（比如一个整数）

# (B) 使用切片
slice_result = idx_obj[1:3] # 注意，Python切片不包含末尾元素
print(f"idx_obj[1:3]         -> {slice_result} (类型: {type(slice_result)})")              #idx_obj[1:3]         -> Index([20, 30], dtype='int64') (类型: <class 'pandas.core.indexes.base.Index'>)
# 注意：切片后返回的仍然是一个 Index 对象！


# (C) 使用位置列表（花式索引）
fancy_result = idx_obj[[0, 3]] # 获取位置 0 和位置 3 的元素
print(f"idx_obj[[0, 3]]      -> {fancy_result} (类型: {type(fancy_result)})")               #idx_obj[[0, 3]]      -> Index([10, 40], dtype='int64') (类型: <class 'pandas.core.indexes.base.Index'>)

# (D) 使用布尔索引（非常强大）
# 步骤1: 创建一个布尔条件的列表/Series

# (D) 使用布尔索引（非常强大）
# 步骤1: 创建一个布尔条件的列表/Series
a = idx_obj % 20 == 0  # [10%20==0, 20%20==0, 30%20==0, 40%20==0] -> [False, True, False, True]
print(a)
print(type(a))

bool_result = idx_obj[a]
print(f"idx_obj[a] -> {bool_result} (类型: {type(bool_result)})")