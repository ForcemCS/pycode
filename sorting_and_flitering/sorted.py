# sorted() 函数用于对任何可迭代对象进行排序，并返回一个新的已排序的列表。它有几个重要参数：
#   iterable (必需)： 你想排序的对象，比如列表、元组、集合、字典的键、字符串等等。
#   key (可选)： 最核心的部分，它是一个函数。这个函数会在每次比较元素时被调用，sorted() 函数会用这个函数的返回值来做实际的比较。但最终排序的列表里包含的仍然是原始的元素。
#   reverse (可选)： 一个布尔值，如果为 True，则进行降序排序；默认为 False（升序）。


# data = {'a': 300, 'b': 100, 'c': 200}

# #1.排序对象是data.keys()，也就是说拿到可迭代对象后，这个值会传递到K
# #2.根据key的返回值，对dict_keys进行排序
# sorted(data.keys(), key=lambda k: data[k])


##code1

data = [10, -6, 0, 3, 6]

def key_func(x):
    return abs(x)

result = sorted(data,key=key_func)
print(list(result))