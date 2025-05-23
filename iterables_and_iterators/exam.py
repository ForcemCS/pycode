from timeit import timeit
from time import perf_counter

#测试1
l = [10, 'abc', 3.14, True]
for k,v in enumerate(l):
    print(f"Index :{k}, Value: {v} ")

#测试2
a= timeit("(d ** 2 for d in range(1, 10_001))", number=1)
print(f"{a:.9f}")

data = (d ** d for d in range(1, 10_001))

for _ in range(5):
    print(next(data))

g = (i ** i for i in range(1, 10_001))

for idx, value in enumerate(g):
    print(value)
    if idx == 4:
        break



start = perf_counter()

data = [d ** 2 for d in range(1, 10_001)]

c = 0 
while c < 5:
    print(data[c])
    c += 1
end = perf_counter()

print(f"elasped: {(end  - start):.9f}")


data = [1, 2, 3, 4, 5, 6]

for  _ in range(10):
    for i in data[:5]:
        print(i)
    print("-----")