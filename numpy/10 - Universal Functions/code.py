import numpy as np
import math

## code1
arr_1 = np.array([1, 2, 4, 4, 5])
arr_2 = np.arange(1,6)

arr = arr_1 + arr_2
print(arr)                 #[ 2  4  7  8 10]

arr = np.add(arr_1,arr_2)  
print(arr)                  #[ 2  4  7  8 10]


print(arr_1 * 2)            # [ 2  4  8  8 10]
print(arr_1 **  2)          # [ 1  4 16 16 25]

##code2 
arr = np.linspace( -2 * math.pi , 2 * math.pi , 10 )

print(np.sin(arr))
print(np.cos(arr))

## code3

##  开盘价， 最高价， 最低价， 收盘价

from time import perf_counter
import random

# num_rows = 10_000_000

# random.seed(0)

# start = perf_counter()

# data = [
#     [
#         random.randint(120, 180),
#         random.randint(180, 200),
#         random.randint(100, 120),
#         random.randint(120, 180)
#     ]
    
#     for _ in range(num_rows)
# ]

# end  = perf_counter()
# print(data[:2])
# print('Elasped: ' , end - start)

# # round((high - low) / close * 100)

# start = perf_counter()
# var = [
#     round((row[1] - row[2]) / row[3] * 100)
#     for row in data
# ]
# end = perf_counter()
# print(var[:5])
# print('Elapsed:', end - start)


## code4 
# 转为np.array
# start = perf_counter()
# data_np = np.array(data)
# end = perf_counter()
# print(data_np[:2])
# print('Elapsed:', end - start)


# start = perf_counter()
# var = np.round(((data_np[:, 1] - data_np[:, 2]) / data_np[:, 3]) * 100)
# end = perf_counter()
# print(var[:5])
# print('Elapsed:', end - start)

## code5 

import numpy as np
from time import perf_counter

np.random.seed(0)

num_rows = 10_000_000

start = perf_counter()
data_np = np.hstack(
    [
        np.random.randint(120, 180, (num_rows, 1)),
        np.random.randint(180, 200, (num_rows, 1)),
        np.random.randint(100, 120, (num_rows, 1)),
        np.random.randint(120, 180, (num_rows, 1)),
    ]
)

var = np.round(((data_np[:, 1] - data_np[:, 2]) / data_np[:, 3]) * 100)
end = perf_counter()
print('Elapsed:', end - start)


