# (function) def gcd(*integers: SupportsIndex) -> int
# Greatest Common Divisor.
#   *integers	表示可以传入 多个整数参数（这是一个可变参数，类似于 gcd(12, 8, 16)）
#   : SupportsIndex	参数类型提示：这些参数都要支持被转为整数（比如 int）
#   -> int	函数的返回值类型是 int 整数类型


# math 是用 C 编写的，作为 Python 的一部分编译进了解释器。所以它不像普通 .py 文件那样被“读取和解释”

# 一旦找到了 math 模块，Python 会：
# 1.在内存中创建一个模块对象（类型是 module）；
# 2.把模块中的函数、变量、常量等装进这个模块对象；
# 3.将这个模块对象绑定到你的变量 math 上。
# 4.也就是说，math 本质上是一个指向模块对象的变量：
#   import math
#   print(type(math))  # <class 'module'>

import os.path  as cc

print(cc.curdir)
print(cc.abspath(cc.curdir))

import fractions

f1  = fractions.Fraction(1,6)
#计算机中的浮点数是一个有理数
f2  = fractions.Fraction(0.1)
print(f2)
