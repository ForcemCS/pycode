def say_hello():
    return 'hello'

print(say_hello())

f = say_hello
print(f())
print(f  is  say_hello)

#输出函数的内置属性
print(f.__name__)

##local  namespace
#locals() 是一个内置函数，返回当前作用域的 局部变量字典。
def add(a, b, c):
    print(f"initial namespace: {locals()}")  
    sum = a + b + c
    print(f"after namespace: {locals()}")
    return a + b + c

print(add(1,2,3))

def  find_max(a, b, c):
    max_ = a
    if b > max_:
        max_ = b 
    if c > max_:
        max_ = c
    return max_

print(find_max(1,-1,4))


from datetime import datetime, UTC

#将日志消息打印到控制台当中，没有使用return
def log(message):
    curr_time = datetime.now(UTC).isoformat()
    print(f"{curr_time} - [{message}]")

log('logging start ....')


data = [1, 2, 3]

#遇到第一个return，函数就会退出
def is_all_positive(data):
    for ele in data:
        if ele < 0:
            return False
    return True

print(is_all_positive([1,2,-1])) 
print(is_all_positive(range(1,10)))

d= {'a':1, 'b':2, 'c': -1}
print(d.values())
print(is_all_positive(d.values()))


def gen_matrix(m, n, default_value):
    return [[default_value for  col in range(n)] for row in range(m)]
print(gen_matrix(3,2,0))

print(gen_matrix(n=3,m=2,default_value=1))