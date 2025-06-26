import decimal
from  decimal import Decimal

#code1
# print(decimal.getcontext())

# ctx = decimal.getcontext()

# ctx.prec = 5

# print(ctx)

# ctx.rounding = decimal.ROUND_UP

# print(ctx)

#code2

decimal.getcontext().prec = 6
decimal.getcontext().rounding = decimal.ROUND_UP

#尽管全局精度 prec 设置为 6，但通过字符串创建的 Decimal 对象 d1 将会保留其字符串中指定的完整精度（即 10 位有效数字），而不是被立即截断为 6 位。 
# prec 的影响将在 d1 参与算术运算或显式调用舍入方法（如 quantize() 或 round()）时体现。
d1 = Decimal('123.4567890')

#默认情况下会调用 d1 对象的 __str__ 方法，通常会输出其数值的字符串表示。
print(d1)
print(type(d1).__name__)
#repr() 的目标是生成一个字符串，该字符串在可能的情况下，能够通过 eval() 函数重新创建出原始对象
print(repr(d1))

print(d1 + Decimal('1'))


#Python 的内置 round() 函数，当其第一个参数是 Decimal 类型时，它会尊重当前 decimal 全局上下文 (context) 中的舍入模式。
print(round(Decimal('100.445'),2))