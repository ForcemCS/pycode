#函数也是py中的对象
#callable 是一个用来描述“可被调用”的对象的术语。简单来说，只要一个对象能像函数一样被“调用”（用 () 执行），它就是 callable 的。

def foo():
    print("hello")

print(callable(foo))  # True，函数是 callable 的
print(callable(42))   # False，整数不是 callable 的

# def function_name():
#     #indented block
#     ....
#     return <value>

def say_hello():
    print("hello")

say_hello()

#如果没有指定返回值，函数将返回None
#return 看成是“把结果放在盒子里”，但你还得自己“打开盒子”（用 print()）才能看到里面装了什么

def one():
    return 1

print(one())


#从 datetime 模块中导入 datetime 类
#Python 有一个内建模块叫 datetime，专门处理“日期和时间”。它里面有一个同名的类也叫 datetime。
from datetime import datetime, timezone

def current_time_utc():
    return datetime.now(timezone.utc).isoformat()

print(current_time_utc())



#每次函数被调用时，它会创建一个新的“局部namespace”，与其他调用互不干扰。
# 1.当你调用一个函数，比如 my_function(5)，Python 就会准备执行这段代码。
# 2.函数是“健忘的”。它不知道你之前怎么调用过它，也不记得以前的变量值。
# 3.每调用一次函数，Python 都会：
#   1)创建一个空的字典（这是函数的“局部namespace”）
#   2)把你传入的参数填进去（键=参数名，值=你传的值）
#   3)然后执行函数里的代码
# 4.这个存放变量名和值的字典就叫做“局部namespace”。


def greet(name):
    print("Hello", name)

greet("Alice")
#调用 greet("Alice") 时：Python 会创建一个局部namespace：{'name': 'Alice'}


def abs_max(a, b):
    abs_a = abs(a)
    abs_b = abs(b)
    if abs_a > abs_b:
        max_val = abs_a
    else:
        max_val = abs_b
    return max_val

print(abs_max(1, -2))


