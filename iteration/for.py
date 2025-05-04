#迭代序列
#join 连接sequence(list tuple str rang())
for x in ['a b', 'b']:
    y = x + x
    z = '=='.join(x)
    print(z)
    print(type(x).__name__, x)
print("Done")


for i in  range(1, 4):
    for  j  in range(1, i + 1):
        print (f"{i} * {j} = ", i * j )
    print('')
print("----------Done")    


#修改元list的值
data = [10, -20, 30, -1, -2]

for idx in range(len(data)):
    if data[idx] < 0:
        data[idx] = 0
print(data)
print("Done-----------")

#返回索引和元素构成的元组
data = [10, -20, 30, -1, -2]

for t in enumerate(data):
    print(t)
print("----------")


data = [10, -20, 30, -1, -2]

for j in enumerate(data):
    index, element = j
    if element < 0:
        data[index] = 0 
print(data)

##更好的表达方式如下

for  index, element in enumerate(data):
    if element < 0 :
        data[index] = 0 
print(data)
