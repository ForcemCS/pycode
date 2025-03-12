# 不区分大小写的比较
s1 = 'hello'
s2  = 'HeLLo'
print(s1.casefold() == s2.casefold())  #true

print("----", s1.casefold())
print('aBC'.lower() == 'ABC'.lower())  #true

#剥离字符串
s = "  hello   "

print(repr(s.strip()))  # 输出hello
print(repr(s.lstrip())) # 输出'hello   '

name = '\t wu \t kui\t'
print("----",repr(name.strip()))

s = "ahello  11c"
# 指定要剥离的字符
print(s.strip('ac'))

""""
username = input("请输入用户名: ").strip()
print("你输入的用户名是：", repr(username))
"""

#字符串的拼接
s1 = 'hello'
s2 = 'world'

result = s1 + ' ' + s2
print(repr(result))

#split 分割字符串,并返回一个列表

data = "100, 200, 300, 400"
print(type(data.split(',')).__name__,":", data.split(','))

l = ('a', 'b')
print(type(l).__name__)

name = 'WU,KUI'
first_name, last_name  = name.split(',')

print(first_name, last_name)

#解包是不关心tuple 还是list，是可迭代的就可以
a, b = ['aa', 'bb']
print(a,b)

a, b = ('aa', 'bb')
print(a,b)

"""
字符串转为tuple
l = tuple('a')
print(type(l).__name__)
"""

#使用join方法来连接字符串,使用join连接可迭代对象
#join 的核心作用对象是分隔符 (Separator): join 方法的本质是用“某个字符串”作为分隔符，去连接一个可迭代对象（如列表、元组）中的字符串元素。从语义上讲，发起连接动作的是分隔符，而不是被连接的元素集合。
#此处体现了设计的巧妙之处
data = ('ab', 'cd', 'ef')
print('--【】'.join(data))

data1 = '='.join('python')    #字符串也是sequence
print(data1)  

print(','.join('ABCD'))

#查找字符串，比索引查找快
print('yo' in 'python')   #false
print('Py' in 'Python')   #True

print("测试in的使用")
print('wukui'.casefold() in 'WuKui'.casefold())

print(1 in [1, 2, 3])
print(1 in (1, 2, 3))
print()

#startswith() 和 endswith()，它们用于检查字符串的开头或结尾是否包含特定的子字符串。
print("startswith的使用")
print('python'.startswith('py'))  #true
print('python'.endswith('onc'))   #false
print()

#元素在sequence中的位置，使用字符串的index() 方法  我们可以使用find代替
data = 'hello world'
print(data.index('w'))   #6
print(data.find('w'))    #6
print(data.find('c'))    #-1
print(data[0:1])

print([1, 2, 3].index(1))

"""
#打印字符串的所有方法
print(dir(str))
#index方法的用法
help(str.index)
"""

message = "To ac is act" 
##查找第二次出现ac的索引位置
print(message.index('ac', 3 + len('ac')))  