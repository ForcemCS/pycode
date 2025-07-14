import numpy  as np

## code1
a1 = np.arange(1,6)
print(a1)     # [1, 2, 3, 4, 5]

a2 = np.arange(1, 11).reshape(2, 5)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
print(a2)

s1 = np.vstack((a1, a2))
# [[ 1  2  3  4  5]
#  [ 1  2  3  4  5]
#  [ 6  7  8  9 10]]
print(s1)

## code2 

a1 = np.array([1, 2, 3])
a2 = np.array([0.1, 0.2, 0.3])

result = np.stack((a1, a2))
print(result)
print(result.dtype)          # float64


## code3

a1 = np.array([1, 2, 3, 4],dtype = np.uint8)
a2 = np.array([1, 2, 3, 4],dtype = np.uint16)

print(np.stack((a1,a2)).dtype)

## code4 

a  = np.vstack(
    (
        np.arange(5),
        np.linspace(0, 1, 5),
        np.eye(5)
    )
)
print(a)
print(a.dtype)

a1 = np.array([1, 2, 3, 4],dtype = np.uint8)

##类型转换
a3 = a1.astype(np.int64)
print(a3.dtype)

## code5 

a1 = np.linspace(0, 5, 10).reshape(5,2)
np.random.seed(0)
a2 = np.random.randint(0, 10, 10).reshape(5, 2)


result = np.hstack((a1,a2))
print(result)