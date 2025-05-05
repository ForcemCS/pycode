suits = ["John", "wu kui", "Smitch"]


#对list进行迭代
for suit in suits:
    abbrev = suit[0].upper()
    print(f"{abbrev} = {suit}")
print("Done--------\n")


for c in 'python':
    print(c)

#此时变量没有消失，仍然存在
print(c)
print("Done--------")

for b in  range(2, 11, 2):
    print(b)

a = list(range(2, 11, 2))
print(a)
print("Done--------\n")

for i in  range(2):
    for j  in range(2):
        print(f"i={i}, j={j}")
    print('-' * 10)
print("Done--------\n")

##编写一个矩阵,迭代其中的每一个元素
m = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


print(a, b) 

for row_idx in range(3):
    for col_idx in range(3):
        #print(f"[{row_idx}, {col_idx}] = ",m[row_idx][col_idx])
        print(f"a{row_idx + 1}{col_idx + 1} = ",m[row_idx][col_idx])
print('-' * 10)


a = len(m)       #确定行数
b = len(m[0])    #确定每行的列数

for row_idx in range(len(m)):
    for col_idx in range(len(m[row_idx])):
        print(f"a{row_idx + 1}{col_idx + 1} = ",m[row_idx][col_idx])
print("Done--------\n")

#输出单位阵
n = 5 

matrx = []
for row_idx in range(n):
    row = []
    for col_idx in range(n):
        if row_idx == col_idx:
            row.append(1)
        else:
            row.append(0)
    matrx.append(row)
print(matrx)
print("Done--------\n")

data  =  [1, 2, 3, 4]
#实际上创建了一种可迭代的东西
print(enumerate(data))
for  t  in enumerate(data):
    idx, el = t
    print(idx, el)

    