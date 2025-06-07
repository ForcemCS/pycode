### ISO Format

```
YYYY-MM-DDTHH:MM:SS[.nnnn][±HH:MM or Z]
```

| 部分     | 含义                        | 举例                       |
| -------- | --------------------------- | -------------------------- |
| `YYYY`   | 年份（4位）                 | `2025`                     |
| `MM`     | 月（2位）                   | `01`, `12`                 |
| `DD`     | 日（2位）                   | `01`, `28`                 |
| `T`      | 分隔符（Date 和 Time 之间） | 就是字母 `T`               |
| `hh`     | 小时（24小时制）            | `14`, `23`                 |
| `mm`     | 分钟                        | `00`, `59`                 |
| `ss`     | 秒                          | `00`, `59`                 |
| `.nnnn`  | 小数秒（可选）              | `14:30:45.1234`            |
| `±hh:mm` | 与 UTC 的偏移（时区）       | `+08:00`, `-05:00`         |
| `Z`      | 替代 `+00:00`，表示 UTC     | 例：`2025-06-07T12:00:00Z` |

**冒号有时会被省略**：`+0800` 等同于 `+08:00`

**小数秒是可选的**：通常用于精密记录，但可以不写。

**Z 是最常见的简写**：代表 UTC（协调世界时间）

✅ 举几个完整的例子：

| ISO 时间字符串              | 含义                                  |
| --------------------------- | ------------------------------------- |
| `2025-06-07T12:00:00Z`      | UTC 时间中午 12 点                    |
| `2025-06-07T20:00:00+08:00` | 北京时间晚上 8 点                     |
| `2025-06-07T14:30:00-05:00` | 美中时间下午 2:30（比 UTC 晚 5 小时） |

```python
from datetime import datetime

# ISO 格式的字符串
iso_str = "2025-06-07T12:00:00Z"

# 解析成 datetime 对象（自动处理 Z）
dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
print("UTC 时间对象:", dt)

```
dateutil
  能自动识别各种格式的字符串

```
from dateutil import parser

dt = parser.parse("March 1, 2020 2:35:01pm")
print(dt)  # 2020-03-01 14:35:01
```

pytz
  提供完整的时区支持，包括夏令时切换
  可以让你：
  给“无时区的时间”加上时区
  在时区之间做转换

```
from datetime import datetime
import pytz

tz = pytz.timezone("US/Eastern")
dt = tz.localize(datetime(2020, 5, 1, 10, 23, 35))  # 自动处理夏令时
print(dt.astimezone(pytz.utc))  # 转成 UTC 时间
```


最佳实践（Python 中）：
1.用户传入时间字符串
2.用 dateutil.parser 解析为 datetime 对象
3.用 pytz 加上合适的时区
4.转为 UTC 保存
5.需要展示时，再转成用户时区

### Epoch 时间（时间戳）

基准时间点是

```
1970年1月1日 00:00:00 UTC
```

Epoch Time 的定义：

+ 某个时间距离“epoch”的**总秒数**

  比如：

  + `1970-01-01T00:00:00Z` → `0`
  + `1970-01-01T00:00:01Z` → `1`
  + `2020-05-01T14:23:35Z` → `1588343015.0`

+ 它是一个浮点数，单位是“秒”。

### datetime 模块

`datetime` 模块提供了 3 种主要对象类型：

| 类型       | 说明                | 示例                  |
| ---------- | ------------------- | --------------------- |
| `date`     | 只有日期（年月日）  | `2025-06-07`          |
| `time`     | 只有时间（时分秒）  | `13:45:00`            |
| `datetime` | 同时包含日期 + 时间 | `2025-06-07 13:45:00` |

这个模块支持**时区处理**（配合 `timezone` 或 `pytz` 模块使用）。

- 给 `datetime` 对象**加上时区信息**
- 在多个时区之间**转换时间**

```python
from datetime import datetime, timezone, timedelta

dt = datetime(2025, 6, 7, 10, 0, tzinfo=timezone.utc)
print(dt)  # 2025-06-07 10:00:00+00:00
```

支持把时间对象：

- ➡️ **格式化为字符串**
- ⬅️ **从字符串解析为时间对象**

✅ 格式化：

```
python复制编辑dt.strftime("%Y-%m-%d %H:%M:%S")
# 输出: '2025-06-07 13:45:00'
```

✅ 解析：

```
python复制编辑from datetime import datetime
datetime.strptime("2025-06-07 13:45:00", "%Y-%m-%d %H:%M:%S")
# 输出: datetime.datetime(2025, 6, 7, 13, 45, 0)
```

⚠️ 缺点是 `strptime()` 需要你**明确知道格式**，不如 `dateutil.parser.parse()` 智能。

#### 例子

计算时间差

```python
from datetime import datetime

start = datetime(2025, 6, 7, 8, 0)
end = datetime(2025, 6, 7, 10, 30)

delta = end - start
print(delta)             # 2:30:00
print(delta.total_seconds())  # 9000.0 秒
```
