## dateutil

+ parser

  不需要告诉它时间字符串的确切格式，它能像人一样“聪明地”识别出大多数常见的日期时间格式。

  Python 自带的 `datetime.strptime()` 方法也能做字符串到 `datetime` 的转换，但它非常“死板”。你必须提供一个与字符串**完全匹配**的格式代码（如 `'%Y-%m-%d %H:%M:%S'`）。如果格式稍有不同，它就会报错。`dateutil.parser` 则灵活得多。

+ rrule

  它可以用来生成复杂的重复日期序列。比如“从今天起，未来三个月里，每周二和周四的日期是什么？”或者“每个月的最后一个工作日”。这在创建日历应用、计划任务等场景下非常有用。

### parser

我们来看这几个例子：

- **`parser.parse('2020-01-01T10:30:00')`**: 这是标准的 ISO 8601 格式，非常规范，解析它轻而易举。
- **`parser.parse('2020-01-01 10:30:00 am')`**: 注意，这里有空格，并且使用了 `am/pm` 表示法。`parser` 能够正确理解这是上午 10:30。
- **`parser.parse('12/31/2020')`**: 常见的“月/日/年”格式（美式）。
- **`parser.parse('31/12/2020')`**: 常见的“日/月/年”格式（欧式）。

**注意**: 默认情况下，`parser.parse()` 返回的是一个 **Naive **`datetime` 对象，它不包含时区信息。

### 处理模糊的月/日 (Ambiguous Month/Day)

- **`4/3/2020`**: 这个日期有歧义。它到底是 **4月3日** (美式：Month/Day) 还是 **3月4日** (欧式：Day/Month)？
- 当遇到这种无法明确判断的情况时，`parser` 必须做出一个选择。它的**默认行为**是遵循美式习惯，即**月份在前 (Month first)**。所以，`parser.parse('4/3/2020')` 会被解析成 **2020年4月3日**。
- 为了解决这个问题，`parse` 函数提供了一个非常有用的参数 `dayfirst`。
  + `parser.parse('2020/4/3')` → `datetime.datetime(2020, 4, 3, ...)` (默认 `dayfirst=False`，解析为4月3日)
  + `parser.parse('2020/4/3', dayfirst=True)` → `datetime.datetime(2020, 3, 4, ...)` (告诉解析器，当有歧义时，请**优先把第一个数字当作“日”**，所以解析为3月4日)

+ **`raises a ParserError`**: 如果字符串完全无法识别，或者是一个无效的日期（比如 `'2020/13/40'`），`parser` 会抛出 `ParserError` 异常，而不是返回一个错误的结果。

### 模糊解析 (Fuzzy Parsing)

这是 `parser` 最“神奇”的功能之一。

+ 模糊解析指的是，日期时间信息被嵌在一堆不相关的“垃圾”文本中。
+ **`→ March the 4th, 2020`**: 这个字符串里包含了 "the" 和 "th"，标准的解析器会失败，因为它不认识这些多余的词。
+ 启用这个功能，你需要使用 `fuzzy_with_tokens=True` 参数。当使用这个参数时，返回值不再是一个简单的 `datetime` 对象，而是一个**元组 (tuple)**。
  + 元组的**第一个元素**是它成功解析出的 `datetime` 对象。
  + 元组的**第二个元素**是另一个元组，包含了所有被它**忽略掉的**、不属于日期时间部分的文本。

```python
from dateutil import parser

result = parser.parse("Let's meet on March the 4th, 2020 at 3pm", fuzzy_with_tokens=True)
print(result)
```

输出会是：

```python
(datetime.datetime(2020, 3, 4, 15, 0), ('Let\'s meet on ', ' the ', ' ', ' at ', ''))
```

***需要注意的是：*它功能强大但有其局限性，并且默认返回 **naive`datetime` 对象。如果需要处理时区，你需要先用 `dateutil.parser` 解析出 naive 时间，然后再用 `pytz` 或 `zoneinfo` 对其进行 `localize`。