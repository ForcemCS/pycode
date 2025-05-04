#range对象本身是一个"惰性sequence"——它不会在创建时立即生成所有值，而是在需要时才生成
#对于非常大的范围请谨慎使用

r = range(2, 10, 2)

print(r)
print(list(r))
print(tuple(r))

print(tuple(range(5)))

print(list(range(2, 5)))

print(len(range(1, 3, 1)))