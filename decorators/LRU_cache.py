#函数执行的独立性与状态管理（记忆）
#我认为理解装饰器的重点是：函数的返回值可以来自于你构造的任一事务的结果
# 在 Python 中，LRU Cache 是一种缓存机制，其全称是 Least Recently Used Cache，即“最近最少使用缓存”。它的作用是缓存函数的结果，以避免重复计算，提高程序效率。
# 当缓存满了，需要删除旧数据时，会优先删除最久未被使用的缓存项。这样可以保证缓存中保留的是“最近常用”的数据。

# import time

# def fibonacci_no_cache(n):
#     """
#     一个没有缓存的斐波那契数列计算函数，模拟耗时操作。
#     """
#     print(f"正在计算 fibonacci_no_cache({n})...")
#     time.sleep(0.1) # 模拟耗时操作
#     if n <= 1:
#         return n
#     return fibonacci_no_cache(n-1) + fibonacci_no_cache(n-2)

# print("--- 未使用缓存的斐波那契 ---")
# start_time = time.time()
# print(f"fibonacci_no_cache(5) = {fibonacci_no_cache(5)}")
# end_time = time.time()
# print(f"耗时：{end_time - start_time:.4f} 秒\n")


# d = {'a': 1, 'b': 2}
# a= frozenset(d.items())

# print(type(a).__name__)

# for ele in a:
#     print(ele)

import time
import collections # 用于创建OrderedDict作为缓存，或者直接用字典也行

def cache_decorator(func):
    cache = {} 
    
    def wrapper(*args, **kwargs):
        key = (args, frozenset(kwargs.items()))

        if key in cache:
            print(f"从缓存中获取结果 {func.__name__}{key}...")
            return cache[key]
        else:
            print(f"计算中... {func.__name__}--{key}")
            result = func(*args, **kwargs)
            cache[key] = result
            return result
        
    return wrapper


@cache_decorator # 这行代码等同于 fibonacci_with_cache = cache_decorator(fibonacci_with_cache)
def fibonacci_with_cache(n):
    """
    一个带缓存的斐波那契数列计算函数。
    """
    time.sleep(0.1) # 模拟耗时操作
    if n <= 1:
        return n
    # 递归调用时，会再次经过装饰器，所以内部调用也会被缓存
    return fibonacci_with_cache(n-1) + fibonacci_with_cache(n-2)

print("\n--- 使用装饰器缓存的斐波那契 ---")

##第一次
start_time = time.time()
print(f"fibonacci_with_cache(5) = {fibonacci_with_cache(5)}")
end_time = time.time()
print(f"耗时：{end_time - start_time:.4f} 秒\n")
##第二次
start_time = time.time()
print(f"fibonacci_with_cache(5) = {fibonacci_with_cache(5)}") # 再次调用
end_time = time.time()
print(f"耗时：{end_time - start_time:.4f} 秒\n")
##第三次
start_time = time.time()
print(f"fibonacci_with_cache(6) = {fibonacci_with_cache(6)}") # 调用新的参数，会利用部分缓存
end_time = time.time()
print(f"耗时：{end_time - start_time:.4f} 秒\n")

fibonacci_with_cache = None # 此时，原来指向 wrapper 对象的引用消失，wrapper 引用计数变为 0，被回收。 进而，wrapper 内部对 cache 的引用也消失，cache 引用计数变为 0，被回收