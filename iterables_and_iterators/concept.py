#iterable(可迭代对象)和iterator(迭代器，对iterable的跟踪)
#迭代器是一个实现了 __iter__() 和 __next__() 方法的对象
my_list = [1, 2, 3]
print(hasattr(my_list, '__iter__'))  # 判断list 是否有__iter__方法

my_list = [1, 2, 3]
my_iter = iter(my_list)  # 得到一个迭代器

print(next(my_iter))  # 输出 1
print(next(my_iter))  # 输出 2
print(next(my_iter))  # 输出 3
print('-' * 10)
# print(next(my_iter))  # 会抛出 StopIteration 异常


l = [1, 2, 3, 4, 5]

iterator = iter(l)
try:
    while True:
        # return next(iterator) - here we'll just print it
        print(next(iterator))
except StopIteration:
    # expected when we reach the end
    # so silence this exception
    pass

l = [1, 2, 3]
l_iterator = iter(l)               #得到了一个list iterator
print(type(l_iterator).__name__)

print(next(l_iterator),next(l_iterator),next(l_iterator)) 


#print(next(l_iterator))   需要再次常见迭代器才能正确执行，不会抛出异常

print(id(l_iterator))

iterator = iter(l_iterator)
print(id(l_iterator))


l = [1, 2, 3]

#它正在使用迭代器
for ele in l:
    print(ele)
print('-' * 10)
#接下来我们模拟for循环
iterator = iter(l)

try:
    while True:
        print(next(iterator))
except StopIteration:
    pass
print('-' * 10)

l = range(10)   #也是一个惰性迭代，但是不是iterator,所以可以多次迭代范围对象
print(l)

r_iter = iter(l)
print(next(r_iter),next(r_iter))     #已经迭代了两次
print(list(r_iter))

#-------------------------------
#range_obj = range(100_000_000)  # 内存很小
#list_obj = list(range(100_000_000))  # 内存巨大，可能会卡死
#del list_obj

#它不仅是 iterable（可迭代对象），而且是 iterator（迭代器），因为它实现了 __next__() 方法。
a = enumerate('abc')
print(next(a))
print(next(a))
print(next(a))
print(hasattr(a, '__iter__'))  # True，说明是可迭代的
print(hasattr(a, '__next__'))  # True，说明是迭代器
#print(next(a))
