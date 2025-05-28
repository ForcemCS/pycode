##测试1，求平均数，当传入的数据为空时，抛出异常
def average(*args):
    try:
        return sum(args) / len(args)
    except ZeroDivisionError:
        raise ValueError('At least one argument must be passed to function.')
    
#print(average())

##测试2

def separator(*,string='-',c=10):
    print(string * c)

separator(string='')


##测试3

data = ['a', 'b', 'c', 'd', 'c', 'a']

count = {}
for ele  in  data:
    count[ele] = count.get(ele, 0) + 1
print(count)


from collections import Counter

c = Counter(data)

a = dict(c)
print(a)