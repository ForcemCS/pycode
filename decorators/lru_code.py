
#code1
def cache(func):
    cache_dict = {}
    print("缓存初始化中")
    def inner(*args):
        if args in cache_dict:
            print(f"缓存命中: {cache_dict}")
            return cache_dict[args]
        else:
            result = func(*args)
            print(f"没有发现缓存")
            cache_dict[args] = result
            print(f"缓存更新后: {cache_dict}")
            return result
            
    return inner
@cache                      #add = cache(add) 程序加载时，立即执行，也就时说立即打印"缓存初始化中"
def add(x,y):
    return x + y
print('-' * 10)

print(add(1,2))
print(add(1,2))

#code2

from functools import lru_cache

@lru_cache(maxsize=2)
def add_(a, b):
    print("called add ....")
    return a + b 
print('*' * 20 )
print(add_(5,6))
print(add_(5,6))   #这一次没有打印"called add ...."

print(add_(3,3))
print(add_(3,3))

print(add_(7,3))
print(add_(7,3))


print(add_(5,6))  #这次缓存被顶替掉了