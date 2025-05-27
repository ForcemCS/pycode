#lambda 函数是一个 匿名函数（anonymous function），它本身没有名字。要使用它，你需要把它赋值给一个变量，然后像调用普通函数一样来调用这个变量。
#lambda 函数只能包含一个表达式。这个表达式的结果就是函数的返回值，你不能在 lambda 体内写多行语句（比如 if/else 结构、for 循环等），也没有 return 关键字。
#是一个迭代器对象（iterator）。

add_function = lambda x, y: x + y
result = add_function(5, 3)
print(result) # 输出: 8

#你也可以不赋值给变量，直接在定义后调用（这种用法相对少见，主要用于一些特殊的、一次性的场景）：
# 直接定义并调用
result = (lambda x, y: x + y)(5, 3)
print(result) # 输出: 8

##code1
#map() 是 Python 中的一个内置函数，用于将指定函数作用于可迭代对象（如列表、元组）中的每个元素，并返回一个迭代器（map 对象）。你可以通过 list() 将其结果转换为列表查看。
#它不会立刻对数据进行处理，而是等你遍历它的时候（比如用 list()、for 循环）才开始执行函数逻辑。
#节省内存，适用于处理大量数据。
def double(x):
    print(f"计算 {x} * 2")
    return x * 2

nums = [1, 2, 3]

#通过map将指定的函数，作用于可迭代的对象，返回的是一个可迭代器对象
result = map(double, nums)  # 此时并不会调用 double

for val in result:          # 在迭代时才会执行 double
    print(val)


##code2
nums = [1, 2, 3]
result = map(lambda x: x * 10, nums)

print(next(result))  # 输出: 10
print(next(result))  # 输出: 20
print(next(result))  # 输出: 30
#print(next(result))  # 抛出 StopIteration 异常（没有元素了）

##code3
nums = [1, 2, 3, 4, 5]
result = map(lambda x: x * x, nums)
print(list(result))  # 输出: [1, 4, 9, 16, 25]

##code4
students = [
    {"name": "Alice", "score": 88},
    {"name": "Bob", "score": 75},
    {"name": "Charlie", "score": 93}
]

# 按成绩从高到低排序
#sorted Python 的内置排序函数，不会修改原列表，而是返回一个新列表
#sorted(iterable, key=function) 可以根据自定义的规则（通过 key 指定的函数）来排序。
sorted_students = sorted(students, key=lambda s: s["score"], reverse=True)

for student in sorted_students:
    print(student["name"], student["score"])


#code5
#filter(function, iterable) 根据函数返回的布尔值过滤序列的元素。

num = [1, 2, 3, 4, 5, 6]
event_num = list(filter(lambda num: num % 2 ==0 , num))

print(event_num)