#1.passing func as  arguement
def add(x,y):
    return x + y
def apply(func, a, b):
    result = func(a,b)
    return result
print(apply(add,1,2))

#2.nested function

def say_hello(first_name='wu', last_name='kui'):
    def assemble_name():
        return ' '.join([first_name,last_name])
    return ' '.join(['Hello, ', assemble_name(), '!'])


print(say_hello())

#3.returning  func

def identity(func):
    return func

def add(x,y):
    return x + y

f = identity(add)
print(f(2,3))


def generate_func(name):
    def add(a, b):
        return a + b

    def mult(a, b):
        return a * b

    if name == 'sum':
        return add
    else:
        return mult

f = generate_func('mult')
print(f(2,3))
