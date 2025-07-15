import numpy as np 

## code1 
m = np.array([-1, 1, -2, 2, -3, 3])
m_bool = np.less(m, 0)
print(m_bool)                #[ True False  True False  True False]
print(m < 0 )                #[ True False  True False  True False]

mask = m > 0                 #[False  True False  True False  True]

print(m[mask])               #[1 2 3]

#与上达到相同的效果,意思是数组m与bool数组 m > 0 做对照，返回为True的部分
print(m[m >0 ])              #[1 2 3]


## code2

m1 = np.arange(1,7)
print(m1[m > 0 ])          #[2 4 6]

 ## code 3
 
m = np.array(
[[-1, 1, -2, 2],
 [-3, 3, -4, 4],
 [-5, 5, -6, 6]
]
)

m < 0 

print(m[ m < -1 ])    #[-2 -3 -4 -5 -6]


## code 4 

arr = np.arange(-5, 6)
mask = (arr > 0 ) & (arr < 4)
print(mask)
print(arr[mask])       #[1, 2, 3]


## code5

## 理解下边的代码，关键抓住下边注释中的索引
# dates:
# [ 2020-10-29,  # 索引 0
#   2020-10-28,  # 索引 1
#   2020-10-27,  # 索引 2
#   2020-10-26,  # 索引 3
#   2020-10-23,  # 索引 4
#   2020-10-22,  # 索引 5
#   2020-10-21,  # 索引 6
#   2020-10-20,  # 索引 7
#   2020-09-29 ] # 索引 8

# ohlc:
# [ [112.37, 116.93, 112.2,  115.32],  # 索引 0
#   [115.05, 115.43, 111.1,  111.2 ],  # 索引 1
#   [115.49, 117.28, 114.54, 116.6 ],  # 索引 2
#   [114.01, 116.55, 112.88, 115.05],  # 索引 3
#   [116.39, 116.55, 114.28, 115.04],  # 索引 4
#   [117.45, 118.04, 114.59, 115.75],  # 索引 5
#   [116.67, 118.7,  116.45, 116.87],  # 索引 6
#   [116.2,  118.98, 115.63, 117.51],  # 索引 7
#   [114.55, 115.31, 113.57, 114.09] ] # 索引 8


# l = [[1, 2],[3, 4]]
# t = (10, 20, 30)

# a= list(zip(l,t))
# print(a)           # [([1, 2], 10), ([3, 4], 20)]
 

from dateutil import parser

import csv

with open('AAPL.CSV') as f:
    reader = csv.reader(f, skipinitialspace=True)
    header = next(reader)
    
    data = [ d  for d in reader ]

arr = np.array(data)


# dates = [ parser.parse(dt) for dt in  arr[:, 1] ]

# print(dates)

dates = np.array([ parser.parse(dt) for dt in  arr[:, 1] ])
print(dates,dates.shape,sep='\n')

ohlc = arr[:, [4, 5, 6, 2]].astype(float)
print(ohlc)

## 收盘股价大于116
print(ohlc[:, 3] > 116.0 )      #一维slice

print(ohlc[ohlc[:,  3] > 116.0 ])


print(dates[ohlc[:, 3] > 116.0])
print('*' * 30)

mask = ohlc[:, 3] > 116.0 

# filtered_data  = [
#     [date, row]
#     for date, row in  zip(dates[mask], ohlc[mask])
# ]

# for row in filtered_data:
#     print(row)
    
    
    
filtered_data  = [
    [date, *row]
    for date, row in  zip(dates[mask], ohlc[mask])
]


for row in filtered_data:
    # print(row)
    #隐藏类型信息
    print(*row, sep=', ')
    
