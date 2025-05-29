# a = 1 
# #这表示变量 a 所引用的对象 1 在内存中的位置。
# #在 Python 中，整数 1 是一个 不可变对象，并且是 小整数常量，通常在程序运行时是预先创建好的，所以多个变量赋值为 1 时，其 id() 是一样的
# print(hex(id(a)))

##code1
def outer(a, b):
    sum_= a +b 

    def inner():
        prod = a * b
        print(a, b, sum_, prod)
        return "You just called a consuer"
    return inner

inner1 = outer(1, 2)   #创建第一个闭包
print(inner1)
print(inner1())
print(inner1())
print(inner1.__closure__)


# def my_func(*args1, **args):
# *args1：表示接收任意数量的位置参数，这些参数会被打包成一个元组 args1；
# **args：表示接收任意数量的关键字参数，这些参数会被打包成一个字典 args；

# def my_func(*args1, **args):
#     print("位置参数 args1:", args1)
#     print("关键字参数 args:", args)

# my_func(1, 2, 3, name="Alice", age=25)

##code2

## *用于解包 (unpack) 一个可迭代对象（如列表、元组、集合）
## **用于解包 (unpack) 一个字典的键值对，并将它们作为单独的关键字参数传递给函数。
def execute(func):
    def inner(*args, **kwargs):
        print(args,kwargs)
        result = func(*args, **kwargs)
        return result
    return inner

def add(a, b, c):
    print('add...')
    return a + b + c

def say_hello(name, *, formal=True):
    print('say_hello...')
    if formal:
        return f'Pleased to meet you, {name}'
    else:
        return f'Hi, {name}!'

exec_add = execute(add)

exec_greet = execute(say_hello)

print(exec_add(1, 2, c=3))
print(exec_greet('Wu Kui', formal =True ))

##code3
from pprint import pprint
from time import perf_counter
def factorial(n):
    prod = 1 
    for i in range(2,n + 1 ):
        prod = prod * i
    return prod

def diagonal_matrix(rows, cols, *, diagonal =1 ):
    return[
        [
            diagonal  if row  == col else 0  for col in range(cols)
        ]
        for row in range(rows)
    ]

pprint(diagonal_matrix(3,3))

##code4

start = perf_counter()
result  = factorial(10)
end  = perf_counter()

print(f"elasped: {end - start:.10f}")
print(f"result = {result}")

##现在我们想通过一个func来实现计算不同函数的perf_counter

def time_it(func, *args, **kwargs):
    start = perf_counter()
    result = func(*args, **kwargs)
    end = perf_counter()
    print(f"elasped: {end - start:.10f}")
    return result
print(time_it(factorial,10))
pprint(time_it(diagonal_matrix,10,10, diagonal = -1))      #可读性其实没那么高，可以使用closure


def time_it(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        print(f"elasped: {end - start:.10f}")
        return result
    return inner
#第一个closure
f = time_it(factorial)
print(f(4))

#第二个闭包
d = time_it(diagonal_matrix)
pprint(d(10,10))


