## 普通的切片独立于原始的list,而numpy slice与原始数组是有联系的
import numpy as np

## code1 

l = [1, 2, 3, 4, 5]
l[0:3] = [10, 20, 30]
print(l)

l = [1, 2, 3, 4, 5]

l[0:2] = [10, 20, 30,40 ,50]
print(l)


arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8])

a1 = arr[0:3]             #[0 1 2]
a2 = arr[2:6:2]           #[2 4] 
a3 = arr[1::2]            #[1 3 5 7]
a4 = arr[::-2]            #8 6 4 2 0]

## code 2

arr = np.arange(1,7)
slice_ = arr[3:]
print(slice_)   # [4, 5, 6]

arr[-1] = 60

print(slice_)  # [4, 5, 60]  原始数组改变对切片也有影响



## code 3

arr = np.arange(1,7)
slice_ = arr[3:].copy()
print(slice_)         # [4 5 6]

arr[-1] = 600
print(slice_)         # [4 5 6]


## code 4 
arr = np.arange(1,26).reshape(5,5)

a = arr[0:2, 0:2]
print(a)

b = arr[::2, ::2]
print(b)

c = arr[2, 1::2]
print(c)


## code5
##数据类型和空间是不可变的
arr = np.array([1, 2, 3, 4, 5, 6])
arr[0:3] = np.array([10, 20, 30])

arr = np.arange(9).reshape(3, 3)
arr[::2, ::2]  = [[10, 20], [50, 60]]

print(arr)


arr = np.arange(9).reshape(3, 3)
## 广播到特定的形状中
arr[::2, ::2]  = 100
print(arr)


## code6

arr1 = np.array([1, 2, 3, 4, 5, 6])
arr2 = np.array([10, 20])
arr1[:2] = arr2

print(arr1)          # [10 20  3  4  5  6]
#若此时我修改第arr2,不影响arr1

