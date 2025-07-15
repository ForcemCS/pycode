import numpy as np

## !!索引数组决定的是结果的维度
## code1 原始数组是一维的示例
arr = np.array([10, 11, 12, 13, 14, 15, 16])
index_arr1 = np.array([0, 1, 2, 4])     ## 此时索引数组的shape为（4,) 一维的

print(arr[index_arr1])


index_arr2 = np.array([[0, 1],  [2, 4]]) 

# [[10 11]
#  [12 14]]
print(arr[index_arr2])


## code2 

arr = np.arange(10, 100, 10)
print(arr)

arr = np.array([10, 20, 30, 40, 50, 60, 70, 80, 90])

l = [arr[0], arr[2], arr[3]]
print(l)               # [np.int64(10), np.int64(30), np.int64(40)]

#方式1：取出其中的原始，作为一个新的np.array
sub  = np.array([arr[0], arr[2], arr[3]])
print(sub)             # [10 30 40]

#方式2
sub = arr[np.array([0, 2, 3])]
print(sub)             #[10 30 40]

#方式3
sub = arr[[0, 2, 3]]  # 不要误写为arr[0, 2, 3]  这是求三维数组的内容
print(sub)            #[10 30 40]


##  code3 

arr = np.arange(1, 10)
sub = arr[np.array([0, 1, 1, 5])]
print(sub)                  # [1 2 2 6]


##接下来重塑为一个二维的数组
sub = arr[np.array([
    [0, 1],
    [1, 5]
])]

# [[1 2]
#  [2 6]]
print(sub)


## code4 
# m = np.arange(25).reshape(5, 5)
m = np.array([[0, 1, 2, 3, 4],
       [5, 6, 7, 8, 9],
       [10, 11, 12, 13, 14],
       [15, 16, 17, 18, 19],
       [20, 21, 22, 23, 24]])


sub = m[[0, 1, 3]]
print(sub)

sub_1 = m[[0, 1, 3], 2]
print(sub_1)             #  [ 2  7 17]

sub_2 = m[[0, 1, 3], 0::2]
# [[ 0  2  4]
#  [ 5  7  9]
#  [15 17 19]]
print(sub_2)


sub_3 = m[np.array([0, 1, 3]), np.array([1, 3, 4])]            #(0, 1) (1, 3) (3, 4)
# [ 1  8 19]
print(sub_3)


## code 5
import csv

from dateutil import parser

with open('AAPL.csv') as f:
    reader = csv.reader(f, skipinitialspace=True)
    header = next(reader)
    
    data = list(reader)

data = np.array(data)

dates = data[:, 1 ]

dates =  [parser.parse(d) for d in dates]

oc = data[:, [4, 2]].astype(float)
print(oc)
print(oc.shape)


diffs = oc[:, 1]  - oc[:, 0]
print(diffs)

diffs_percs = diffs / oc[:, 0 ] * 100
print(diffs_percs)