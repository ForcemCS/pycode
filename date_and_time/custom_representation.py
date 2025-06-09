# strftime is available for:
#   → datetime.time
#   → datetime.date
#   → datetime.datetime

# strptime is available for:
#   → datetime.datetime


from datetime import date,time,datetime

##code1 时间信息的载入
t = time(22, 30, 45)
print(t.strftime("The time is: %I hours,  %M minutes, and %S seconds, %p"))


d = date(2020,5,15)
print(d.strftime("%B %d, %Y"))

dt = datetime(2020, 5, 15, 22, 10, 5)
print(dt.strftime("%I:%M %p on %B %d, %Y"))

##code2 提取字符串中的时间

dt = datetime.strptime('10:10 PM on May 15, 2020', '%I:%M %p on %B %d, %Y')
print(dt)

print(dt.isoformat())

a = dt.fromisoformat('2020-05-15T22:10:00')

print(type(a),a)

## code3

b  = datetime.fromisoformat('2020-05-15T22:10:00-05:00')
print(b.tzinfo)