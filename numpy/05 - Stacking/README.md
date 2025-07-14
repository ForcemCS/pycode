### 数据类型 (`dtype`) 的处理

- 可以堆叠不同 `dtype` 的数组。
- NumPy 会自动决定一个合适的、能兼容所有输入数组的公共数据类型。
- 我们无法在堆叠时直接控制这个选择。
- 例如：将 `uint8`, `uint16`, `int64` 堆叠，NumPy 会选择 `float64`。

在 NumPy 中，这个过程叫做“**类型提升 (Type Promotion)**”。当 `vstack` 或 `hstack` 这样的函数接收到多个不同 `dtype` 的数组时，它必须为新生成的数组找到一个“最通用”或“最安全”的数据类型，这个类型必须能容纳下所有输入数组中的数据而不丢失信息。

### 如何控制最终的数据类型

- 我们可以通过**事先转换**输入数组的类型来间接控制结果的类型。
- 使用数组的 `.astype()` 方法进行转换。
- 示例：在 `vstack` 之前，将所有数组都用 `.astype(np.int64)` 转换。

```python
import numpy as np

# 创建两个不同类型的数组
arr1 = np.array([1, 2, 3], dtype=np.int8)      # 类似“小杯”整数
arr2 = np.array([4.0, 5.0, 6.0], dtype=np.float32) # 类似“中杯”浮点数

# 1. 不加控制的堆叠
stacked_auto = np.vstack([arr1, arr2])
print(f"自动选择的类型: {stacked_auto.dtype}")
# 输出: 自动选择的类型: float32  (因为float32比int8更通用)
print(stacked_auto)
# [[1. 2. 3.]
#  [4. 5. 6.]]

# 2. 我们想强制结果为 int64
# 先把所有“原料”都用 astype 转换成我们想要的类型
arr1_converted = arr1.astype(np.int64)
arr2_converted = arr2.astype(np.int64) # 注意：这里浮点数的小数部分会被截断！

print(f"\narr2 转换后的值为: {arr2_converted}") # 输出：[4 5 6]

# 现在用转换后的数组进行堆叠
stacked_controlled = np.vstack([arr1_converted, arr2_converted])

print(f"\n我们控制的类型: {stacked_controlled.dtype}")
# 输出: 我们控制的类型: int64
print(stacked_controlled)
# [[1 2 3]
#  [4 5 6]]
```

### 堆叠数组与原始数组的独立性

- 之前我们看到 `reshape` 操作可能与原数组“链接”（即共享内存，称为“视图”）。
- 堆叠（Stacking）操作并非如此。
- 修改堆叠后的新数组，不会影响原始数组。
- 修改原始数组，也不会影响堆叠后的新数组。

这是 NumPy 中一个至关重要的概念：**视图 (View) vs 副本 (Copy)**。

- **视图 (View)**：像一个快捷方式或一个别名。它只是对**同一块内存数据**的一种新的“看法”（比如不同的形状）。修改视图就是修改原始数据。`reshape` 和数组切片 `arr[:]` 常常会产生视图。
- **副本 (Copy)**：像复印了一份文件。它会开辟一块**全新的内存空间**，把原始数据复制过去。修改副本和原件互不相干。

```python
import numpy as np

# 原始数组
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])

# 堆叠它们
stacked_arr = np.vstack([arr1, arr2])

print("--- 初始状态 ---")
print("arr1:\n", arr1)
print("stacked_arr:\n", stacked_arr)

# 修改堆叠后的数组
print("\n--- 修改 stacked_arr[0, 0] 为 99 ---")
stacked_arr[0, 0] = 99

print("stacked_arr 现在是:\n", stacked_arr)
print("arr1 仍然是 (未受影响):\n", arr1) # arr1的(0,0)位置还是1

# 修改原始数组
print("\n--- 修改 arr1[1, 1] 为 -5 ---")
arr1[1, 1] = -5

print("arr1 现在是:\n", arr1)
print("stacked_arr 仍然是 (未受影响):\n", stacked_arr) # stacked_arr的(3,1)位置还是8

```
