##datetime时间点，有时区信息属性
##timedelta预设的时间间隔
from datetime import datetime,timezone,timedelta,date

#code1
#d1= datetime.now()    ##获取到的是当前计算机环境的时间
d1 = datetime.now(timezone.utc)      #创建一个**“感知型”(aware)** 的 datetime 对象。这意味着 d1 不仅知道日期和时间，还明确知道它代表的是 UTC (协调世界时) 时间。它的 tzinfo 属性会被设置为 timezone.utc。
print(d1,d1.tzinfo,sep="\n")

d2 = datetime.fromisoformat("2026-01-01T00:00:00")    ##字符串格式化为时间
print(d2,d2.tzinfo,sep="\n")

#td = d2 - d1           #这段代码会报错，d1是aware对象，d2是naive对象
td = d2.replace(tzinfo=timezone.utc) - d1
print(td,type(td).__name__, sep="\n")
print(td.total_seconds())


#code2

td = timedelta(hours=2, minutes=30)
print(td)
print(td.days,td.seconds)

#code3

s = "2025-12-30T11:59:00"

dt  = datetime.fromisoformat(s)
print(dt)

start = datetime(year=dt.year, month=dt.month,day=1)
print(start)

start = date(year=dt.year,month=dt.month,day=dt.day)
print(start)

delta = timedelta(hours=50,minutes=30)

print(start + delta)


#code3

end = date(2023,3,1)
print(end - timedelta(days=1))