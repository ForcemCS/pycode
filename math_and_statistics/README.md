### 分位数函数

#### `quantiles(s, *, n=4, method='exclusive')`

- **作用**: 将数据从小到大排序后，分成 `n` 个包含相同数量数据点的连续区间，然后返回作为分割点的数值列表。

- **参数详解**:

  - `s`: 输入的数据序列。

  - ```
    n
    ```

    : 要将数据分成的区间数量。

    - `n=4` (默认值): 计算 **四分位数 (quartiles)**。返回 3 个分割点，将数据分为 4 部分。这三个点通常称为 Q1 (第一四分位数), Q2 (第二四分位数，即中位数), 和 Q3 (第三四分位数)。
    - `n=100`: 计算 **百分位数 (percentiles)**。返回 99 个分割点。
    - `n=10`: 计算 **十分位数 (deciles)**。返回 9 个分割点。

  - ```
    method
    ```

    : 计算分割点的方法，主要有两种：

    - `'exclusive'` (默认值): "排除"法。适用于数据 `s` 是从一个更大的总体中抽取的**样本**。它认为数据点是位于分割点之间的观测值。
    - `'inclusive'`: "包含"法。适用于数据 `s` 本身就是所研究的**总体**，或者你的数据明确包含了总体的最小值和最大值。它将数据中的最小值和最大值视为第 0 和第 100 百分位数。

- **示例**:

  ```python
  # 准备一个有11个点的数据，方便观察分割
  data = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110]
  
  # 1. 计算四分位数 (默认 n=4, method='exclusive')
  # 将数据分成4份，需要3个分割点
  quartiles = statistics.quantiles(data)
  print(f"四分位数 (Quartiles): {quartiles}")
  # 输出: 四分位数 (Quartiles): [35.0, 60.0, 85.0]
  # 解释: 
  # - 25% 的数据小于 35.0 (Q1)
  # - 50% 的数据小于 60.0 (Q2, 中位数)
  # - 75% 的数据小于 85.0 (Q3)
  
  # 2. 计算十分位数 (Deciles)
  deciles = statistics.quantiles(data, n=10)
  print(f"\n十分位数 (Deciles): {deciles}")
  # 输出: 十分位数 (Deciles): [21.0, 32.0, 43.0, 54.0, 65.0, 76.0, 87.0, 98.0, 109.0]
  
  # 3. 方法对比示例
  short_data = [1, 2, 3, 4, 5]
  
  # 'exclusive' 方法通常用于样本
  exclusive_q = statistics.quantiles(short_data, n=4, method='exclusive')
  print(f"\nExclusive Quartiles: {exclusive_q}")
  # 输出: Exclusive Quartiles: [1.5, 3.0, 4.5]
  
  # 'inclusive' 方法认为数据本身是完整的
  inclusive_q = statistics.quantiles(short_data, n=4, method='inclusive')
  print(f"Inclusive Quartiles: {inclusive_q}")
  # 输出: Inclusive Quartiles: [2.0, 3.0, 4.0]
  ```