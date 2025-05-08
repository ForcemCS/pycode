value = 10 

while value < 15 :
    print(value)
    value  = value + 1
print("Done")

price = 100

while price >90:
    print(f"price: {price} waiting for price come down")
    price -= 1
print(f"buying at {price}")

#不会执行代码块
while price >99:
    print("cc")
print("Done")


#逐个删除列表中元素
my_list = list(range(6))

index = 0 
while index < len(my_list):
    item = my_list[index]
    print(f"正在处理元素{item}")
    del my_list[index]  # 删除当前元素，但 index 不变，因为删除后元素会向前移动

print(my_list)

#逐个删除列表中元素
data = [1,2,3,4,5]

while  len(data) >0 :
    last_ele = data.pop()
    print(f'此刻删除的元数据为{last_ele}')
    print(data)