l1 = [1, 2, 3]
l2 = l1[:]
print(l1,l2)
print(l1 is l2)

l2.append(10)
print(l2)

m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
print(m1)

m2 = m1.copy()
print(m2)

m2.append([10, 20, 30])
print(m1)
print(m2)

m2[0].append(-1)
print(m1)
print(m2)

from  copy import deepcopy
m1 = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]
m2 = deepcopy(m1)

print(m2)

print(m1[0] is m2[0])

#你是无法修改tuple的
a = 1, 2, 3
b = a[:]

print(b,type(b).__name__)