import pandas as pd
import numpy as np # 经常和 pandas 一起使用，这里用来创建 NaN 值

# 1. 从 Series 对象列表 (from a list of Series objects)

s1 = pd.Series({'name': 'Alice', 'age': 25, 'city': 'New York'})
s2 = pd.Series({'name': 'Bob', 'age': 30, 'city': 'Paris'})
s3 = pd.Series({'name': 'Charlie', 'age': 35, 'city': 'London'})

# 将 Series 列表传入 DataFrame 构造函数
df_from_list_of_series = pd.DataFrame([s1, s2, s3])

print(df_from_list_of_series)

# 2. 从列表的列表 (from a list of lists)
data = [
    ['Alice', 25, 'New York'],
    ['Bob', 30, 'Paris'],
    ['Charlie', 35, 'London']
]

# 创建 DataFrame，并手动指定列名
df_from_list_of_lists = pd.DataFrame(data, columns=['Name', 'Age', 'City'])

print(df_from_list_of_lists)

# 3. 手动指定索引的例子 (基于“列表的列表”)：
data = [[1, 2], [3, 4]]
df_manual_index = pd.DataFrame(data, 
                               columns=['Col_A', 'Col_B'], 
                               index=['Row_1', 'Row_2'])
print(df_manual_index)


data = {
    'Product': ['Apple', 'Banana', 'Carrot', 'Donut'],
    'Category': ['Fruit', 'Fruit', 'Vegetable', 'Bakery'],
    'Price': [1.2, 0.5, 0.8, 1.5],
    'InStock': [True, True, False, True]
}
df = pd.DataFrame(data)
print(df)

## code1 
# 每一个series对象代表一行，变量名就是row名称，可以关联到同一个索引(也就是列名称)
columns = pd.Index(
    [
        'The Bronx',
        'Brooklyn',
        'Manhattan',
        'Queens',
        'Staten Island'
    ]
)

counties = pd.Series(
    ['Bronx', 'Kings', 'New York', 'Queens', 'Richmond'],
    index=columns,
    name='county'
)


populations = pd.Series(
    [1_418_207, 2_559_903, 1_628_706, 2_253_858, 476_143],
    index=columns,
    name='population'
)
gdp = pd.Series(
    [42.695, 91.559, 600.244, 93.310, 14.514],
    index=columns,
    name='gdp'
)
areas = pd.Series(
    [42.10, 70.82, 22.83, 108.53, 58.37],
    index=columns,
    name='area'
)


## 每行有五条数据
new_york = pd.DataFrame([counties, populations, gdp, areas])
print(new_york)

print(new_york.transpose())

## code 2

d = {
    'county': counties,
    'population': populations,
    'gdp': gdp,
    'area': areas
}

## 每列有五条数据
new_york = pd.DataFrame(d)

print(new_york)


## code 3

counties = {
    'The Bronx': 'Bronx',
    'Brooklyn': 'Kings',
    'Manhattan': 'New York',
    'Queens': 'Queens',
    'Staten Island': 'Richmond'
}

populations = {
    # 会自动调整对应关系
    'Manhattan': 1_628_706,
    'Queens': 2_253_858,
    'Staten Island': 476_143,
    'The Bronx': 1_418_207,
    'Brooklyn': 2_559_903
}

gdp = {
    'The Bronx': 42.695,
    'Brooklyn': 91.559,
    'Manhattan': 600.244,
    'Queens': 93.310,
    'Staten Island': 14.514
}


areas = {
    'The Bronx': 2.10,
    'Brooklyn': 70.82,
    'Manhattan': 22.83,
    'Queens': 108.53,
    'Staten Island': 58.37
}

d = {
    'county': counties,
    'population': populations,
    'gdp': gdp,
    'area': areas
}

new_york = pd.DataFrame(d)
print(new_york)

# code 4

new_york = pd.DataFrame([counties, populations, gdp, areas])
print(new_york)

a =  new_york.rename(
    index={
        0: 'country',
        1: 'populatation',
        2: 'gdp',
        3: 'area'
    }
)

print(a)
print(new_york)


# code 5 

b = new_york.rename(
    columns={
        0: 'county',
        1: 'population',
        2: 'gdp',
        3: 'area'
    }
)

print(b)
print('-----  -----')

# code 6 


# 这里创建了5个列表，分别存储了纽约市五个行政区（burroughs）的名称、对应的县名（counties）、人口、GDP和面积。
burroughs = ['The Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island']
counties = ['Bronx', 'Kings', 'New York', 'Queens', 'Richmond']
populations = [1_418_207, 2_559_903, 1_628_706, 2_253_858, 476_143]
gdp = [42.695, 91.559, 600.244, 93.310, 14.514]
areas = [42.10, 70.82, 22.83, 108.53, 58.37]

# 这一步是理解的关键。这里使用了 “列表的列表” 来创建 DataFrame。
data = [burroughs, counties, populations, gdp, areas]

new_york = pd.DataFrame(
    data,
    index=['burroughs', 'county', 'population', 'gdp', 'area']
)

# --------
#                     0         1           2        3             4
# burroughs    The Bronx  Brooklyn   Manhattan   Queens  Staten Island
# county           Bronx     Kings    New York   Queens       Richmond
# population     1418207   2559903     1628706  2253858         476143
# gdp             42.695    91.559     600.244   93.310         14.514
# area             42.10     70.82       22.83   108.53          58.37
# --------

# 上边的输出非常不易阅读，进行转置，结构非常清晰
new_york = new_york.transpose()

# -----
#      burroughs    county population      gdp   area
# 0    The Bronx     Bronx    1418207   42.695  42.10
# 1     Brooklyn     Kings    2559903   91.559  70.82
# 2    Manhattan  New York    1628706  600.244  22.83
# 3       Queens    Queens    2253858   93.310 108.53
# 4  Staten Island  Richmond     476143   14.514  58.37
# -----


#使用 burroughs 这一列的值（'The Bronx', 'Brooklyn'等）来作为新的行索引，替换掉当前的数字索引 0, 1, 2, 3, 4。
new_york = new_york.set_index('burroughs')

# --------------
#                  county population      gdp    area
# burroughs
# The Bronx         Bronx    1418207   42.695    42.1
# Brooklyn          Kings    2559903   91.559   70.82
# Manhattan      New York    1628706  600.244   22.83
# Queens           Queens    2253858    93.31  108.53
# Staten Island  Richmond     476143   14.514   58.37
# --------------


print(new_york)

print(new_york.info())
print(new_york.index)           #Index(['The Bronx', 'Brooklyn', 'Manhattan', 'Queens', 'Staten Island'], dtype='object', name='burroughs')


new_df = new_york.drop(columns='county')
print(new_df)

new_df = new_df.drop(index=['The Bronx', 'Queens'])
print(new_df)