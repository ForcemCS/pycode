https://numpy.org/doc/stable/

### 什么是数组？

数组是一种可以存储多个元素的数据结构。Python 的 `list` 就是一种非常灵活的数组。

#### Python list

1.  Python `list` 是一个类型的数组 

   ```python
   # 创建一个 Python 列表
   my_list = [10, "hello", 3.14, True]
   print(my_list)
   # 输出: [10, 'hello', 3.14, True]
   ```

2. 元素是可以索引的

   ```
   arr = [10, 20, 30, 40]
   # 获取第一个元素 (索引为 0)
   print(arr[0])  # 输出: 10
   # 获取第三个元素 (索引为 2)
   print(arr[2])  # 输出: 30
   ```

3. 数组可以被切片 

   ```
   arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
   # 获取从索引 2 到索引 5 (不包括 5) 的元素
   print(arr[2:5])  # 输出: [2, 3, 4]
   # 获取所有偶数索引的元素
   print(arr[0:10:2]) # 输出: [0, 2, 4, 6, 8]
   ```

4. 可变大小 

   对于 Python 的 `list`，你可以随时添加或删除元素，它的大小是动态变化的。

   ```python
   arr = [1, 2, 3]
   print("原始列表:", arr)
   # 添加一个元素到末尾
   arr.append(4)
   print("添加后:", arr) # 输出: [1, 2, 3, 4]
   # 删除一个元素
   arr.remove(2)
   print("删除后:", arr) # 输出: [1, 3, 4]
   ```

5. **异构性 (heterogeneous)**

   异构，意味着一个列表里可以存放不同数据类型的元素，比如整数、字符串、浮点数等。

   ```python
   hetero_list = [1, "apple", 3.5, False]
   print(hetero_list) # 可以正常工作
   ```

#### NumPy 数组 (ndarray)

主要特点是 **固定大小 (fixed size)** 和 **同质性 (homogeneous)**

### Python list vs NumPy ndarray

| 特性     | NumPy `ndarray`                                              | Python `list`                                |
| -------- | ------------------------------------------------------------ | -------------------------------------------- |
| 大小     | 固定大小 (fixed size)：创建后，大小不能改变。                | 可变大小 (variable size)：可以随时增删元素。 |
| 元素类   | 同质性 (homogeneous)：所有元素必须是相同的数据类型。         | 异构性 (heterogeneous)：元素可以是不同类型。 |
| 元素本质 | 元素是专门的、受限的数据类型（如 32 位整数）。               | 元素是完整的 Python 对象，开销较大。         |
| 高级操作 | 支持 **掩码 (masking)** 和 **花式索引 (fancy indexing)** 等高级、高效的操作。 | 不直接支持这些高级操作。                     |

```python
import numpy as np

# ---- 大小和类型对比 ----
# Python list (可变大小, 异构)
py_list = [1, "two", 3.0]
py_list.append(False) # 没问题
print("Python list:", py_list)

# NumPy ndarray (固定大小, 同质)
# 当我们用混合类型创建时，NumPy 会尝试统一成一种最兼容的类型（这里是字符串）
np_array = np.array([1, "two", 3.0])
print("NumPy array:", np_array) # 输出: ['1' 'two' '3.0'] -> 所有元素都变成了字符串！
# np_array.append(False) # 这会报错！NumPy 数组没有 append 方法。

# ---- 高级操作对比 ----
data = np.array([1, 5, 2, 8, 9, 4])
lst = [1, 5, 2, 8, 9, 4]

# 1. 掩码 (Masking) - 筛选出所有大于 3 的元素
mask = data > 3 # 这会创建一个布尔数组: [False, True, False, True, True, True]
print("NumPy 掩码结果:", data[mask]) # 输出: [5 8 9 4]

# 在 Python list 中实现同样效果，需要写循环
list_mask_result = [x for x in lst if x > 3]
print("Python list 实现掩码:", list_mask_result)

# 2. 花式索引 (Fancy Indexing) - 获取第 0, 3, 5 个位置的元素
indices = [0, 3, 5]
print("NumPy 花式索引结果:", data[indices]) # 输出: [1 8 4]

# 在 Python list 中实现同样效果，也需要写循环
list_fancy_result = [lst[i] for i in indices]
print("Python list 实现花式索引:", list_fancy_result)
```

### NumPy 效率 (NumPy Efficiency)

为什么愿意放弃 `list` 的灵活性，而去使用限制更多的 `ndarray`？

1. 优点 (Pros)

   - **更省空间 (more space efficient)**：因为 `ndarray` 存储的是紧凑的原始数据（比如纯粹的 8 字节整数），而 `list` 存储的是指向庞大的 Python 对象的指针，所以 `ndarray` 占用的内存小得多。
   - 数组操作和计算快得多 ：这是 NumPy 最重要的优势。
   - **矢量化 (vectorization)**：这是 NumPy 快的**秘诀**。矢量化意味着你可以对整个数组执行一个操作，而不需要写 Python 循环。NumPy 会在底层用高效的、预编译的 C 语言代码来循环处理，这比 Python 解释器逐个处理元素快几个数量级。

   **矢量化举例**：

   ```python
   # 假设我们有一个大数组，想让每个元素都乘以 2
   big_array = np.arange(1_000_000) # 创建一个从 0到999999 的数组
   big_list = list(range(1_000_000))
   
   # NumPy 的矢量化操作 (非常快)
   %timeit big_array * 2
   
   # Python list 的循环操作 (慢得多)
   %timeit [x * 2 for x in big_list]
   ```

