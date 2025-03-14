## ASCII 

ASCII 通过 **数值编码** 映射到 **字符**，包括可打印和不可打印的字符。

ASCII 编码使用 **7 个二进制位（bits）** 来表示一个字符的数值。也就是说，ASCII 编码可以表示 **0 到 127** 之间的 128 个字符。

95个可打印的字符，33个不可打印的字符

**ASCII**（只支持 128 个字符），但是它太有限，无法满足世界上不同语言的需求。于是人们尝试扩展 ASCII，但这些扩展标准不统一，导致混乱。

nicode 主要解决字符编码混乱的问题，它的 核心目标是：

+ 为每个字符分配一个唯一的编号（称为 **code point**，即 "代码点"）。

+ 不规定代码点如何存储到计算机的二进制格式中，而是交由编码方式（如 UTF-8、UTF-16）去决定。

**Python 默认使用 UTF-8**

- **UTF-8** 是 Unicode 的一种编码方式，它是 **Python 默认使用的编码**。
- 其他编码方式还包括 UTF-16、UTF-32，但它们不如 UTF-8 常见。

## 进制的转换

<img src="./img/1.png" alt="1" style="zoom:50%;" />

## 字符串方法

请[参考](https://docs.python.org/3/library/stdtypes.html#string-methods)

**Note: **字符串是不可变的（immutable）

### 常见分类

- **大小写转换（case conversions）**：例如 `.upper()`、`.lower()`、`.capitalize()`、`.title()`

  + ```python
    'Hello World'.lower()         # 结果: 'hello world'
    'python'.upper()              # 结果: 'PYTHON'
    'one two three'.title()       # 结果: 'One Two Three'
    ```

  + 注意有些unicode字符是无大小写的
  + 不区分大小写的比较 `casefold()`

- **删除字符串两端的特定字符（stripping start and end characters）**：例如 `.strip()`（去除首尾空格）、`.lstrip()`（去除左侧空格）、`.rstrip()`（去除右侧空格）

- **字符串拼接（concatenating strings）**：使用 `+` 或者 `join()` 方法

- **拆分和合并字符串（splitting and joining strings）**：例如 `.split()`（拆分字符串）、`.join()`（合并字符串）

- **查找子字符串（finding substrings）**：例如 `.find()`（查找子字符串索引）、`.count()`（统计出现次数）
