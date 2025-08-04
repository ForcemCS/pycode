import pandas as pd

# 读取 CSV 文件
file_path = "Morningstar - European Mutual Funds.csv"
df = pd.read_csv(file_path)

# 列数
print("总列数：", len(df.columns))
print(df.shape)             #(row, col)
# 列名
print("列名：", df.columns.tolist())
print('--' * 20 )

## 前五行的所有数据
print(df.iloc[:5, :])
print(df.info())
print(pd.options.display.max_info_columns)
print(df.info(verbose=True))

stats = df.describe()
print(stats)
pd.options.display.max_columns = None
print(stats)


stats = df.describe(include='all')
print(stats)
print('--' * 20 )
print(stats[ 'fund_return_2018' ])


## code1
data = df.loc[:, ['ticker', 'fund_name', 'morningstar_category', 'fund_return_2018']]
data = data.set_index('ticker')

print(data)
print(data.describe(include='all'))

data['morningstar_category'].nunique()

categories = data['morningstar_category'].unique()

## code2 

sorted_categories = sorted(categories)
for category in sorted_categories:
    print(category)
    
cat_freq = data['morningstar_category'].value_counts()

print(type(cat_freq))                 # <class 'pandas.core.series.Series'>


## code 3

for cat, freq in cat_freq.items():
    print(f'{freq}\t{cat}')


cat_freq.sort_index()

for cat, freq in cat_freq.sort_index().items():
    print(f'{freq}\t{cat}')
    
    
