import numpy as np

## code1 
#创建了一个 NumPy 数组。你可以把它想象成一个特殊的高性能列表。
a = np.array([1, 2, 3])
print(type(a).__name__)      #ndarray,这是 NumPy 库定义的一种核心对象类型。

print(a.dtype)               #ndarray类型的数组 a 里的所有元素的类型


a = np.array([1, 2, 3], dtype = np.int8)


## code 2

l = [
    [1, 0, 0],
    [0, 1, 0]
]

#Axes (轴)
# axes 0 表示列的方向
# axes 1 表示行的方向
# axis 0 指的是“行”这个维度（上下方向），axis 1 指的是“列”这个维度（左右方向）

m = np.array(l,dtype=np.int8)
print(m.shape)
print(m.shape)            #(2,3) 元组的第一个元素是 axis 0 的大小，第二个是 axis 1 的大小。


c = np.array([1, 2, 3])
print(c.shape)              #一维数据，三个元素