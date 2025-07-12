import numpy as  np

# code1 
arr = np.arange(12)
# [ 0  1  2  3  4  5  6  7  8  9 10 11]
print(arr)
# (12,)
print(arr.shape)

m1 = arr.reshape(4,3)
print(m1)

## 输出False
print(arr is m1)

arr[0] = 100
# [100   1   2   3   4   5   6   7   8   9  10  11]
print(arr)
# [[100   1   2]
#  [  3   4   5]
#  [  6   7   8]
#  [  9  10  11]]
# 改变原始数组arr,m1也会变化
print(m1)


# code2

# 改变m1，但是原数组arry没有变化
m1[0][0] = 0 
print(m1)
print(arr)

m2 = arr.copy().reshape(3,4)
print(m2)

m2[0][1] = 88
print(arr)

m3 = m2.reshape(12,)
print(m3)
m3[0] = 100
print(arr)