import math

#code 1
class Circle:
    def __init__(self, radius):
        if not (isinstance(radius, float) or isinstance(radius, int)):
            raise ValueError('radius must be is a float or an init')
        if radius < 0 :
            raise ValueError('radius cannot be negative')
        self.radius = radius
    
    def area(self):
        return math.pi * self.radius ** 2




#code 2
class Circle:
    def __init__(self, radius):
        if not (isinstance(radius, float) or isinstance(radius, int)):
            raise ValueError('radius must be is a float or an init')
        if radius < 0 :
            raise ValueError('radius cannot be negative')
        self._radius = radius
    @property    
    def radius(self):
        print('radius getter called ...')
        return self._radius + 1
    @property
    def area(self):
        print('area property called ...')
        #self.radius 表示调用radius 这个property的公共接口
        return math.pi * self.radius ** 2


a = Circle(10)
a._radius = 1
print(a.area,a._radius)
print('-' * 10 )



# code 3
class Circle:
    def __init__(self, radius):
        if not (isinstance(radius, float) or isinstance(radius, int)):
            raise ValueError('radius must be is a float or an init')
        if radius < 0 :
            raise ValueError('radius cannot be negative')
        self._radius = radius
    @property    
    def radius(self):
        print('radius getter called ...')
        return self._radius + 1
    @radius.setter
    def radius(self, value):
        print('radius setter called ...')
        if not (isinstance(value, float) or isinstance(value, int)):
            raise ValueError('radius must be is a float or an init')
        if value < 0 :
            raise ValueError('radius cannot be negative')
        self._radius = value
        
    @property
    def area(self):
        print('area property called ...')
        #self.radius 表示调用radius 这个property的公共接口
        return math.pi * self.radius ** 2
    
a = Circle(10)
a._radius = 10
print(a.area,a.radius)

a.radius = 10
print(a.area,a.radius)
print('-' * 10 )

# code 4

class Circle:
    def __init__(self, radius):
        #触发radius.setter
        self.radius = radius
    @property    
    def radius(self):
        print('radius getter called ...')
        return self._radius + 1
    @radius.setter
    def radius(self, value):
        print('radius setter called ...')
        if not (isinstance(value, float) or isinstance(value, int)):
            raise ValueError('radius must be is a float or an init')
        if value < 0 :
            raise ValueError('radius cannot be negative')
        self._radius = value
        
    @property
    def area(self):
        print('area property called ...')
        #self.radius 表示调用radius 这个property的公共接口
        return math.pi * self.radius ** 2
    
a = Circle(10)
a.radius = 9
print(a.area)
print('**' * 10 )
print(a.radius)