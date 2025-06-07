# strftime: 把 时间对象 (struct_time) --> 格式化的 字符串。
# strptime: 把 字符串 --> 解析成 时间对象 (struct_time)。

##code1
from time import time,gmtime,strftime

now = time()

tomorrow = now + (24 * 60 * 60 )

print(gmtime(now),gmtime(tomorrow),sep='\n')

print(strftime("%Y/%m/%d", gmtime(now)))

##code2
from time import strptime

d = "2012-11-10"

print(strptime(d, "%Y-%m-%d"))


##code3

s = 'Monday, April 18, in the year 2020 CE'

f = '%A, %B %d, in the   year %Y CE'

print(strptime(s,f))