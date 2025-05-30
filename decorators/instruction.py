# 装饰器的实现严重依赖于这两个特性：
# 1. 函数可以作为参数传递，也可以作为返回值返回：
#    装饰器本身就是一个函数（或类，但我们先关注函数装饰器）。
#    这个装饰器函数会接收另一个函数（你想装饰的那个函数）作为它的参数。
#    装饰器函数通常会返回一个新的函数(闭包函数)
# 2. 闭包（Closure）：
#    在装饰器中，内部的 wrapper 函数能够“记住”并访问外部装饰器函数作用域中的变量，即使外部函数已经执行完毕。最典型的就是，wrapper 函数能够“记住”它需要调用的原始函数 func_to_decorate。

##阶段一
def say_whee():
    print("Whee!")

# 现在我们想装饰 say_whee，在它执行前后打印信息
# 1. 定义一个“装饰器函数”，它接受一个函数作为参数
def my_decorator_function(func_to_decorate):
    # 2. 定义一个closure函数
    def wrapper_function():
        print(">>> Something is happening before the function is called.")
        func_to_decorate() # 调用原始函数
        print(">>> Something is happening after the function is called.")
    # 3. 装饰器函数返回包装函数
    return wrapper_function

# 4. 手动“装饰” say_whee
decorated_say_whee = my_decorator_function(say_whee)

# 5. 调用被装饰后的函数
decorated_say_whee()



##阶段二

def my_decorator_function(func_to_decorate):
    ##这个闭包中引用了原函数
    def wrapper_function():
        print(">>> (Using @) Something is happening before the function is called.")
        func_to_decorate()
        print(">>> (Using @) Something is happening after the function is called.")
    return wrapper_function

#@my_decorator_function 放在 def say_hello(): 的上方，就自动完成了 say_hello = my_decorator_function(say_hello) 这个赋值操作。say_hello 这个名字现在指向的是 wrapper_function。
@my_decorator_function # 这行等价于 say_hello = my_decorator_function(say_hello)
def say_hello():
    print("Hello!")

say_hello() # 直接调用，它已经是被装饰后的版本了


##阶段三
def decorator_with_args_and_return(func):
    # @functools.wraps(func) # 推荐使用，后面解释
    def wrapper(*args, **kwargs): # 接收任意位置参数和关键字参数
        print(f"--- Calling function: {func.__name__} ---")
        print(f"--- Arguments: {args}, {kwargs} ---")
        result = func(*args, **kwargs) # 调用原始函数并传递参数
        print(f"--- Function {func.__name__} returned: {result} ---")
        return result # 返回原始函数的执行结果
    return wrapper

# def greet_person(name, age):
#     greeting = f"Hello {name}, you are {age} years old."
#     return greeting

# a = decorator_with_args_and_return(greet_person)
# print(a('Wu Kui', 30))
# 等价于下边的写法
@decorator_with_args_and_return
def greet_person(name, age):
    greeting = f"Hello {name}, you are {age} years old."
    return greeting
@decorator_with_args_and_return
def add_numbers(a, b, c=0):
    return a + b + c

message = greet_person("Bob", 30)
print(f"Final message: {message}\n")

sum_result = add_numbers(10, 20)
print(f"Final sum: {sum_result}\n")

##阶段四
import functools

def log_decorator(func):
    @functools.wraps(func) # 使用 functools.wraps 来保留被装饰函数的元信息
    def wrapper(*args, **kwargs):
        print(f"LOG: 正在调用函数 ➡️ {func.__name__}")
        result = func(*args, **kwargs)
        print(f"LOG: 函数 {func.__name__} 执行完毕 ✅")
        return result
    return wrapper

@log_decorator
def greet(name):
    """decorarot初始。"""
    print(f"Hello, {name}!")
    return f"Greetings to {name}"

print(greet(name="Alice"))

print(f"函数名: {greet.__name__}") # 正常情况下会是 'wrapper'，有了 wraps 则是 'greet'
print(f"文档字符串: {greet.__doc__}") # 正常情况下会是 None，有了 wraps 则是 'decorarot初始'