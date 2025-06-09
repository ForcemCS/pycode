from datetime import datetime, timezone, timedelta
#code1
##附带时区的时间
d1 = datetime.fromisoformat('2020-05-15T13:30:00-05:00')

tz_EDT = timezone(timedelta(hours=-4), 'EDT')
d2 = datetime(year=2020, month=5, day=13,
              hour=13, minute=30, second=0,
              tzinfo=tz_EDT)

print(d2)


naive_dt = datetime(2023, 10, 27, 10, 30, 0) 
print(f"naive时间: {naive_dt}, 时间: {naive_dt.tzinfo}")

#在naive时间的基础上增加时区信息
utc_dt  = naive_dt.replace(tzinfo=timezone.utc)
print(f"aware时间: {utc_dt}, 时区: {utc_dt.tzinfo}")

bj_offset = timedelta(hours=8)
bj_tz = timezone(bj_offset, name="BeijingTime")
bj_dt = naive_dt.replace(tzinfo=bj_tz)

print(f"aware时间: {bj_dt}, 时区: {bj_dt.tzinfo}")

#code2
##时区的转换(两者都需要与utc时间作为基准)

d1 = datetime.fromisoformat('2020-05-15T13:30:00-04:00')

tz_CDT = timezone(timedelta(hours=-5), 'CDT')                

d2 = d1.astimezone(tz_CDT)

print(d2)