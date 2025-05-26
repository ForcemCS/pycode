#def func(a, b, *, c):
# a：位置参数（positional argument）
# b：位置参数
# *：这是重点，它的作用是强制后面的参数只能通过关键字（keyword）来传递
# c：关键字参数（keyword-only argument）


def greet(name, *, greeting="Hello"):
    print(f"{greeting}, {name}!")

greet("Alice", greeting="Hi")  # ✅ 正确
#greet("Alice", "Hi")          # ❌ 错误，greeting 不能通过位置传参

def func(a, b, *args, c, d, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("d:", d)
    print("kwargs:", kwargs)

func(1, 2, 3, 4, 5, c=6, d=7, e = 8,f = 'aa')

#a, b	位置参数，必须用位置传
#*args	可变位置参数，收集多余的位置参数，类型是 tuple
#c, d	关键字参数，只能用 c=value, d=value 的形式传
#**kwargs	可变关键字参数，收集多余的关键字参数，类型是 dict


def func(a, *, b , **keys):
    print("a:", a)
    print("b:", b)
    print("keys:", keys)

func(1,b=2, e='cc')   