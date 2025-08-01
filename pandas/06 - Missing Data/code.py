import pandas as pd
import numpy as np
import math

## code1 
print(float('NaN'),float('nan'))
print(math.nan, np.nan)

a = float('NaN')
print(math.isnan(a))   # True

## code 2 

a = np.array([1, 2, np.nan, 3, math.nan])
print(np.isnan(a))                           #[False False  True False  True]

s = pd.Series([3.14, 2.5, None, 5])
print(s)


print(math.isnan(float('nan')))


## code 3

s = pd.Series(['aaa', 'bbb', None, 'ddd', np.nan], index=list('abcde'))
print(s)
print(pd.isnull(s))  # [False, False, True, False, True]
print(s[pd.isnull(s)])
print(s[~pd.isnull(s)])

## 取出有意义的值
print(s.dropna())

##  code 4
print(s.fillna('missing'))
print(s.fillna(method = 'ffill', axis=0))  

##  code 4 

s = pd.Series([1, 2, None, 4, None, 7])
print(s.interpolate(method='linear'))     #线性插值  [1.0 , 2.0 ....7.0]


## code 5

d = {
    'col1': {'row1': 1, 'row2': 10, 'row3': 100, 'row4': 1000, 'row5': 10000},
    'col2': {'row1': 2, 'row2': None, 'row3': None, 'row4': 2000, 'row5': 20000},
    'col3': {'row1': 3, 'row2': 30, 'row3': 300, 'row4': None, 'row5': 40000},
    'col4': {'row1': 4, 'row2': 40, 'row3': 400, 'row4': 4000, 'row5': 40000}
}

## 将上边的数据进行翻转
df = pd.DataFrame(d)
print(df)


#        col1     col2     col3   col4
# row1      1      2.0      3.0      4
# row2     10      NaN     30.0     40
# row3    100      NaN    300.0    400
# row4   1000   2000.0      NaN   4000
# row5  10000  20000.0  40000.0  40000

print(df.interpolate(method='linear'))

#        col1     col2     col3   col4
# row1      1      2.0      3.0      4
# row2     10    668.0     30.0     40
# row3    100   1334.0    300.0    400
# row4   1000   2000.0  20150.0   4000
# row5  10000  20000.0  40000.0  40000

print(2668 / 2)   #1334.0