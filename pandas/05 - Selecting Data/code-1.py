import pandas as pd
import numpy as np

# 1.创建一个示例 DataFrame
data = {'Math': [85, 90, 78, 92],
        'Science': [91, 88, 95, 89],
        'History': [80, 82, 88, 85]}
students = ['Alice', 'Bob', 'Charlie', 'David']
df = pd.DataFrame(data, index=students)
# ```
#          Math  Science  History
# Alice      85       91       80
# Bob        90       88       82
# Charlie    78       95       88
# David      92       89       85
# ```

print(df)

## 2.取出矩阵中的单个元素
alice_math = df.loc['Alice', 'Math']
print(alice_math)  # 输出: 85

alice_math_iloc = df.iloc[0, 0]
print(alice_math_iloc)  # 输出: 85

## 3. 行的标签或者隐式索引
bob_scores = df.loc['Bob']
print(bob_scores)

charlie_scores = df.iloc[2]


## 4.切片 (Slicing)
# loc 的切片是闭区间，即包含开始和结束标签。
# iloc 的切片是半开区间，即包含开始位置，不包含结束位置（和 Python 列表切片规则一样）。

#loc 切片: 选取从 Bob 到 David 的行，以及从 Science 到 History 的列。

# 包含 'David' 行和 'History' 列
slice_loc = df.loc['Bob':'David', 'Science':'History']
print(slice_loc)
# ```
# #          Science  History
# # Bob           88       82
# # Charlie       95       88
# # David         89       85
# ```

# 5.花式索引 (Fancy Indexing)

#1)loc: 选取 Alice 和 Charlie 的 Math 和 History 成绩。
fancy_loc = df.loc[['Alice', 'Charlie'], ['Math', 'History']]
print(fancy_loc)

#          Math  History
# Alice      85       80
# Charlie    78       88

# 2)iloc: 选取第1、4行（位置0, 3）和第1、3列（位置0, 2）。
fancy_iloc = df.iloc[[0, 3], [0, 2]]
print(fancy_iloc)

#---------------------------------------------
#一旦你用 loc 或 iloc 成功地选取了数据，就可以用赋值符号 (=) 来修改这些数据。

# 1. 替换单个单元格的值 (with a scalar value)
# “Scalar value” 指的是单个值（如一个数字、一个字符串）。

# 将 Charlie 的科学成绩从 95 改为 96
print("--- 修改前 ---")
print(df)

df.loc['Charlie', 'Science'] = 96

print("\n--- 修改后 ---")
print(df)

# 2. 替换多个单元格的值
# a. 用一个标量值进行广播 (broadcast)
# “广播”意味着将一个单个值赋给所有被选中的单元格。

# 将 Alice 和 Bob 的历史成绩都改为 0
df.loc[['Alice', 'Bob'], 'History'] = 0
print(df)

#          Math  Science  History
# Alice      85       91        0
# Bob        90       88        0
# Charlie    78       96       88
# David      92       89       85

# b. 用形状相同的列表或数组替换
# 替换值的形状必须和被选区域的形状完全一致。

# 重新创建df以获得干净数据
df = pd.DataFrame(data, index=students)

# 将一个 2x2 的区域替换成一个新的 2x2 列表
new_values = [[100, 100], [100, 100]]
df.loc['Alice':'Bob', 'Math':'Science'] = new_values
print(df)

#          Math  Science  History
# Alice     100      100       80
# Bob       100      100       82
# Charlie    78       95       88
# David      92       89       85

# c. 用一维数组/列表进行广播
# 当用一维数据替换多列时，这一维数据会广播到每一列。更常见的是用一维数据替换单列的多个值。

# 将 David 和 Alice 的科学成绩分别更新为 99 和 89
df.loc[['David', 'Alice'], 'Science'] = [99, 89]
print(df)


# 3. 用 Series 或 DataFrame 替换（注意！索引可能导致问题）
# 这是非常重要的一点。当你用一个 Series 或 DataFrame 去赋值时，Pandas 会根据索引进行对齐。如果索引不匹配，你可能会得到不想要的结果（通常是 NaN）。
# 创建一个 Series，其索引与我们要替换的目标索引一致
new_history_scores = pd.Series({'Alice': 81, 'David': 86})

# 因为索引 ('Alice', 'David') 能匹配上，所以赋值成功
df.loc[['Alice', 'David'], 'History'] = new_history_scores
print(df)

