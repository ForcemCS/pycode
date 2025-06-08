from datetime import date,timedelta,datetime,timezone

#code1
##timedelta表示预设的时间插值
delta_one_day = timedelta(days=1)
print(f"One day: {delta_one_day}")

delta_two_hours_30_mins = timedelta(hours=2, minutes=30)
print(f"Two hours and 30 minutes: {delta_two_hours_30_mins}")

delta_complex = timedelta(weeks=1, days=2, hours=3, minutes=4, seconds=5, milliseconds=6, microseconds=7)
print(f"Complex delta: {delta_complex}")
print(f"Total seconds in complex delta: {delta_complex.total_seconds()}")

print(datetime.now())

#code2
## timezone 对象表示一个与UTC（协调世界时）的固定偏移量。它是 tzinfo 抽象基类的一个简单实现。
##timezone(offset, name=None)
##offset: 一个 timedelta 对象，表示与UTC的偏移。例如，timedelta(hours=8) 表示 UTC+8。timedelta(hours=-5) 表示 UTC-5。

## 东八区 (UTC+8)
offset_8_hours = timedelta(hours=8)
beijing_zone = timezone(offset_8_hours, name="BeijingTime")
print(f"Beijing Zone: {beijing_zone}, Offset: {beijing_zone.utcoffset(None)}")

## 将 timezone 用于 datetime 对象
dt_now_utc = datetime.now(timezone.utc)
print(f"Current datetime in UTC: {dt_now_utc}")

dt_now_beijing = datetime.now(beijing_zone)
print(f"Current datetime in Beijing (fixed offset): {dt_now_beijing}")