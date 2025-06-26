# 计算机内部使用二进制表示数字，这导致很多我们习以为常的十进制小数（如 0.1）无法被精确表示，只能存储一个非常接近的近似值。这就是为什么 0.1 + 0.2 不等于 0.3 的原因。而 Decimal 对象内部使用十进制算术，可以完全精确地表示这些小数。
# from decimal import Decimal,getcontext

# print(0.1 + 0.2)  # 输出: 0.30000000000000004
# print(Decimal('0.1') + Decimal('0.2')) # 输出: 0.3

# 为了保证在创建 Decimal 对象时精度不丢失，你必须使用字符串 ('0.1') 来初始化它。如果直接使用浮点数 (0.1)，那么这个浮点数本身的不精确性会先被代入，然后再被转换成 Decimal，这样就失去了意义。
# 写 Decimal('...') 显然比直接写数字要麻烦一些 (unwieldy)。

# Python 的math 模块中的函数（如 math.sqrt, math.sin 等）是为处理浮点数（float）而设计的。如果你试图将一个 Decimal 对象传入这些函数，它会先被默默地转换成一个不精确的浮点数，然后再进行计算，这使得 Decimal 的精确性荡然无存。

# import math
# d = Decimal('2')

# # math.sqrt() 会把 Decimal 转成 float，失去精确性
# result_float = math.sqrt(d) 
# print(type(result_float)) # 输出: <class 'float'>
# print(result_float)       # 输出: 1.4142135623730951

# 为了解决上一个问题，Decimal 对象自身就定义了很多数学方法。你需要使用 decimal_object.sqrt() 而不是 math.sqrt(decimal_object)。这些内置函数是专门为 Decimal 设计的，能够保持计算的精确性。

# # 设置精度
# getcontext().prec = 50 

# d = Decimal(2)
# # 使用 Decimal 对象自带的 sqrt() 方法
# result_decimal = d.sqrt()
# print(type(result_decimal)) # 输出: <class 'decimal.Decimal'>
# print(result_decimal)       # 输出一个50位精度的结果:  1.4142135623730950488016887242096980785696718753769


# 总结：float 的运算直接由硬件（CPU的浮点运算单元FPU）支持，速度极快。而 Decimal 的运算是在软件层面通过算法模拟十进制算术实现的，这个过程比硬件计算要慢得多。
# 适用场景: 在需要极高计算速度的科学计算、数据分析等领域，通常会优先选择 float。Decimal 更适用于对精度要求高于一切的场景，如金融、会计。
# 一个标准的 float 对象通常占用固定的内存（如64位/8字节）。而 Decimal 对象为了存储任意精度的数字，需要更多的内存空间来记录每一位数字以及其他信息（如符号、小数点位置等）。精度越高，占用的内存就越多。

from decimal import Decimal, getcontext, ROUND_HALF_EVEN

# 1. 设置算术上下文
getcontext().prec = 5                  # 设置精度为 5
getcontext().rounding = ROUND_HALF_EVEN  # 设置舍入方法为银行家舍入法

# 2. 定义 Decimal 对象
d1 = Decimal('1.2325')
d2 = Decimal('122')

# 3. 执行乘法运算
result = d1 * d2

# 4. 查看结果
print(result)
print(Decimal.getc)