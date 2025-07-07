import pytz

from datetime import datetime, timezone

## code 1
a = pytz.timezone('Asia/Shanghai')
print(type(a))
b = a.zone
print(type(b))

tz_utc = pytz.timezone('UTC')
print(tz_utc,type(tz_utc),tz_utc.zone)

print('-' * 20 )


## code 2 

dt_naive = datetime(2025, 7, 7, 10, 0, 0)

print(dt_naive,type(dt_naive))

dt_shanghai = a.localize(dt_naive)

#附加时区信息
print(dt_shanghai)
print(dt_naive.replace(tzinfo=a))                 ## 这种方式是不推介的！！！！


## code 3

tz_melbourne = pytz.timezone('Australia/Melbourne')

##将上海时间转为墨尔本时间
dt_shanghai_to_melbourne = dt_shanghai.astimezone(tz_melbourne)
print(dt_shanghai_to_melbourne)

##转为utc时间

print(dt_shanghai.astimezone(pytz.utc))


# code 3

now_utc = datetime.now(pytz.utc)
print(now_utc)

now_shanghai = datetime.now(pytz.timezone('Asia/Shanghai'))
print(now_shanghai)