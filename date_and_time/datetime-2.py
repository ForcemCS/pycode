#code1
import datetime

now = datetime.date.today()
print(now)

##code2

import time

dt = datetime.date.fromtimestamp(time.time())   #将epoch时间转为日期
print(dt)

dt = datetime.date.fromisoformat('2022-12-12')
print(dt)


cst_zone  = datetime.timezone(datetime.timedelta(hours=8), 'CST')

print(type(cst_zone).__name__)


##code3

d = datetime.datetime(2020, 4, 2, 18, 30, 30, tzinfo=datetime.timezone(datetime.timedelta(days=-1, seconds=61200)))
print(d)