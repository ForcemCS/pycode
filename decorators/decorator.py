#code1
def outer(func):
    def inner(*args,**kwargs):
        print(f"Calling {func.__name__} ....")
        result = func(*args, **kwargs)
        return result
    return inner

##方式1
def add_1(x,y):
    return x + y

def greet(name):
    print(f"Hello {name} ")

##我们可以对上边的函数进行wrapper
a = outer(add_1)
g = outer(greet)

print(a(1,2))
print(g('Wu Kui'))
print('-' * 20 )

##方式2
@outer
def add_2(x,y):
    return x + y
print(add_2(1,2))
@outer
def greet_2(name):
    print(f"Hello {name}")
    
print(greet_2('Jack'))

@outer
def jojn(data,*, item_sep='|', line_sep='\n'):
    return line_sep.join(
        [
            item_sep.join( str(item) for  item in row)  for row in data
        ]
    )
data = (1, 2, 3), ('a', 'b', 'c' )
print(jojn(data))
print('-' * 20 )
    

##code2

def log(func):
    def inner(*args, **kwargs):
        result = func(*args, **kwargs)
        print(f'{func.__name__} called... result={result}')
        return result
    return inner

@log
def greet_3(name):
    return  f"Hello {name}"
print(greet_3.__closure__)
print(hex(id(greet_3)))
    
print(greet_3('Jack'))

## code3

import logging
from  time import perf_counter

logging.basicConfig(
    format='%(asctime)s %(levelname)s: %(message)s',
    level=logging.DEBUG
)

logger = logging.getLogger('Custom Log')

logger.debug('debug message')
logger.error('some error happened')

def log(func):
    def inner(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        end = perf_counter()
        logger.debug(f'called={func.__name__}, elapsed={end - start}')
        return result
    return inner

@log
def add(x,y,z):
    return x + y + z
@log
def join(data, *, item_sep=' ', line_sep='\n'):
    return line_sep.join([item_sep.join(str(item) for item in row) for row in data])

print(add(1,2,3))
data = ([1,2], ['a','b'])
print(join(data))