# headers = ('i', 'fib' ,'fact', 'gcd')
# a = ','.join(headers)
# print(a)

##测试1
from functools import lru_cache
from math import factorial, gcd
@lru_cache
def fibonacci(n):        
    if n <= 1:
        return 1
    return fibonacci(n - 1) + fibonacci ( n - 2)


def fibonacci_correlation(n):
    with open('fi.txt', 'w') as f:
        f.write('i,fib,fact,gcd\n')
        for i in range(n + 1):
            x = fibonacci(i - 1) + fibonacci ( i - 2)
            y = factorial(i)
            z = gcd(x,y)
            a = ','.join((str(i),str(x),str(y),str(z)))
            a += '\n'
            f.write(a)

fibonacci_correlation(5)

#测试1
file_name = 'data.csv'

headers = ('i', 'fib' ,'fact', 'gcd')

n = 6

with open(file_name, 'w') as f:
    f.write(','.join(headers))
    f.write('\n')
    for i in range(n):
        data = [i,fibonacci(i), factorial(i), gcd(factorial(i), fibonacci(i))]
        row = ','.join(map(str, data))
        f.write(row)
        f.write('\n')
    

#测试2
file_name = 'data.csv'
with open(file_name) as f:
    next(f)  # skip header row
    data = [list(map(int, row.strip().split(','))) for row in f]
        
print(data[:6])


fib_stored = [row[1] for row in data]
fact_stored = [row[2] for row in data]
gcd_stored = [row[3] for row in data]

print(fib_stored, fact_stored, gcd_stored)