# 我们可以像使用普通numpy数组一样使用pandas index 
import pandas as pd
import numpy as np

## code 1
idx = pd.Index(['London', 'Paris', 'New York', 'Tokyo'])

a = idx != 'Tokyo'  # [ True  True  True False]

print(idx[a])       # Index(['London', 'Paris', 'New York'], dtype='object')


## code2 

idx_1 = pd.Index(['a', 'b', 'c'])
idx_2 = pd.Index(['c', 'd', 'e'])

a = idx_1.intersection(idx_2)

print(a)

## code3

a = pd.Index(range(2,10,2))

print(a)          # RangeIndex(start=4, stop=8, step=2)
print(list(a))    # [2, 4, 6, 8]
print(a.to_numpy())  #[2 4 6 8]


## code4 

idx_1 = pd.Index(['a', 'b', 'c'])

print(idx_1[[ 1,True, False] ])