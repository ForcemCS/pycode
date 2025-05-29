# def my_map(func, iterable):
#     result = [func(element) for element in iterable]
#     return result
# 这段代码是自定义实现的一个简单版的 map()：
# 1. func 是你传入的函数；
# 2. iterable 是一个可迭代对象，比如列表；
# 3.使用了列表推导式 [func(element) for element in iterable]，表示把 func 应用到 iterable 的每个元素上，生成一个新列表 result；
# 4.最后返回这个列表。（但是有一个问题，iterable是一个很大的数据，一次生成的新list，会占用很大的内存）

#map() 函数会将一个 指定的函数 应用于一个 可迭代对象（如列表）中的 每一个元素，返回一个 映射后的结果（是一个迭代器）。
# map() 返回的不是一个列表，而是一个 惰性迭代器（lazy iterator），它不会立即计算所有结果，而是 在需要的时候才计算每一个值，更节省内存。
# result = map(func, iterable)
# for val in result:
#     print(val)


##code1 
data = ['a', 'ab', 'abc', 'abcd']

def my_lens(x):
    return len(x)

a = ( my_lens(ele) for ele in data )

print(list(a))

##map等效写法

a = map(len, data)
print(list(a))
print(list(a))