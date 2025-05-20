#就像数学中集合的概念一样，
#是可迭代的，不保证迭代的顺序
#集合元素必须是可哈希的
#集合是不可变的和不可哈希的
#一个集合不能是两一个集合的元素，你真的想要嵌套集合，使用 frozenset
# 定义set  {1, 'a', True}  set([1, 'a', True])
# set()空集合
l = [1, 2, 3, 4, 5]
s = set(l)  # {1, 2, 3, 4, 5}

l = [1, 1, 2, 2, 3, 3, 4, 4, 5, 5]
s = set(l)  # {1, 2, 3, 4, 5}

s = set('python')  # {'h', 'p', 'n', 'o', 't', 'y'}
print(s)

# for循环进行迭代
# in 测试元素的存在性
# s.copy() 创建一个浅拷贝


print('x' not in  s)
for item in s:
    print(item)

from copy import deepcopy

s2  = deepcopy(s)
print(s2)


s = {10, 'b', True}
s.add(4)
print(s)

s.remove(True)
print(s)

#s.remove('x')   元素不存在会报错，可以使用discard

s.discard('x')

###子集和超子集

###并集（|）和交集（&）
#  s1 -s2的意义是 取出s1中与s2中不同的元素

