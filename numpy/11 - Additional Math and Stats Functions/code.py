import numpy as np 

## code 1
a = np.amin(np.array([1, 3, 5]))
print(a)


m = np.array([[10, 2, 3], 
              [4, 50, 6], 
              [7, 8, 90]])
## axis = 0 表示row的方向 axis =1 表示column 的方向
print(np.amin(m, axis=0))


m = np.median(np.array([1, 2, 3, 4, 5, 6]))
print(m)


# decimals > 0 (正数):
# 这表示要保留的小数位数。这是最常见的用法。

# decimals = 0 (零):
# 这表示四舍五入到最接近的整数（个位）。

# decimals < 0 (负数):
# 这是最特殊的情况。负数表示要舍入到小数点左边的位置，也就是十位、百位、千位等。
a = np.around(np.array([123, 155]), decimals=-2)

print(a)


## code2 
np.random.seed(0)
arr = np.random.randint(1, 10, 20)


# [0, 2) [2, 4) [4, 5) [6, 8) [8, 9]
bins = np.array([0, 2, 4, 6, 8, 9])

h = np.histogram(arr, bins=bins)
print(h)