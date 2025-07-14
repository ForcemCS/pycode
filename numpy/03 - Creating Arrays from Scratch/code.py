import numpy as np 

## code1 
a = np.zeros(5)
print(a)
print(a.dtype)

a =np.zeros(5, dtype=np.int32)
print(a)


# 创建一个多为数组
a = np.zeros((4,3), dtype=np.uint8)
print(a)

## code2 
a = np.ones((10,2), dtype=np.uint8)
print(a)
print('--' * 10)

## code 3

a = np.full((2,3), 1.23, dtype=np.float64)
print(a)

## code4
## 单位阵
a = np.eye(5, dtype=np.int64)
print(a)

a = np.eye(5,3, dtype=np.uint32)
print(a)

## code5 
b = list(range(2,11,2))

print(b)

a = np.arange(2,11,2 , dtype=np.uint8)
print(a)

##  code6
# [2,10] 均匀的取出5个数字
a = np.linspace(2,10, num= 5)
print(a)

a = np.linspace(2,10, num = 10)
print(a)


## code 7

import math

x_coords = np.linspace(- 1 * math.pi, 1 * math.pi, num=50)
print(x_coords)

y_coords = np.array([math.sin(x) for x in  x_coords])

print(y_coords)

## code 8

# 生成包含五个随机数的数组
a = np.random.random(5)
print(a)

np.random.seed(0)
print(np.random.random(5))
np.random.seed(0)
print(np.random.random(5))

np.random.seed(0)
print(np.random.random((3,2)))
np.random.seed(0)
print(np.random.random((3,2)))


## code9
np.random.seed(0)
# [1, 20)之间生成20个随机数
print(np.random.randint(1,10 ,20))


## code 10

from numpy import random as npr

npr.seed(0)
# 生成 10 x 2 的矩阵
npr.randint(1, 7, (10, 2))


