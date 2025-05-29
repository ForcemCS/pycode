##函数作为参数,code1
def add(a, b):
    return a + b

def greet(name):
    return f'Hello {name}'

def apply(func, *args):
    return func(*args)

print(apply(add,2,3))

## 函数作为参数,code2
f  = lambda a, b, c : a + b +c
print(f(10,20,30))

result = (lambda x,y : x + y) (1,2)
print(result) 


def apply1(func, *args):
    return func(*args)

print(apply1((lambda x,y : x + y),70,80))
print(apply1(lambda x,y : x + y,70,80))


##  函数返回函数,code3

def mult(a,b):
    return a * b 

def power(x, n):
    return x ** n

def choose_operator(name):
    if name == 'power':
        return power
    if name == 'mult':
        return mult
 
op = choose_operator('power')  ##选择一个函数实例化出一个具体的函数

print(op(2,3))
print(choose_operator('power')(2,4))
print('-' * 20 )



##  函数返回函数,code4

def choose_operator(name):
    if name == 'power':
        return lambda x, n : x ** n
    if name == 'mult':
        return lambda a, b : a *b 
 
op = choose_operator('power')  ##选择一个函数实例化出一个具体的函数

print(op(2,3))
print(choose_operator('power')(2,4))