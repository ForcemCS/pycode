import pandas as pd
import numpy as np

arr = np.arange(9).reshape(3,3)
# [[0 1 2]
#  [3 4 5]
#  [6 7 8]]

df = pd.DataFrame(
    arr,
    columns=['c1', 'c2', 'c3'],
    index=['r1', 'r2', 'r3']
)
#     c1  c2  c3
# r1   0   1   2
# r2   3   4   5
# r3   6   7   8

print(df.loc['r1'])  ##取出r1行

print(df['c1'])      ##取出c1列

print(df.values)     ##取出原始数组，也就是arr
print(type(df.values))   


print(df.values[0,1])   ##输出原始数组的0行1列

print(df.iloc[1, 2])    ## 使用隐式索引取出1行2列  
print(df.loc['r2', 'c3'])

print(df.loc['r1': 'r2', : ])

#     c1  c2  c3
# r1   0   1   2
# r2   3   4   5

print(df.iloc[0:1, 1:2])

#     c2
# r1   1


print(df.iloc[0:2, :])   ## 等价于print(df.iloc[0:2])
print(df.iloc[0:2])


print(df.loc[:, ['c1', 'c3']])