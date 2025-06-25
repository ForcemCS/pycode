import statistics  as stati
data = ['one', 'two', 'three', 'three', 'four', 'four']

print(stati.multimode(data))



import random

random.seed(0)

data = [random.gauss(0, 2) for _ in range(10_000)]

print(stati.fmean(data), stati.median(data))
