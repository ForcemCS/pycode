import numpy as np 
import pandas as pd

## code 1
df  = pd.read_csv('populations.csv')
print(df[:5])
print('--' * 20 )
data = df.set_index('Geographic Area')

print(data[:5], data.loc['United States'])
print('--' * 20 )
print(data.loc['United States'])
print('--' * 20 )
print(data['July 1, 2001 Estimate'])
print('--' * 20 )

mask = data['July 1, 2001 Estimate'] < 3_000_000
print(mask)
print('--' * 20 )

mask1 = data.iloc[:, 0] < 3_000_000
print(mask1)
print('--' * 20 )

data_mask = data[mask]
print(data_mask)
print('--' * 20 )


## code 2
s = pd.Series([10, 20, 30, 40], index=['Z', 'x', 'y', 'w'])
print(s) 
print(s.sort_index())
# Z    10
# w    40
# x    20
# y    30

## code 3

print(s.sort_index(key=lambda ind: ind.str.casefold()))  #按照行的显示索引进行排序

s = pd.Series(list('abcded'), index=[-1, -3, -5, 0, 2, 4])

np.abs(s.index)

print(s.sort_index())
print(s.sort_index(key=lambda ind: np.abs(ind)))
#  0    d
# -1    a
#  2    e
# -3    b
#  4    d
# -5    c

## code 4 

print(data[:5])
print(data[:7].sort_index(key=lambda ind : ind.str.casefold()))
print(data[:7].sort_index(key=lambda ind : ind.str.len(), ascending=False))

## code 5
print(data.sort_values('July 1, 2001 Estimate', ascending=False))
print('--' * 20 )

df = pd.read_csv('world_bank_countries.csv')
print(df[:5])
print('--' * 20 )

data = df[['ShortName', 'Region', 'CountryCode', 'CurrencyUnit']]
print(data[:5])
print('--' * 20 )


df = pd.read_csv(
    'world_bank_countries.csv',
    names=['code', 'name', 'currency', 'region'],
    usecols=[0, 1, 5, 7],
    header=0
)

print(df)
print(df[['region', 'code', 'name', 'currency']])


df = pd.read_csv(
    'world_bank_countries.csv',
    names=['code', 'name', 'currency', 'region'],
    usecols=[0, 1, 5, 7],
    header=0
)[['region', 'code', 'name', 'currency']]

print(df)

print(df.info())
print('--' * 20 )
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 14 entries, 0 to 13
# Data columns (total 4 columns):
#  #   Column    Non-Null Count  Dtype
# ---  ------    --------------  -----
#  0   region    13 non-null     object
#  1   code      14 non-null     object
#  2   name      14 non-null     object
#  3   currency  13 non-null     object
# dtypes: object(4)
# memory usage: 576.0+ bytes
# None

## code 5

print(df['region'].notnull())    ##返回的是布尔值

data = df[df['region'].notnull()]  ##删除掉region为空的行
print(data)

print(df.info())

print(df.dropna(axis=0))      #删除掉还有nan的行
print('--' * 20 )
print(data.sort_values('region'))
print('--' * 20 )
sorted_data = data.sort_values(['region', 'code'])
print(sorted_data, type(sorted_data))
print('--' * 20 )

## code 6

df = pd.DataFrame({
    'name': ['Alice', 'Bob', 'Charlie'],
    'age': [25, 30, 35]
})
for _, row in df.iterrows():
    print(row)
    print('-' * 20 )

for _, row in df.iterrows():
    print(f"姓名: {row['name']}, 年龄: {row['age']}")
    
for _, row in df.iterrows():
    print(row.values)