2. 代价
   + **固定大小 (fixed size)**：一旦创建，就不能像 `list.append()` 那样添加或删除元素。虽然可以替换元素（`arr[0] = 100`），但不能改变数组的总长
   + **同质性 (homogeneous)**：所有元素必须是同一类型。如果试图存入不同类型，NumPy 会强制转换类型。
   + **数据类型 (data types)**：它使用 C 语言的底层数据类型（如 `int32`, `float64`），这正是它能实现内存效率和矢量化的原因。

#### Integer

Python 的普通整数 `int` 是一个非常“庞大”的对象，它可以自动扩展以表示任意大的整数，但这很浪费内存。在 NumPy 中，你可以精确地指定数据类型，从而大大节省内存。

```python
#假设你要存储 100 万个用户的年龄。年龄通常在 0-120 之间。
# 使用标准的 Python 列表
ages_list = [25, 30, 45] * 333334 # 模拟一个大列表
import sys
print(f"Python list 内存占用: {sys.getsizeof(ages_list)} bytes")

# 使用 NumPy，并指定一个非常合适的数据类型
# uint8 (无符号 8 位整数) 可以表示 0-255，足够存年龄了，而且每个数字只占 1 个字节 (8 bit)
ages_np = np.array([25, 30, 45] * 333334, dtype=np.uint8)
print(f"NumPy array 内存占用: {ages_np.nbytes} bytes")
```

#### Float

和整数一样，存储浮点数也需要占用一定数量的比特（bits）。使用的比特数决定了浮点数的**精度（precision）\**和能表示的\**范围（range）**，同时也影响内存占用。

1. Python 使用 64 比特来存储浮点数

   + 在标准的 Python 中，当你写 `x = 3.14` 时，这个 `3.14` 在内存中是用 64 个比特来存储的。这被称为“双精度浮点数”(double-precision float)，在 NumPy 中对应 `float64`。

   + 每个数字都占用 8 个字节（64 bits = 8 bytes），在处理海量数据时内存开销大。

2. C 语言有 32 比特的浮点数 (C also has 32-bit floats)
   + **存储效率更高 (but more efficient storage)**：每个数字只占用 4 个字节（32 bits = 4 bytes），内存占用减半！

```python
import numpy as np

# 一个有很多小数位的数字
pi_high_precision = 3.141592653589793

# 使用 NumPy 创建两种不同精度的浮点数数组
# 1. 默认的 64 位浮点数 (双精度)
arr64 = np.array([pi_high_precision], dtype=np.float64)

# 2. 指定为 32 位浮点数 (单精度)
arr32 = np.array([pi_high_precision], dtype=np.float32)

print("---- 精度对比 ----")
print(f"64-bit float (float64): {arr64[0]}")
print(f"32-bit float (float32): {arr32[0]}") # 注意看，精度丢失了！

print("\n---- 内存占用对比 ----")
print(f"一个 float64 元素占用: {arr64.itemsize} 字节") # itemsize 告诉我们每个元素占多少字节
print(f"一个 float32 元素占用: {arr32.itemsize} 字节")
```

**最重要的是：**在 NumPy 中你可以选择你的数据类型 ！！

```python
import numpy as np

# 例子1：为特定数据选择合适的类型
# 存储一批学生的年龄，年龄不可能是负数，也很少超过 255
student_ages = np.array([18, 19, 20, 19, 21], dtype=np.uint8)
print(f"学生年龄数组: {student_ages}")
print(f"数据类型: {student_ages.dtype}")
print(f"每个年龄占用内存: {student_ages.itemsize} 字节\n") # 非常节省空间！

# 例子2：选择错误类型的后果 —— 数据溢出 (Overflow)
# uint8 的最大值是 255。如果我们试图存储一个更大的数会怎样？
# 注意：NumPy 在这里会“回绕”(wrap around)
overflow_array = np.array([255], dtype=np.uint8)
print(f"原始值: {overflow_array[0]}")

overflow_array[0] = overflow_array[0] + 1 # 255 + 1
print(f"加 1 后的值: {overflow_array[0]}") # 结果变成了 0！(256 % 256 = 0)

overflow_array[0] = overflow_array[0] + 2 # 0 + 2
print(f"再加 2 后的值: {overflow_array[0]}") # 结果是 2

# 这就像一个时钟，过了 12 点又回到 1 点。
# 这是一个非常常见的 bug 来源，所以必须确保你选择的类型范围足够大！

# 例子3：NumPy 的类型推断
# 如果不指定 dtype，NumPy 会智能地为你选择一个合适的类型
inferred_array = np.array([1, 2, 300]) # 因为有 300，超过了 int8 的范围
print(f"\nNumPy 推断出的类型: {inferred_array.dtype}") # 可能是 int16 或 int32，取决于你的系统
```

