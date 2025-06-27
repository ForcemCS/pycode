# class Circle:
#     """Circle class"""

# def create_circle(radius):
#     #创建一个Circle实例
#     c = Circle()
#     #为实例初始化
#     c.radius = radius
#     #返回初始化的实例
#     return c
    
# c1 = create_circle(10)
# print(c1)

##code 1
class Circle:
    def create_circle(radius):
        c = Circle()
        c.radius = radius
        return c

c1 = Circle.create_circle(10)
print(c1.radius)

##code 2
# 使用 __init__ 初始化器 (Python 的标准方式)
class Circle:
    # 这是 Python 的特殊初始化方法，也叫构造方法
    # self 代表的正是那个正在被创建的实例对象本身。
    def __init__(self, radius):
        # 把传入的 radius 值，赋给 我自己(self) 的 radius 属性
        self.radius = radius * 2

# 如何使用：直接调用类名(),在创建的那一刻就有了初识状态
# 成功创建并返回了一个实例之后，Python 会立即拿着这个新实例去调用 __init__ 方法。
# __init__ 的工作只是在原地修改 self 对象，而不是创建一个新对象，所以它不应该（也不能）返回任何东西。
c2 = Circle(10)
print(c2.__dict__)
print(c2.radius) # 输出 20


# 重要！！！：在 Python 中，__init__ 方法的唯一工作是初始化一个已经被创建好的对象（即设置它的初始属性），它绝不能返回任何值（除了 None）
##code 3 
class Persion:
    def __init__(self):
        print("custom init ...")

Persion()


class Persion:
    def __init__(self):
        print("custom init ...",self)

p1 = Persion()

print(hex(id(p1)))

#为特定的实例增加新的属性
p1.first_name = "wu"
p1.last_name = "kui"

print(p1.__dict__)

#改进上边的代码
class Person:
    def __init__(self, first, last):
        print(f"正在初始化一个 Person 对象...")
        # 直接在 __init__ 内部，使用 self 来设置属性
        self.first_name = first
        self.last_name = last

# 创建实例时，直接提供所需的初始值
p1 = Person("wu", "kui")

# 此时，对象一创建好就已经拥有了所有必要的属性
print(p1.__dict__)




##  code4 
class Point:
    def __init__(self, *coords):
        self.coordimates = coords
        print(f"demension : {len(coords)}")
        
p = Point(1, 2, 3)


## code 5 

class Circle:
    def __init__(self, *, radius= 1 ):
        self.radius = radius
        
c = Circle()
#返回对象的属性字典
print(vars(c))



## code 6
class Circle:
    def __init__(self, *, radius= 1 ):
        if radius <= 0:
            raise ValueError('Radius must be positive')
        self.radius = radius
        
c = Circle(radius=-1)
