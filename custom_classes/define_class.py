# class → Circle
#       → state: radius
#       → functionality: area(), perimeter()
      
# circle_1 → Circle(radius = 1)
# circle_2 → Circle(radius = 2)

# c1.radius = 10  -> 一旦有了一个实例（如 c1），你就可以动态地给它添加属性 (attributes)，这些属性就是实例的状态 (state)。
#                     之后你可以通过 print(c1.radius) 来获取这个属性的值。

# 创建并初始化一个 Circle 实例
# c1 = Circle(): 首先，创建一个 Circle 类的“空”实例。
# c1.radius = 10: 然后，手动为这个 c1 实例添加 radius 属性并赋值。这两步合起来完成了对 c1 的创建和初始化。
# 每个 Python 实例都有自己独立的命名空间，用来存储它独有的属性。这就是为什么给 c1 设置的 radius 不会影响到另一个 Circle 实例 c2 的原因。

class Persion:
    """This string can be  used to document this class -
    called a docstring
    """

##code 1    
p1 = Persion()
print(p1)
print(p1.__doc__)
print(type(p1).__name__)

a = p1.__class__  is Persion
print(a)

print(isinstance(p1, Persion)) 


#code2
p1.first_name = "wu"
p1.last_name  = "kui"

print(p1.__dict__)