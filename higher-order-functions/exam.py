##测试1
def power(x):
    return x ** 2 -1

def extreme_power(func, l, r, n,  extreme):
    interval = ( r - l ) / n
    value = [ func(l + i * interval ) for i in range(1, n +1 ) ]
    if extreme == 'min':
        print(min(value))
    if extreme == 'max':
        print(max(value))
        
extreme_power(power, -5, 5, 4, 'min')
    

##测试2
def bivariate_func(x,y):
    return 2 * x + 3 * y + 5

data = [(1,1), (1,2)]

result = map(lambda pairs: bivariate_func(pairs[0],(pairs[1])), data)
print(list(result))

##测试3

data = ['absolute', 'abs' ,'bbivariate']

result_f = filter(lambda x : x[0] == 'a',data)

print(list(result_f))

result_m = map(lambda x : x.upper()  ,data)

print(list(result_m))