# class的函数：1. 第一个参数，Python 会自动为你处理。它代表正在被创建的那个实例对象本身。你不需要为它提供值。2，第二个参数在没有默认值的情况下，这意味着，任何人在创建 Circle 对象时，必须 提供一个值。
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(actual_circle):
        ## !!! 关键点在这里：这个方法执行完 print 之后，没有 return 语句 ! 
        ## 在 Python 中，一个函数或方法如果没有明确的 return 语句，它会默认返回 None。
        print('area() called for instance :', actual_circle)
        
        
c = Circle(1).area()   #area() called for instance : <__main__.Circle object at 0x0000020A681B6900>

# print(c.radius)   此时会报错，没有任何属性


##code1

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(actual_circle):
        print('area() called for instance :', actual_circle)
        return actual_circle
        
c = Circle(1).area() 

print(c.radius)   ##此时返回的才是1