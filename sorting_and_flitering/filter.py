#filter() 函数的目的：从一个可迭代对象（data）中，筛选出那些满足特定条件(条件是返回true)的元素。

##code1
data = [1, 2, 3, 4]

def is_event(x):
    return x % 2 == 0 

events = [x for x in data if  is_event(x) ]
print(events)

events = filter(is_event, data)
print(list(events))
print(list(events))   ##元素已经迭代完，返回的是[]

##code2
data = [
    ('ADAT', 0.6, 0.68, 0.59, 0.66, 86400),
    ('ADBE', 29.43, 29.71, 29.07, 29.14, 7585300),
    ('ADCT', 12.68, 12.69, 12.66, 12.68, 1660500),
    ('ADEP', 6.14, 6.14, 4.95, 5.61, 71000),
    ('ADES', 6.2, 6.22, 6, 6.19, 4800),
    ('ADGF', 4.31, 4.55, 4.31, 4.54, 10200)
]

def closed_higher(rec):
    open_ = rec[1]
    close_ = rec[4]
    return close_ > open_

a = closed_higher(('ADGF', 4.31, 4.55, 4.31, 4.54, 10200))
print(a)                  #true
filtered = filter(closed_higher, data)
print(list(filtered))

filtered = filter(lambda x : x[4] > x[1], data)
print(list(filtered))