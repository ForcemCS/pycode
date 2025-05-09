# for else整个是 一个代码逻辑
# for i in range(5):
#     <code block1>
# else:
#     <code block2>
    

for i in range(100):
    print(i)
    if i >= 5:
        print("breaking out of  loop")
        break
print("-" * 10 )

##只打印偶数

for i in range(1, 11):
    if i % 2  == 1:
        continue
    print(i) 
print("-"  * 10)


i = 0 

while True:
    i += 1
    if i > 5:
        break
    print(i)
print('-'  * 10 ) 


##如果 for 循环没有被 break 中断，那么执行 else 子句。否则跳过 else。
data = [1, 2, 3, 4, 5 ]

all_completed = True

for i in  data:
    if i <= 0:
        all_completed = False
        break
    print(i)
#else:
#    print("all data complete")
if  all_completed:
     print("all data complete")


for i in list(range(1,4)):
    for j in list(range(1, 5)):
        print(f"{i} x {j} = ", i * j)
    print("-" * 15 )


data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)

for row_idx, row_ele in  enumerate(data):
    if  row_ele[2] > row_ele[1]:
        data1 = row_ele[2] - row_ele[1]
        print(f"{row_ele[0]} 的绝对值为: " ,data1)

        row_ele.append(data1)
    else:
        data1 = row_ele[1] - row_ele[2]
        print(f"{row_ele[0]} 的绝对值为: " ,data1)
        row_ele.append(data1)
print(data)

data = (
    ['2021-01-01', 10, 20],
    ['2021-01-02', 20, 18],
    ['2021-01-03', -10, 10],
    ['2021-01-04', 100, 102],
    ['2021-01-05', 20, 45]
)

for row in data:
    row.append(abs(row[1] - row[2]))
print(data)

max_spread = data[0][-1]
date = data[0][0]

for a,b,c,d in data[1:]:
    if d > max_spread:
        max_spread = d
        date = a
print(date,max_spread)        



data = [
    [10, 20],
    [20, 30],
    [35, 50],
    [45, 60]
]

start = 0 
for row  in  data:
        row.append('')
        break