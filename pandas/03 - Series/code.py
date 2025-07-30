import pandas as  pd
import numpy as np


## code1

s = pd.Series([10, 20, 30], index=['a', 'b', 'c'])
print(s)
print(s['a'])


## code2
capitals = {
    'USA': 'Washington D.C.',
    'Canada': 'Ottawa',
    'UK': 'London',
    'France': 'Paris'
}

s = pd.Series(capitals)
print(s)
print(s.index)             #Index(['USA', 'Canada', 'UK', 'France'], dtype='object')

print(type(s.values))      #<class 'numpy.ndarray'>
print(s.values)            #['Washington D.C.' 'Ottawa' 'London' 'Paris']


## code 3

a = {'a': 1, 'b': 2}      #dict_items([('a', 1), ('b', 2)])
print(a.items())


print(s.items())          # <zip object at 0x000001DE279E3D40>
print(list(s.items()))    # [('USA', 'Washington D.C.'), ('Canada', 'Ottawa'), ('UK', 'London'), ('France', 'Paris')]


## code4

#series中索引可以是重复的值
areas = pd.Series(
    ['USA', 'Topeka', 'France', 'Lyon', 'UK', 'Glasgow'],
    index=['country', 'city', 'country', 'city', 'country', 'city']
)

print(areas['city'])

a = areas['city']   #类型是series

print(a)


## code 5

s = pd.Series([10, 20, 30, 40, 50], index=list('abcde'))
print(s)
print(s['a':'d'])     #显式索引包含d


#花式索引
print(s[['a', 'c']])

## code6

a = pd.Series([100, 200, 300], index=[10, 20, 30])

#使用隐式索引
print(a.iloc[0])
#显示索引
print(a.loc[10])

## code 7
# name可以认为式添加了一个说明性的属性
areas = pd.Series(
    ['USA', 'Topeka', 'France', 'Lyon', 'UK', 'Glasgow'],
    index=['country', 'city', 'country', 'city', 'country', 'city'],
    name='Areas'
)

a = areas[areas !='Glasgow' ]
print(a)

## code8

s =  pd.Series([10, 20, 30], index=list('abc'), name='test')

new =s.drop(['a', 'c'])
print(new)
print(s)             #此时原始数据没有被修改


print(s.index)       #Index(['a', 'b', 'c'], dtype='object')

print(s.index[[0, 2]])

new = s.drop(s.index[[0, 2]])
print(new)
print(s)