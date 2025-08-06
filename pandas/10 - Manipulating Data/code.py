import pandas as pd
import numpy as np

# df  = pd.read_csv('world_bank_countries.csv',nrows=20)
# print(df)

# df.to_csv('world_bank_countries.csv', index=False)

## code 1

m = np.array(
    [
        [1, 10, 100],
        [2, 20, 200],
        [3, 30, 300],
        [4, 40, 400]
    ]
)

print(np.mean(m, axis=0))    ##按行计算平均值(列的方向)

df = pd.DataFrame(
    m,
    index=['r0', 'r1', 'r2', 'r3'],
    columns=['c0', 'c1', 'c2']
)

print(df.mean().loc['c0'])
print(df.sum(axis=1))

print(df['c0'] + df['c1'])

print(df.loc[:, 'c0']  + df.iloc[:, 1])

print(np.sin(df))

print(df.transpose())
#      r0   r1   r2   r3
# c0    1    2    3    4
# c1   10   20   30   40
# c2  100  200  300  400

## code 2 
df = pd.read_csv('world_bank_countries.csv')
print(df.iloc[:5])     #显示前5行

print(df.info())
print(df['LatestPopulationCensus'].unique())
print('-'  * 30 )
    

latest_census = pd.to_numeric(df['LatestPopulationCensus'],errors='coerce')
print(latest_census)
print('-'  * 30 )
print(latest_census.dropna().astype(int))   #  将float64转为int64
print('-'  * 30 )
print(latest_census[latest_census.notnull()])

## code 3

df_1 = pd.DataFrame(
    [
        [1, 2, 3],
        [2, 3, 4]
    ],
    index = ['r1', 'r2'],
    columns = ['c1', 'c2', 'c3']
)

df_2 = pd.DataFrame(
    [
        [10, 20],
        [20, 30]
    ],
    index = ['r1', 'r2'],
    columns = ['c10', 'c20']
)

print(df_1)
#     c1  c2  c3
# r1   1   2   3
# r2   2   3   4
print(df_2)
#     c10  c20
# r1   10   20
# r2   20   30

print(pd.concat([df_1, df_2], axis=1))
#     c1  c2  c3  c10  c20
# r1   1   2   3   10   20
# r2   2   3   4   20   30

## code 4

df_1 = pd.DataFrame(
    [
        [1, 2, 3],
        [2, 3, 4]
    ],
    index = ['r1', 'r2'],
    columns = ['c1', 'c2', 'c3']
)

df_2 = pd.DataFrame(
    [
        [10, 20],
        [20, 30]
    ],
    index = ['r10', 'r2'],
    columns = ['c10', 'c20']
)

print(pd.concat([df_1, df_2], axis=1))
#       c1   c2   c3   c10   c20
# r1   1.0  2.0  3.0   NaN   NaN
# r2   2.0  3.0  4.0  20.0  30.0
# r10  NaN  NaN  NaN  10.0  20.0


## code 5 
df = pd.read_csv('world_bank_countries.csv')
latest_census = pd.to_numeric(df['LatestPopulationCensus'], errors='coerce')
mask = latest_census.notnull()
print(mask)
subset = df.loc[:, ['CountryCode', 'ShortName']][mask]
print(subset)

result = pd.concat([subset, latest_census.dropna().astype(int)], axis=1)
print(result)


## code 5 
df = pd.read_csv('world_bank_countries.csv')
latest_census = pd.to_numeric(df['LatestPopulationCensus'], errors='coerce').dropna().astype(int)
subset = df[['CountryCode', 'ShortName']]

pd.concat([subset, latest_census], axis=1, join='inner')