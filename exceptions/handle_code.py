##示例1
try:
    1 / 0
except ZeroDivisionError as ex:
    print(f"Exception occurred: {type(ex).__name__}, {ex}")
print('Code continues running here ...')

l = [1, 2, 3, 4]
while len(l) > 0:
    print(l.pop())
print("The data has been processed")


##示例2
l = [1, 2, 3, 4]
try:
    while True:
        print(l.pop())
except IndexError:
    # index error means  list is now empty    
    print("All done - all elements has been popped.")

l = (1, 2, 3, 4 )
try:
    print(l.pop())
except Exception as ex:
    print(f"Exception occurred : {ex}")

##示例3

data = [10, 20, 30, 40 ]

sum_data = 0 
count = 0 

for elemunt  in data:
    sum_data +=  elemunt
    count += 1
average_data = sum_data / count


print(f"平均数：{average_data:.3f}")


#示例4
data = [10, 20, 'adc',15,'cc']

sum_data = 0 
count = 0 
try:
    for elemunt  in data:
        try:
            sum_data += elemunt
            count += 1
        except TypeError:
            pass
    average_data = sum_data / count
    print(average_data)
except ZeroDivisionError as ex:
    average_data = 0 
    print(average_data)


#示例5
try:
    raise ValueError('custom message')
except ValueError as ex:
    print(f"handle a ValueError : {ex}")
finally:
    print("this's always executed")
print("all done")