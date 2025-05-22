#a =1 
#b = 1
#print(a / b )

#ValueError：是 Python 的一个内置异常类型，表示“值错误”，通常在函数接收到的参数值不合适时抛出。
#ex  = ValueError('name must be at least 5 characters long')  #创建了一个异常对象，但并没有抛出它,可以使用raise抛出异常
#print(type(ex).__name__,ex,repr(ex),str(ex))

#raise ex   #输出

name = input('Enter name (至少五个字符):')

if len(name) < 5:
    raise ValueError(f"{name} 不满足至少五个字符的条件")

print(f"Hello {name}")

#issubclass(A, B) 是 Python 的内置函数，用于判断类 A 是否是类 B 的子类（或子类的子类）。

print(issubclass(KeyError, LookupError))

ex = KeyError('some message')

print(isinstance(ex,KeyError))