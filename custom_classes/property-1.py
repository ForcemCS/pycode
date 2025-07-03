#1. Read-Only Property (只读属性)
import math

class Circle:
    def __init__(self, radius):
        self._radius = radius  # 内部存储半径

    # 1. 定义一个名为 area 的方法
    # 2. 在上面加上 @property 装饰器
    @property
    def area(self):
        """这是一个 getter 方法，用于计算和返回面积"""
        print("(Calculating area...)") 
        return math.pi * (self._radius ** 2)

# --- 使用 ---
c = Circle(10)

# 访问 area 就像访问一个普通的属性
# 但实际上，它在背后调用了 area() 方法
print(f"The radius is 10, the area is: {c.area}")

# 再次访问，会再次调用方法
print(f"The area is still: {c.area}")

# 尝试修改 area 会失败，因为它没有 setter
try:
    c.area = 300
except AttributeError as e:
    print(f"\nError when trying to set area: {e}")
    
# 2.Read/Write Property (读/写属性)
class Person:
    def __init__(self, name):
        # __init__ 方法也会调用 setter！
        # self.name = name 这行代码会触发下面的 name.setter 方法
        self.name = name

    # --- Getter ---
    @property
    def name(self):
        """这是 getter，当读取 p.name 时调用"""
        print(f"(Getter called for '{self._name}')...")
        return self._name

    # --- Setter ---
    # 装饰器必须是 @<getter方法名>.setter
    @name.setter
    def name(self, value):
        """这是 setter，当执行 p.name = '...' 时调用"""
        print(f"(Setter called with value '{value}')...")
        if not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("Name must be a non-empty string")
        # 如果验证通过，就把值存到内部变量 _name 中
        self._name = value.strip()

# --- 使用 ---
print("Creating person ' Alex '...")
p = Person("  Alex  ")  # 注意名字前后的空格

print("\nReading name:")
print(f"Person's name is: {p.name}") # 调用 getter

print("\nTrying to set an invalid name:")
try:
    p.name = "" # 调用 setter，但会失败
except ValueError as e:
    print(f"Error: {e}")

print("\nSetting a new valid name:")
p.name = "Bob" # 调用 setter，成功
print(f"Person's new name is: {p.name}") # 调用 getter


#3. Calculated Property (计算属性)
#   它的值不是简单地从一个内部变量返回，而是通过一系列计算动态生成的

from datetime import date

class Person:
    def __init__(self, name, birthdate):
        self.name = name
        self._birthdate = birthdate # 存储出生日期

    @property
    def age(self):
        """一个计算属性。它没有对应的 _age 变量。"""
        print("(Calculating age...)")
        today = date.today()
        # 计算年龄的简单逻辑
        age = today.year - self._birthdate.year - ((today.month, today.day) < (self._birthdate.month, self._birthdate.day))
        return age

# --- 使用 ---
# 创建一个出生在 1990年5月20日的人
p = Person("Charlie", date(1990, 5, 20))

# 访问 age 属性，它会动态计算
print(f"{p.name}'s age is: {p.age}")

# 再次访问
print(f"{p.name}'s age is still: {p.age}")

# 这个属性是只读的，因为设置年龄没有意义（应该修改出生日期）
try:
    p.age = 40
except AttributeError as e:
    print(f"\nError: {e}")