### pytz

https://pythonhosted.org/pytz/

IANA 时区数据库（也叫 Olson 数据库）是全球公认的、最权威的时区信息集合。它不仅包含了全球所有时区，还记录了每个时区历史上所有的变更，比如夏令时的开始和结束日期（这些规则每年都可能变）。`pytz` 把这个数据库带到了 Python 里。

夏令时是时区处理中最头疼的问题。比如美国纽约，冬天是 `-05:00` (EST)，夏天是 `-04:00` (EDT)。`pytz` 能根据你给出的具体日期，自动判断当时是否处于夏令时，并使用正确的 UTC 偏移量。

`pytz` 使用标准的 `Area/Location` (大洲/城市) 格式来命名时区，例如 `America/New_York`, `Europe/Paris`, `Asia/Shanghai`。这种命名方式是唯一的，不会产生歧义。要避免使用像 `EST`, `CST` 这样的缩写，因为它们在不同国家可能代表不同的时区。

#### 用法和创建时区对象

+ **`pytz.all_timezones`**: 这个变量是一个巨大的列表，包含了 `pytz` 支持的所有时区的名字（比如 `'America/New_York'`, `'Asia/Tokyo'` 等）。
+ **`pytz.timezone('US/Eastern')`**: 这是获取一个具体时区对象的**标准方法**。你传入一个时区名称，它会返回一个代表该时区的 `tzinfo` 对象。
+ **`pytz.UTC`**: 这是一个方便的快捷方式，可以直接获取世界标准时间（UTC）的时区对象。
+ **NOTE:  `datetime(..., tzinfo=pytz.timezone(...))`**: **这是一个巨大的陷阱!** 因为 `pytz` 的时区对象内部有复杂的 DST 逻辑，直接通过构造函数附加，在夏令时切换的边界时刻会产生错误
+ `localize` (让 Naive 变 Aware)

#### Naive and Aware

##### naive

通常，当你直接创建一个 `datetime` 对象而不指定 `tzinfo`时，得到的就是 Naive 对象。

```python
from datetime import datetime

# 创建一个 naive datetime 对象
naive_time = datetime(2023, 10, 27, 9, 30, 0)

print(naive_time)        # 输出: 2023-10-27 09:30:00
print(naive_time.tzinfo) # 输出: None
```

这个 `naive_time` 只是“某个地方的上午9点30分”，至于具体是哪里，它自己一无所知。

##### aware

+ ##### 一个 Aware 的 `datetime` 对象**包含了足够的时区信息，可以 unambiguous (毫不含糊地) 定位到世界时间线上的一个特定时刻**。

+ 它的 `tzinfo` 属性是一个具体的时区对象（不是 `None`）。这个对象包含了 UTC 偏移量（比如 `+08:00`）和夏令时（DST）规则。例如，`2023-10-27 09:30:00+08:00` 就明确表示这是东八区的上午9点30分。

+ 你可以轻松地将一个 Aware 对象转换到任何其他时区，或者与其他 Aware 对象进行比较，因为它们都有一个共同的参照系（通常是 UTC）。

#### localize (让 Naive 变 Aware)

+ `localize` 方法的作用是：**解释 (interpret)** 一个 "naive" 的 `datetime`。
+ `localize` 不是“转换”，而是“附加”或“说明”。如下：
  - `naive_dt = datetime(2023, 1, 1, 8, 0, 0)` // 一个天真的时间：早上8点
  - `tz_ny = pytz.timezone('America/New_York')`
  - `aware_dt = tz_ny.localize(naive_dt)` // 告诉程序，这个8点是“纽约的早上8点”
+ 执行后，`aware_dt` 的值看起来还是 `2023-01-01 08:00:00`，但它内部已经包含了纽约时区的信息 (`-05:00`)，它现在是一个 "aware" 对象了。`pytz` 会自动帮你计算好 DST，比如如果你 `localize` 的是一个7月的时间，它会自动使用夏令时偏移量。

#### astimezone (在 Aware 对象之间转换)

+ 只有 "aware" 的对象才能进行时区转换，因为程序需要一个明确的“时间锚点”才能计算其他时区的时间。

+  `astimezone()` 是 `datetime` 对象自带的方法。当 `datetime` 对象是 "aware" 的时候，这个方法就能正常工作。

+ 例如

  ```python
  import pytz
  from datetime import datetime
  
  # 1. 创建一个 naive datetime
  naive_dt = datetime(2023, 11, 10, 9, 0, 0) # 假设这是纽约当地时间上午9点
  
  # 2. 使用 localize 使其变为 aware
  tz_ny = pytz.timezone('America/New_York')
  aware_ny_dt = tz_ny.localize(naive_dt)
  print(f"纽约时间: {aware_ny_dt}") # 输出: 纽约时间: 2023-11-10 09:00:00-05:00
  
  # 3. 使用 astimezone 转换到其他时区
  tz_paris = pytz.timezone('Europe/Paris')
  aware_paris_dt = aware_ny_dt.astimezone(tz_paris)
  print(f"巴黎时间: {aware_paris_dt}") # 输出: 巴黎时间: 2023-11-10 15:00:00+01:00
  
  tz_shanghai = pytz.timezone('Asia/Shanghai')
  aware_shanghai_dt = aware_ny_dt.astimezone(tz_shanghai)
  print(f"上海时间: {aware_shanghai_dt}") # 输出: 上海时间: 2023-11-10 22:00:00+08:00
  ```

  你会看到，纽约的上午9点，确实是巴黎的下午3点和上海的晚上10点。`astimezone` 完美地完成了**转换**工作。