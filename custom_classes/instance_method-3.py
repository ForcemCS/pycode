##code 1
from math import pi

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center = center_x, center_y
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def translate(self, x, y):
        self.center = (self.center[0] + x, self.center[1] + y)

    def scale(self, factor):
        self.radius *= factor
        

c = Circle(0, 0, 2)

print(c.center,c.radius)
print(c.area())
c.translate(1,-1)
print(c.center,c.radius)

c.scale(10)
print(c.radius)

print(c.area())

## code 2

file_name = 'DEXUSEU.csv'

import csv

with open(file_name) as f:
    reader  = csv.reader(f)
    header = next(reader)
    data = list(reader)[:5]

print(header,data,sep='\n')


from datetime import datetime

a = datetime.strptime('2025-06-30', '%Y-%m-%d')

print(a,a.date(),sep='\n')

## code3

from decimal import Decimal

class Forex:
    def  __init__(self, f_name):
        with open(f_name) as f:
            reader = csv.reader(f)
            
            self.header  = next(reader)
            self.data = [
                (
                    datetime.strptime(date, '%Y-%m-%d').date(),  Decimal(value)
                )
                for date, value in reader
                if  value != '.'
            ]

forex = Forex(file_name)

print(forex.data[:2])

print('-' * 20)

## code 4
from decimal import Decimal

class Datapoint:
    def __init__(self,date, value):
        self.date = date
        self.value = value

class Forex:
    def  __init__(self, f_name):
        with open(f_name) as f:
            reader = csv.reader(f)
            
            self.header  = next(reader)
            self.data = [
                
                Datapoint(
                    datetime.strptime(date, '%Y-%m-%d').date(),
                    Decimal(value)
                    )
                for date, value in reader
                if  value != '.'
            ]

forex = Forex(file_name)

print(forex.data[0].date)




##code 5 

class Datapoint:
    def __init__(self,date, value):
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.value = Decimal(value)
        
class Forex:
    def  __init__(self, f_name):
        with open(f_name) as f:
            reader = csv.reader(f)
            
            next(reader)            

            self.data = [ Datapoint(date,value) for date, value in reader if  value != '.' ]

forex = Forex(file_name)

print(forex.__dict__)


## code 6

class Datapoint:
    def __init__(self,date, value):
        self.date = datetime.strptime(date, '%Y-%m-%d').date()
        self.value = Decimal(value)
        
class Forex:
    def  __init__(self, f_name):       
        self.f_name  = f_name
        #{data: [列表对象]}
        self.data = self.process_data()
        
    def process_data(self):
        with open(self.f_name) as f:
            reader = csv.reader(f)
            next(reader)            
            return [ Datapoint(date,value) for date, value in reader if  value != '.' ]

forex = Forex(file_name)
#返回字典
print(forex.__dict__)
#返回List,列表中的对象由字典组成
print(forex.data)


print(forex.data[0].date)


for item in forex.data[:5]:
    print(item.date,item.value)