#测试1
#calcute the  smallest absolute value of squence，并处理空list的情况
values = []

try:
    minimum = abs(values[0])
    for min in values[1:]:
        if  abs(min)  < minimum:
            minimum = abs[min]
except IndexError as ex:
    print(f"Exception  occurred : {ex}")
    minimum  = 0 
print(minimum)
    
#侧式2
# 抛出一个异常，自定义提示，并打印出来

try:
    raise ValueError('定义的value错误')
except ValueError as ex:
    print(ex)