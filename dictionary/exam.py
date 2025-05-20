#ord() 是 Python 的一个内置函数，用来获取一个字符对应的 Unicode 编码（整数）。
#必须是一个长度为 1 的字符串（单个字符）
a = tuple((ord('a'),ord('z')))
print(a)

##测试1
s = 'Aa, Bb - A a a B C'

count = {}
for c in s:
    if ((ord(c) >= ord('a') and ord(c) <= ord('z')) or (ord(c) >= ord('A') and ord(c) <= ord('Z'))):
        count[c] = count.get(c, 0 ) + 1
print(count)

##测试2
d1 = {'a': 10, 'b': 20, 'c': 30}
d2 = {'d': 100, 'e': 200, 'f': 300}
d3 = {'f': 30, 'g': 40}

k_l = []
d  = [d1, d2, d3]
for  idx in  range(len(d)):
    for k  in  d[idx]:
        k_l.append(k)
print(k_l)


keys = []
values = []
for d  in (d1, d2, d3):
    for k, v in d.items():
        keys.append(k)
        values.append(v)
print(keys,values,sep='\n')


### 我们还可以使用list + ,+ 不会修改原列表 a 或 b，而是创建一个新列表。
### a + b	合并两个列表，返回新列表
### a += b	把 b 的元素追加到 a
### a.append(x)	把单个元素 x 添加到末尾
### a.extend(b)	把另一个列表 b 的所有元素追加到 a

a  =  list(d1.keys()) + list(d2.keys()) + list(d3.keys())
print(a)
print('-' * 10)

##测试3
grades = {
    'John': [90, 95, 98],
    'Eric': [86, 84, 92],
    'Michael': [90, 89, 85]
}

exam = {
    'Eric': 99,
    'John': 100
}

print(exam.get('Michael'))

print(grades['John'])

for name in  grades.keys():
    grades[name].insert(0, exam.get(name))
print(grades)