### 矢量化 (Vectorization)

如何计算 `[1, 2, 3, 4] * [10, 20, 30, 40]` 得到 `[10, 40, 90, 160]`？

1. **纯 Python 的实现方法 (The Loop)**

   - 方法一：`for` 循环

     ```python
     a = [1, 2, 3, 4]
     b = [10, 20, 30, 40]
     result = []
     for i in range(len(a)):
         result.append(a[i] * b[i])
     print(result) # 输出: [10, 40, 90, 160]
     ```

   - 方法二：列表推导式 (List Comprehension)，这是一种更简洁的写法，但本质还是一样的循环。

     ```python
     result = [x * y for x, y in zip(a, b)]
     print(result) # 输出: [10, 40, 90, 160]
     ```

2. **为什么这个循环很慢？(at every loop, Python must:)**
   这才是关键！对于循环中的**每一次**乘法（比如 `a[0] * b[0]`），Python 解释器在幕后都必须做很多额外的工作：
   + 查找操作数对象 (lookup the operand objects)
     + Python 先要找到 `a[i]` 是什么。因为 Python 列表可以装任何东西，`a[i]` 只是一个指向某个内存地址的“指针”。Python 必须沿着这个指针找到那个代表数字 `1` 的 Python 对象。
     + 然后，它对 `b[i]` 做同样的事情，找到代表数字 `10` 的 Python 对象。
   + 确定类型 (determine the types)
     + 现在 Python 拿到了两个对象。它必须检查：“第一个对象是什么类型？哦，是 `int`（整数）。”，“第二个对象是什么类型？哦，也是 `int`。”
   + 尝试执行操作 (try to perform the operation)
     + 现在 Python 知道了类型，它会查找整数类型对应的 `*` 操作是什么（是数学乘法）。然后执行计算。
     + 幻灯片中提到的 `a * b` 不行就试 `b * a` 指的是 Python 的魔法方法 `__mul__` 和 `__rmul__`。这增加了 Python 的灵活性，但也是一种开销。

3. **C 语言不必做这些工作 (C does not have to do all that work)**
   - 像 C 这样的编译型语言，在代码运行前就已经知道了所有变量的类型（比如它们都是 32 位整数）。内存也是连续存储的。因此，C 语言可以直接在硬件层面进行快速的数学运算，没有任何上述的动态检查开销。这就是它**快得多 (significantly faster)** 的原因。

#### 矢量化 (Vectorization) - NumPy 的方式

不在 Python层面写循环，而是把整个操作（例如“两个数组相乘”）作为一个指令，交给 NumPy。NumPy 会在底层用一个高度优化的 C 语言循环来完成这个任务。

1. **NumPy 的实现方式 **
   - 前提条件 1: `a` 和 `b` 必须是 NumPy 数组 (`ndarray`)。
     - **为什么？** 因为 NumPy 数组是同质的（所有元素类型相同）并且数据在内存中是紧凑、连续存放的。这意味着 NumPy 从一开始就知道所有元素的类型和位置。
   - 前提条件 2: 使用的是 NumPy 支持的操作符或函数。
     - `a + b`、`a * b`、`a / b`、`np.sin(a)` 等等。
2. **通用函数 (Universal Functions - ufunc)**
   - 当你写 `a * b` 时，你实际上是在调用一个 NumPy 的**通用函数** `np.multiply(a, b)`。同样，`a + b` 调用 `np.add(a, b)`，`np.sin(a)` 调用 `np.sin` ufunc。
   - 这些 `ufunc` 是用 C 语言编写的，专门用来对整个数组进行快速、元素级的操作。
3. **魔法发生的地方 (NumPy pushes the loop and calculations down into C)**
   - 当你执行 `c = a * b`时：
     1. NumPy 不会在 Python 里循环。
     2. 它获取 `a` 数组的内存地址、`b` 数组的内存地址、数据类型（比如 `float64`）和数组长度。
     3. 它将这些信息**一次性**传递给底层的、预编译好的 C 函数。
     4. 这个 C 函数接管一切，运行一个极其高效的循环，直接在内存上操作原始数据，没有任何 Python 的开销。
     5. 计算完成后，它返回一个指向新结果数组的指针给 Python。
   - **这个将循环从 Python “推”到 C 的过程，就叫做“矢量化 (vectorization)”。**

```python
import numpy as np
import time

# 创建两个包含一百万个元素的大数组
size = 1_000_000
np_a = np.arange(size)
np_b = np.arange(size)

# --- 方法1: NumPy 矢量化 (The Fast Way) ---
start_time = time.time()
np_c = np_a * np_b
end_time = time.time()
print(f"NumPy 矢量化用时: {end_time - start_time:.6f} 秒")

# --- 方法2: Python 循环 (The Slow Way) ---
# 即使数据在 NumPy 数组里，用 Python 循环依然很慢
py_c = np.zeros(size, dtype=np.int64)
start_time = time.time()
for i in range(size):
    py_c[i] = np_a[i] * np_b[i]
end_time = time.time()
print(f"Python 循环用时:   {end_time - start_time:.6f} 秒")
```

