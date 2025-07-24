import pandas as pd

# 场景1: 默认创建，使用 RangeIndex
s1 = pd.Series(['a', 'b', 'c', 'd'])
print("--- 场景1: 默认索引 ---")
print(s1.index)
print(f"类型: {type(s1.index)}\n")
# 输出: RangeIndex(start=0, stop=4, step=1) -> 内存高效！

# 场景2: 显式提供非连续整数，使用 Int64Index
s2 = pd.Series(['a', 'b', 'c'], index=[10, 5, 15])
print("--- 场景2: 非连续整数索引 ---")
print(s2.index)
print(f"类型: {type(s2.index)}\n")
# 输出: Int64Index([10, 5, 15], dtype='int64') -> 必须存储所有值

# 场景3: 显式提供浮点数，使用 Float64Index
s3 = pd.Series(['a', 'b', 'c'], index=[1.1, 2.2, 3.3])
print("--- 场景3: 浮点数索引 ---")
print(s3.index)
print(f"类型: {type(s3.index)}\n")
# 输出: Float64Index([1.1, 2.2, 3.3], dtype='float64')