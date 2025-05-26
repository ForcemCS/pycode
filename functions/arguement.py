def my_func1(*args):
    print(type(args).__name__)
    print(args)

my_func1(1, 2, [1, 2],'abc')
print('-' * 10 )


def my_func2(a, b, *args):
    print(a)
    print(b)
    print(args)

my_func2(1,2)
my_func2(1, 2, 3, 4, 5)
print("-" * 10)


def my_func3(a, b, *args, c):
    print(a)
    print(b)
    print(c)
    print(args)

my_func3(1,2,c=1)
print('-' * 10 )
my_func3(1, 2, 3, 4, c=5)   



sum([1, 2, 3])
sum((1, 2, 3))
sum({1, 2, 3})

def  average(*values):
    try:
        return sum(values) / len(values)
    except ZeroDivisionError as ex:
        return 0

print(average())


def average(*values):
    if len(values) == 0:
        return 0 
    return sum(values) / len(values)

print(average())

#a = (1,)
#print(type(a).__name__)


def prods(*values):
    prod = 1
    for v in values:
        prod *= v
    print(prod) 

prods([1, 2])     # 把一个列表作为一个整体传入,v得到的是整个list[1, 2],而不是单个数字
prods(*[1, 2])    # * 是解包运算符，意思是把列表 [1, 2] 拆成两个参数 1, 2