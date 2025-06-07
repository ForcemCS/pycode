##code1 
from datetime import time,timezone, timedelta

opening_time = time(hour=9, minute=30)
closing_time = time(22, 0)
print(f"商店开门时间: {opening_time}")
print(f"商店关门时间: {closing_time}")

#code2
naive_time  = time(10,0)
print(type(naive_time).__name__)
print(naive_time.tzinfo)             #None 没有时区信息


##code2
utc_zone  = timezone.utc

cst_zone  = timezone(timedelta(hours=8), 'CST')

aware_time_cst = time(18, 0, tzinfo=cst_zone)

print(aware_time_cst,aware_time_cst.tzinfo)

##code3
t = time(hour=14, minute=5, second=30, microsecond=123456,tzinfo=cst_zone)
print(t.hour)

## time.fromisoformat(s) 和 <time_obj>.isoformat()
# 这是一对用于在 时间对象 和 标准格式字符串 之间进行转换的方法。
# ISO 8601 是一种国际通用的、无歧义的日期和时间表示格式。对于时间来说，它看起来像 HH:MM:SS.ffffff，如果带时区，则像 HH:MM:SS.ffffff+08:00。
# <time_obj>.isoformat(): 将一个 time 对象 转换成 ISO 格式的字符串。
# time.fromisoformat(s): 将一个 ISO 格式的字符串 解析成 time 对象

my_time  = time(15,33)
iso_string = my_time.isoformat()

print(type(iso_string).__name__, iso_string)


time_str = "10:30:55.500"  #ISO格式
new_time = time.fromisoformat(time_str)

print(new_time)