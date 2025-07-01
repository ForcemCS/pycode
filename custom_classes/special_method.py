# code 1
class Person:
    def __init__(self, name):
        self.name = name
        
    def __eq__(self, other):
        return self.name == other.name
    
p1 = Person('Wu kui') 
p2 = Person('Wu kui')

print(p1.__eq__(p2))
print(p1 == p2)

# code 2
import math 
 
class Circle:
    def __init__(self, radius):
        self.radius   = radius 
    
    def area(self):
        return math.pi * self.radius ** 2 
    #__str__ 这个特殊方法 必须返回一个字符串（string）类型
    def __str__(self):
        return str(self.radius)
        #return f"A circle with radius {self.radius}"
    
c = Circle(10)

print(c)


# code 3

from decimal import Decimal

a = Decimal('12.01')
print(str(a))

print(repr(a))



class Circle:
    def __init__(self, radius):
        self.radius   = radius 
    
    def area(self):
        return math.pi * self.radius ** 2 
    #__str__ 这个特殊方法 必须返回一个字符串（string）类型
    def __str__(self):
        return f'Circle({self.radius})'
    
    def __repr__(self):
        return f'Circle(radius={self.radius})'
    

b = Circle(10.11)

print(b)
print(repr(b))


# code 4

class Circle:
    def __init__(self, radius):
        self.radius   = radius 
    
    def area(self):
        return math.pi * self.radius ** 2 
    
    def __str__(self):
        return f'Circle({self.radius})'
    
    def __repr__(self):
        return f'Circle(radius={self.radius})'
    
    def __eq__(self, other):
        if isinstance(other , Circle):
            return self.radius == other.radius
        return False

a = Circle(10)
b = Circle(10)

print(a == b )   