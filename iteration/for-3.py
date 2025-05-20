m = [
    [0, 1],
    [2, 3, 4, 5, 6],
    [7, 8, 9],
    [10]
]

##取出list中的每个元素
for sublist in m:
    for ele in  sublist:
        print(ele)
print("done-------------")

for row_idx, row in enumerate(m):
    for col_idx, col  in enumerate(row):
        print(row_idx + 1,col_idx + 1 ,col)


data  = [80, 90, None, 95, None]

count = 0 
total = 0 

for  a in range(len(data)):
    if data[a]  is not None:
        count  += 1
        total  +=  data[a]
average = total / count
#average表示要插入的变量
#：表示开始格式说明

print(f"{average:.5f}")


data = [10.5, 11.2, 9.8, None, 11.5, None]
#不是None的元素出现了一共出现了几次
count = sum(1 for val in data if val is not None)
total = sum(val for val in data if val is not None)
average = total / count
#列表推导式的写法，用于创建新的list
#[ A if 条件 else B for 变量 in 列表 ],读作：「如果 条件 成立就用 A，否则用 B，遍历 列表」

data = [val if val is not None else average for val in data]
print(data)

from statistics import fmean

data = [10.5, 11.2, 9.8, None, 11.5, None]
average = fmean(val for val in data if val is not None)
data = [val if val is not None else average for val in data]
data