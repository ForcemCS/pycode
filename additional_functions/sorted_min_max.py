##code1
l = [1, 10, 2, 9, 3, 8]
t = (1, 10, 2, 9, 3, 8)
d = {1, 10, 2, 9, 3, 8}

print(sorted(t))
print(sorted(d))

a = sorted(t, reverse=True)


##code2

print(ord('a'),ord('A'))

print(ord('a') > ord('A'))  #true,根据unicode代码点进行判断

print(sorted(('a', 'b', 'c', 'd' )))
print(sorted('cdfsfdsa'))

##code3
a = sorted(['Zebra', 'apple', 'atom'],key=str.lower)  #这是 str 类型的一个方法引用

print(a)

words = ['apple', 'cat', 'banana', 'dog']
print(sorted(words, key=len))


pairs = [('a', 3), ('b', 1), ('c', 2)]

print(sorted(pairs, key=lambda x : x[1], reverse=False))

##code4

students = [
    {'name': 'Tom', 'score': 90},
    {'name': 'Jerry', 'score': 90},
    {'name': 'Spike', 'score': 85}
]

# 优先按 score，其次按 name
print(sorted(students, key=lambda x: (x['score'], x['name']),reverse=True))

##code5

print(min([], default=0))
