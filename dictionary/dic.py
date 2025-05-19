#d.clear()删除所有的元素
#d.copy()浅拷贝，键和值的引用与原始对象的相同

#dict.get() 是字典对象的一个方法，用来安全地获取键对应的值，即使这个键不存在也不会报错。
#   dict.get(key) —— 只传一个参数（键）
#   dict.get(key, default_value) —— 传两个参数（键 + 默认值）


person_dict = {'ssn1' : 10}

if 'ssn' in person_dict:
    social = person_dict['ssn']
else:
    social = ''
    print(f"'{social}'")
social = person_dict.get('ssn', '')
print(repr(social))
print('-' * 10)

data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110
}
print('open' in data)     #执行的是扫描，但是速度是非常快的
print('x' not in data)
l = [1, 2, 3, 4]
print(1 in l)
print('-' * 10)

data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110
}
data.clear()
print(data)

print(len(data))
print('-' * 10)

data = {
    'open': 100,
    'high': 110,
    'low': 95,
    'close': 110
}

data_copy = data.copy()     #执行的是浅拷贝,会影响原来的值
print(data,data_copy,sep='\n')
print(data is data_copy)
data_copy['x'] = 100
print(data_copy)

from copy  import deepcopy

data_copy = deepcopy(data)    #执行的是深拷贝
print(data_copy is data)
print('-' * 10)

d = {
    'a': [1, 2, 3],
    'b': {
        'x': 0,
        'y': 0
    }
}

d_copy = d.copy()
print(d_copy is d)

d['a'].append(4)
print(d)
print(d_copy)
print('-' * 10)


d = dict.fromkeys(['open', 'high', 'low', 'close'],0)
print(type(d).__name__,d,sep='\n')
print('-' * 10)

d = dict.fromkeys(['a', 'a'],10)     #不重复的key
print(d)

symbols = ['APPLE', 'MSFT', 'APPLE', 'MSFT']
d = dict.fromkeys(symbols,0)
print(d)

a = list(d)
print(a)              #将有重复的列表元素去重