import numpy as np

a1 = np.array([1, 2, 3, 4])
a2 = np.array((0.1, 0.2, 0.3, 0.4))

print(a1)

a3 = np.array([1, 2, 3.14, 9.9], dtype=np.uint8)
print(a3)


a4 = np.array([1, 2, 3.14, 'x'])
print(a4,a4.dtype)

m2 = np.array(
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9],
        [10, 11, 12]
    ]
)

print(m2.size)