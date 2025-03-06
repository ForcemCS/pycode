print('Demo1')

for i in range(10):
    print(i)

print('Done') 

l = [10, 20, 30]

#输出<class 'list'>，表示l时list类，list是对象，对象有状态和functionality
print(type(l))
print(type(l).__name__)
print(l[1])
print(l[len(l) - 1])

#修改列表的元素
l[2] = 3.14

print(l)

##创建空列表
a = []
print(a)

b = list()
print(b, type(b).__name__)

## tuple类型
t = 10, 20, [True, True]
t[2][0] = False

print(t, type(t).__name__)

a = 10
b = 20

##实际上创建了一对元组
print(a, b, a + b )

##将list转变为tuple

c = [1, 2, 3]
t = tuple(c)
print(t)

##字符串的使用

t = 1, 2, 3
s= str(t)
print(s,type(s).__name__)
###输出(
print(s[0]) 

s = "Python"
t = tuple(s)

print(t,t[1])

##巧将字符串转化为列表
l = list("abcd")
print(l)

t = ( [1, 2], 30)

s = t * 2

print(s)

print(t[0] is s[0])

m = [0, 0, 0] * 3

print(m)

##切片的使用
l = [10, 20, 30, 40, 50]

t = l[::-1]
print(t)