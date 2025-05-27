#主要用于“打包多个可迭代对象”，能一对一地配对组合它们的元素。
#zip(iterable1, iterable2, ...)
#  1.将多个可迭代对象“并排配对”
#  2. 返回一个迭代器，每一项是个tuple

l = [1, 2, 3]
t = (10, 20, 30)

a= list(zip(l,t))
print(a)

##code1
##创建字典的不同方式
#  1. d = {'a': 1, 'b': 2, 'c': 3}
#  2. dict([('a', 1), ('b', 2), ('c', 3)])  # 使用tuple组成的list

d = dict([('a', 1), ('b', 2), ('c', 3)])

print(d)


##code2
data = [
    ('item1', 10, 100.0),
    ('item2', 5, 25.0),
    ('item3', 100, 0.25)
]

schema = ['widget', 'num_sold', 'unit_price']

print(schema[1:])

for rows in data:
    print(list(zip(rows, schema)))

print('-' * 10)

##code3


data = [
    ('item1', 10, 100.0),
    ('item2', 5, 25.0),
    ('item3', 100, 0.25)
]


schema = ['widget', 'num_sold', 'unit_price']

d = {}

for rows in data:
    widget_name = rows[0]
    sub_dict = dict(zip(schema[1:],rows[1:]))
    d[widget_name] = sub_dict
print(d)


##code4
d = {rows[0]: dict(zip(schema[1:], rows[1:])) for rows in data}

from pprint import pprint
pprint(d)