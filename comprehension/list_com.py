##different types of  comprehension
## 1. lists 2. dictionaries 3.sets 4.generators

#Python 中的推导式（Comprehensions）是一种非常强大且简洁的语法，可以用来从一个或多个迭代器（如列表、元组、集合、字典等）快速创建新的列表、集合、字典，或者生成器。
#理解推导式的核心在于：它们本质上是 for 循环的紧凑写法，通常还可能带有一个可选的 if 条件判断。

vectors = [(0, 0), (0, 1), (1, 0), (1, 1)]

from  math  import sqrt   #square root 函数

magnitudes = []   #向量的大小

for vector in  vectors:
    magnitude = sqrt(vector[0] ** 2 + vector[1] ** 2)
    magnitudes.append(magnitude)
print(magnitudes)

#接下来使用comprehension 

magnitudes = [ sqrt(vector[0] ** 2 + vector[1] ** 2 ) for vector in vectors  ]
print(magnitudes)

#perf_counter() 的主要用途是性能分析和基准测试，即精确测量某段代码执行所花费的时间。
#单调性 (Monotonicity - 通常情况下): 它的值只会增加，不会因为系统时间被调整（例如，NTP同步、用户手动修改时间）而向后跳。这使得它非常适合测量代码段的执行时间。
#单个 perf_counter() 的返回值本身没有意义。你总是需要取两次调用的差值来计算时间间隔。
#我们可以使用这个函数来测试执行的时间（代码省略）
from  time import perf_counter

a  = 'Python is an awesome language'.split(' ', -1)   #-1表示最多分割的次数

print(a)
print('-' * 10)

sales = {
    'widget 1': 0,
    'widget 2': 5,
    'widget 3': 10,
    'widget 4': 2
}

high_sales = []
for k, v in  sales.items():
    if v >= 5:
        print(k)
        high_sales.append(k)
print(high_sales)

high_sales = [k for k,v  in sales.items() if v >= 5]
print(high_sales)
print('-' * 10)

m = [[0] * 3] * 3   # 这三个子列表，其实是同一个对象的三次引用！
print(m)
print(m[0] is m[1])

#我们可以使用list comprehension 来生成新的行对象
m = [ [0, 0, 0 ]  for _ in  range(3) ]

print(m)
m[0][0] = 1
print(m)

m = [ [0] * 3   for _ in  range(3) ]

print(m)
m[0][0] = 1
print(m)

##接下来我们将快速的创建一个单位阵(1)
m =  [ [0] * 3  for  _ in range(3)]

for row in range(3):
    for col in  range(3):
        if row == col:
            m[row][col] =1 
print(m)
print('-' * 10)

#快速创建单位阵的第二个方法
m  =  [ [1 if row == col else 0  for col in range(3)] for row in range(3) ]
print(m)
print('-' * 10)

