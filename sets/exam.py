l = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']

print(list(set(l)))

l_s = set()
for i in  l:
    print(i)
    l_s.add(i.upper())
print(l_s)





data = {
    'd1': {'a': 1, 'b': 2, 'c': 3},
    'd2': {'b': 20, 'c': 30, 'd': 40},
    'd3': {'d': 100, 'x': 200}
}


a = set()
for k ,v in data.items():
    a = a | set(v)
print(a)
print('-' * 10)


b = {12,13,14,15,16,17,18,19,123,43,24,5,65,324,231,4,324721,32,13123,123,21,2223,222213}
value  = 0
for i in b:
    value += 1
    if  value <=  10:
        print(i)


l = ['AAPL', 'AAPL', 'Aapl', 'aapl', 'MSFT']

#结合推导式 { 表达式 for 变量 in 可迭代对象 }
unique_values = {symbol.casefold() for symbol in l}     
print(unique_values)

##list推导式
squares = [x * x for x in range(10)]
print(squares)

##字典推导式
d = {f"{x} * {x}" : x*x for x in range(5)}
print(d)