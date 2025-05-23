a = (ele ** 2 for ele in range(5))   #创建了一个generator object,是一个迭代器对象，有next方法
print(type(a).__name__)   


##使用案例是读取一个文中中的一行，存放在另一个文件中，然后再读取下一行

data = [0, 1, 2, 3 , 4]
squares = ( i ** 2 for i in data)

print(3 in squares)
##特别注意，上一步已经把元素迭代完了
print(list(squares))

from timeit import timeit
#把这个字符串里的 Python 表达式执行 1 次，然后返回它执行的时间（单位：秒）
print(timeit("[i ** 2 for i in  range(25_000_000)]", number = 1)) 

print(timeit("(i ** 2 for i in  range(25_000_000))", number = 1)) 