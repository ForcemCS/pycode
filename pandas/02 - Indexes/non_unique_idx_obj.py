import pandas as pd

# --- 1. 创建一个非唯一的索引对象是合法的 ---
non_unique_idx_obj = pd.Index([1, 1, 2, 2])
print("--- 非唯一索引对象 ---")
print(non_unique_idx_obj)
print("这是一个合法的对象，不会报错。\n")


# --- 2. 将非唯一索引与数据关联 ---
data = [10, 20, 30, 40]
idx = ['A', 'B', 'A', 'B']
s = pd.Series(data, index=idx)

print("--- 带有非唯一索引的 Series ---")
print(s)
print("\n")


# --- 3. 使用重复的标签进行索引 ---
print("--- 使用标签 'A' 进行查询 ---")
result_A = s.loc['A']
print(result_A)
print(f"\n返回值的类型是: {type(result_A)}")
# 注意！返回的是一个新的 Pandas Series，而不是一个列表或单个值。




# 转换为 Python 列表
value_list = result_A.tolist()
print(f"\n将所有'A'对应的值转为列表: result_A.tolist() -> {value_list}")
print(type(value_list))

# 获取底层的 NumPy 数组
value_array = result_A.values
print(f"\n获取所有'A'对应的值的NumPy数组: result_A.values -> {value_array}")
print(type(value_array))