from datetime import datetime,timedelta,timezone

s = "2025-06-09T11:00:00-07:00"

a = datetime.fromisoformat(s)
print(a)

##转为utc时间，程序内部使用
#b = a.replace(tzinfo=timezone.utc)
b = a.astimezone(timezone.utc)
print(b)

##程序结束之后再转为-7

c = b.replace(tzinfo=timezone(timedelta(hours=-7)))
print(c)


