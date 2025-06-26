import decimal
import math
from decimal   import Decimal
from datetime import datetime


##code1
a = Decimal('0.1') * 3
print(type(a).__name__)

print(decimal.getcontext())

##code2

print(round(Decimal('1.345'), 2))
print(round(Decimal('1.355'), 2))


##code3
d1  = Decimal('2')

result = math.sqrt(d1)
print(type(result).__name__,result)

print(d1.sqrt())

##code4

f_name = 'DEXUSEU.csv'

with open(f_name) as f:
    for _ in range(5):
        print(next(f).strip())

import csv

with open(f_name) as f:
    reader  = csv.reader(f)
    for _ in range(5):
        print(next(reader))
        
##code5
#是一个迭代器对象
a = (x * 2 for x in range(5))
print(next(a),next(a))  #0 2
print(tuple(a))         # 4 6 8 



dt_format = "%Y-%m-%d"
a = datetime.strptime("2025-06-26",dt_format)

print(type(a).__name__)  #datetime.datetime 对象



def load_data(f_name,dt_format,use_decimal=False):
    with open(f_name) as f:
        reader = csv.reader(f)
        next(reader)
        
        data = [
            (
                datetime.strptime(row[0],dt_format), Decimal(row[1]) if   use_decimal else float(row[1])
            )
            for row in reader 
            if row[1] != '.'
        ]
        
        return data
    
dt_format = "%Y-%m-%d"

data_float = load_data(f_name,dt_format)
#print(data_float[:3])
print(format(data_float[0][1], '.28f'))

data_decimal = load_data(f_name,dt_format,use_decimal=True)
#print(data_decimal[:3])
print(format(data_decimal[0][1], '.28f'))

from time import perf_counter

start = perf_counter()

for _ in range(10_000):
    result = sum(row[1] for row in data_float)

end = perf_counter()

print(end - start, result)


start = perf_counter()

for _ in range(10_000):
    result = sum(row[1] for row in data_decimal)

end = perf_counter()

print(end - start,result)