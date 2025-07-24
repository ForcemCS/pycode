### Indexes Have Set-Like Properties (索引拥有类似集合的属性)

Pandas 的索引对象可以像 Python 的集合（Set）一样进行数学运算，比如求交集、并集等。 这在数据对齐和合并时非常有用。

- `&` (intersection - **交集**): 找出两个索引中共有的元素。
- `|` (union - 并集): 找出两个索引中所有的元素（重复的只保留一个）。
- `in` (element of - 成员测试): 判断一个元素是否存在于索引中。这比在 Python 列表中查找快得多，因为索引内部有哈希表等优化。
- **类型扩展 ("broadest data type")**: 当你对两种不同类型的索引进行运算时（比如一个整数索引和一个浮点数索引），结果会自动扩展为能容纳所有元素的“最宽”类型。`float` 比 `int` 宽，`object` (字符串) 比 `float` 宽。
- **`RangeIndex` 的运算**: 当对 `RangeIndex` 进行运算时，Pandas 会尝试返回一个 `RangeIndex`（如果结果仍然是连续的话），以保持内存优势。如果结果不再是连续的整数序列，它就会“退化”成一个普通的 `Int64Index`。

```python
idx1 = pd.Index([1, 2, 3, 4])
idx2 = pd.Index([3, 4, 5, 6])
idx_float = pd.Index([4.0, 5.0])

# 1. 交集 (&) 和 并集 (|)
print("--- 集合运算 ---")
print(f"idx1 & idx2 (交集): {idx1 & idx2}")
print(f"idx1 | idx2 (并集): {idx1 | idx2}\n")

# 2. 成员测试 (in)
print("--- 成员测试 ---")
print(f"3 in idx1? -> {3 in idx1}")
print(f"7 in idx1? -> {7 in idx1}\n")

# 3. 类型扩展
print("--- 类型扩展 ---")
union_result = idx1 | idx_float
print(f"整数索引和浮点数索引的并集: {union_result}")
print(f"结果类型: {type(union_result)}\n") # 结果是 Float64Index

# 4. RangeIndex 的运算
r_idx1 = pd.RangeIndex(start=0, stop=6) # 0,1,2,3,4,5
r_idx2 = pd.RangeIndex(start=4, stop=8) # 4,5,6,7
r_idx3 = pd.RangeIndex(start=10, stop=12) # 10,11

print("--- RangeIndex 运算 ---")
intersection_range = r_idx1 & r_idx2
print(f"r_idx1 & r_idx2: {intersection_range}")
print(f"结果类型: {type(intersection_range)}") # 结果仍然是 RangeIndex

union_fallback = r_idx1 | r_idx3
print(f"r_idx1 | r_idx3: {union_fallback}")
print(f"结果类型: {type(union_fallback)}") # 结果不连续，退化为 Int64Index
```

### String, Integer and Float Indexes (字符串、整数和浮点数索引)

不同数据类型会产生哪种具体的索引类。

- 字符串 (Strings)
  - 会生成一个通用的 `pd.Index` 对象。
  - 它的数据类型 `dtype` 是 `object`。
  - `object` 是一个“包罗万象”的类型，可以存储字符串、混合类型等任何 Python 对象。它的缺点是性能和内存效率不如专门的数字类型。
- 整数 (Integers)
  - 会生成一个专门的 `pd.Int64Index` 对象。
  - 这是为整数优化的，速度快，内存使用合理。
- 浮点数 (Floats)
  - 会生成一个专门的 `pd.Float64Index` 对象。
  - 为浮点数优化。

```python
# 字符串索引
idx_str = pd.Index(['a', 'b', 'c'])
print("--- 字符串索引 ---")
print(idx_str)
print(f"类型: {type(idx_str)}")
print(f"数据类型 (dtype): {idx_str.dtype}\n")

# 整数索引
idx_int = pd.Index([1, 2, 3])
print("--- 整数索引 ---")
print(idx_int)
print(f"类型: {type(idx_int)}\n")

# 浮点数索引
idx_float = pd.Index([0.1, 0.2, 0.3])
print("--- 浮点数索引 ---")
print(idx_float)
print(f"类型: {type(idx_float)}\n")
```

`pd.Index()` 是一个工厂函数，它会根据你传入的数据，自动为你创建最合适的、经过优化的索引对象子类。

### Pandas 中，索引值（标签）可以重复

```python
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
```

