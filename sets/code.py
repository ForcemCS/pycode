s1 = set('abc')
s2 = {True, False}
s3 = ('a', 100, 200)

print(s1.isdisjoint(s2))  #s1中的任一个元素在s2没有发现

s = set()
s.add(4)
print(s)


s1 = set('abc')
s2 = set('bcd')

print(s1 <= s2)
print(s1 | s2)
print(s1 & s2)

print(s1 - s2 )

s1 = {'FB', 'AMZN', 'AAPL', 'NFLX', 'GOOG', 'MSFT'}
s2 = {'BABA', 'WMT', 'COST'}
s3 = {'TSLA', 'F', 'GM'}

s = s1 | s2 |s3
print(type(s).__name__,s)

s_list = list(s1 | s2 |s3)

print(s_list)

alphabet = set('abcdefghijklmnopqrstuvwxyz')

import string               #导入Python 内置的 string 模块，它提供了很多和字符串相关的工具。

a = string.ascii_lowercase  #string.ascii_lowercase 是 string 模块内置的一个字符串，包含了所有的小写字母：
print(a)

print(alphabet)
print(set(string.ascii_lowercase))

print(string.ascii_letters.casefold())
