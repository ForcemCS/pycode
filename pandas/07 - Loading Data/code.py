import csv
import numpy as np
import pandas as pd

# code1 
# with open('populations.csv') as f :
#     data = csv.reader(f)
#     print(next(data))
    
    
df = pd.read_csv('populations.csv')
print(df)


df = df.rename(
    columns={
        'Geographic Area': 'region',
        'July 1, 2001 Estimate': '2001',
        'July 1, 2000 Estimate': '2000',
        'April 1, 2000 Population Estimates Base': 'not needed'
    }
)

print(df)

df = df.drop(columns='not needed')
print(df)


## code 2 

#将某一列作为显示索引，替换掉行数字索引

df = df.set_index('region')
print(df)
print(df.info())

## code 3


df = pd.read_csv(
    'populations.csv',      # 参数1: 文件名
    header=0,               # 参数2: 指定哪一行为列名
    usecols=[0, 1, 2],      # 参数3: 指定要读取哪些列
    names=['region', '2001', '2000'], # 参数4: 为读取的列指定新的名字
    index_col=0             # 参数5: 指定哪一列作为行索引
)
print(df)
print('--' * 20 )

## code4  
print(df.loc[:, '2001'])

print(df['2001'])

increase = 100 * (df['2001'] - df['2000']) / df['2000']
print(increase)

##1. 修改了原始的df
df['increase'] = increase

print(df)
print('--' * 20 )

## 2. 避免修改原始df

df_with_increase = df.assign(
    increase = lambda x : 100 *   (x['2001'] - x['2000']) / x['2000']
)

print(df_with_increase)
# print(df)


final_df = (
    df.assign(increase=lambda x: 100 * (x['2001'] - x['2000']) / x['2000'])
      .rename(columns={'increase': 'Growth Rate (%)'})
      .sort_values(by='Growth Rate (%)', ascending=False)
)

print(final_df)


## code 5

df = pd.read_excel('populations.xls', sheet_name='data')

print(df)


df = pd.read_excel(
    'populations.xls',      # 参数1: 文件名
    header=0,               # 参数2: 指定哪一行为列名
    usecols=[0, 1, 2],      # 参数3: 指定要读取哪些列
    names=['region', '2001', '2000'], # 参数4: 为读取的列指定新的名字
    index_col=0             # 参数5: 指定哪一列作为行索引
)

print(df)