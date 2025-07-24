import pandas as pd
import numpy as np


data = [100, 200, 300, 400]
idx = pd.Index(['alpha', 'beta', 'gamma', 'delta'])
s = pd.Series(data, index=idx)

print(idx)
print(s.index)

##取出关联后数据的标签索引
label_index = s.index

## 然后筛选标签索引中包含'e'的索引
# a = label_index.str.contains('e')
# print(a)

filtered_index = label_index[label_index.str.contains('e')]
print(f"筛选后的索引标签: {filtered_index}")

##取出满足条件的原始数据

for i in filtered_index:
    print(s.loc[i])
    

print(s.loc[filtered_index])

print('--- * 20 ')


#### 快捷写法
print("\n" + "="*20 + "  快捷写法  " +  "="*20  + "\n")

result = s.loc[s.index.str.contains('e')]

# for k in result:
#     print(k)
result_dict  = {k: v for k, v in result.items()}
print(result_dict)
