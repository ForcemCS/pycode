## code 1
class Person:
    ##初始化阶段
    def __init__(self, name):
        self.name = name
    ##定义一个函数
    def say_hello(self):
        return f'Hello, {self.name}'

p = Person('Alex')
print(p.say_hello())

##code 2

# class Person:
#     def __init__(self, name):
#         self.name = name

#     def eat(self, food):
#         return f'{self.name} is eating {food.lower()}.'

# # p = Person("wu kui").eat("Broccoli")



class Person:
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print(f'{self.name} is eating {food.lower()}.')
        return self
# p 就代表着这个“名叫Alex的人”的对象。        
p = Person('Alex')  

# 让变量 p 所代表的那个对象去执行 eat 这个动作。
p.eat('Broccoli')
print(p.__dict__)       