##测试1
from time import perf_counter
import time
def performance(func):
    def wrapper(*args, **kwargs):
        start  = perf_counter()
        result = func(*args,**kwargs)
        end  = perf_counter()
        print(f'func = {func.__name__} 的运行时间为{end - start:.8f} ')
        return result
    return wrapper

@performance
def add(x,y):
    time.sleep(0.01)
    return x + y

print(add(1,2))

##测试2
# if not isinstance(original_result, (int, float, Decimal)):
#     return original_result
# isinstance(value, (type1, type2, ...)) 是一个内建函数，用来判断 value 是否是指定类型中的任意一个。

#float(Decimal('2.718'))  #2.718

import functools
from decimal import Decimal

PRECISION  = 2

def normalize(fn):
    @functools.wraps(fn)
    def wrapper(*args,**kwargs):
        result = fn(*args,**kwargs)
        if not isinstance(result, (int,float,Decimal)):
            return result
        result = round(float(result), PRECISION)
        return result
    return wrapper

@normalize
def perc_diff(x, y):
    try:
        return (y-x) / x * 100
    except ZeroDivisionError:
        return 0
@normalize    
def sum_squares(*args):
    """用于求平方和"""
    return sum(x**2 for x in args)

@normalize
def avg(*args):
    if len(args) == 0:
        return 0
    
    numbers = [Decimal(x) for x in args]
    sum_ = sum(numbers)
    return sum_ / len(numbers)



print(f"初始精度: PRECISION = {PRECISION}")

result1 = perc_diff(10, 12)
print(f"perc_diff(10, 12): {result1}, type: {type(result1).__name__}")

result2  = sum_squares(2,3)
print(f"sum_squares(2,3): {result2}, type: {type(result2).__name__}, 文档字符串: {sum_squares.__doc__}")

result3 = avg(0.4,0.2)
print(f"avg(0.4,0.2): {result3}, type: {type(result3).__name__}")
print('*' * 20 )



##测试4

import functools
from decimal import Decimal

def normalize(precison):
    def decorators(fn):
        def inner(*args,**kwargs):
            result = fn(*args,**kwargs)
            if not isinstance(result, (int,float,Decimal)):
                return result
            result = round(float(result), precison)
            return result
        return inner
    return decorators
                    

@normalize(2)
def perc_diff(x, y):
    try:
        return (y-x) / y * 100
    except ZeroDivisionError:
        return 0
result1 = perc_diff(10, 12)
print(f"perc_diff(10, 12): {result1}, type: {type(result1).__name__}")

@normalize(3)
def perc_diff(x, y):
    try:
        return (y-x) / y * 100
    except ZeroDivisionError:
        return 0
result1 = perc_diff(10, 12)
print(f"perc_diff(10, 12): {result1}, type: {type(result1).__name__}")

#测试3
from functools import lru_cache

from timeit import timeit

def add1(x,y):
    time.sleep(0.01)
    return x + y
a = timeit('add1(2, 2)', globals=globals(), number=10)
print(a)

@lru_cache
def add2(x,y):
    time.sleep(0.01)
    return x + y
b = timeit('add2(2, 2)', globals=globals(), number=10)
print(b)

