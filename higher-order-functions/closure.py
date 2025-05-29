def make_adder(x):
    """
    这是一个外部函数，它接受一个参数 x。
    这个函数会创建一个并返回一个内部函数。
    """
    print(f"make_adder 被调用了，x 的值是: {x}")

    def adder(y):
        """
        这是一个内部函数，它接受一个参数 y。
        这个函数会使用外部函数 make_adder 定义的 x。
        """
        print(f"  adder 被调用了，y 的值是: {y}")
        return x + y # 内部函数 'adder' 引用了外部函数的 'x'

    return adder # 外部函数返回了内部函数 'adder' 的引用

#现在我们使用上边的函数
#1.创建第一个闭包
# 当我们调用 make_adder(5) 时：
#   - make_adder 执行，x 被赋值为 5。
#   - 它定义了内部函数 adder。
#   - 最后，它返回了这个内部函数 adder 的引用。
#   - 此时，make_adder 已经执行完毕了，但 adder 函数“记住”了 x=5 这个环境。
add_five = make_adder(5)
print("--- make_adder(5) 执行完毕 ---")

# 2. 使用这个闭包
# 此时，add_five 实际上就是那个记住 x=5 的 adder 函数。
print(f"add_five 的类型是: {type(add_five)}")
result1 = add_five(3) # add_five(3) 实际上是 adder(3)，其中 x 仍然是 5
print(f"结果 1: {result1}") # 输出: 8 (5 + 3)
result2 = add_five(4) 
print(f"结果 2: {result2}") 
##闭包的动机：
# 1. 数据封装和隐藏 (Data Encapsulation & Hiding):
#    闭包允许你将一些数据（外部函数的局部变量）“私有化”给一个函数使用，而不需要将这些数据暴露为全局变量或类属性。
#    在上面的例子中，x 的值被封装在 add_five 或 add_ten 这个“特殊”的 adder 函数内部，外部无法直接访问这个 x，只能通过调用 add_five 或 add_ten 来间接影响它。这有助于防止数据被意外修改。
# 2. 创建函数工厂 (Function Factories) / 动态生成函数:
#    闭包提供了一种非常灵活的方式来动态地创建和定制函数。你可以编写一个“工厂函数”（外部函数），根据不同的输入参数，生成功能相似但行为略有不同的函数。
#    make_adder 就是一个函数工厂，它可以根据你传入的 x，生成 add_five、add_ten 等各种“加法器”函数。这样就避免了为每个固定数值编写一个单独的加法函数。
# 3.维持状态 (Maintaining State) (不使用类):
def make_counter():
    count = 0 # 外部函数的局部变量

    def counter_func():
        nonlocal count # 声明这是一个外部作用域的变量
        count += 1
        return count
    return counter_func


#第一次创建执行环境，由于counter_func一直引用着count这个变量，所以一直没有被销毁
#只要有函数（闭包）引用着外部作用域的变量，外部作用域就不会被垃圾回收机制清除。
my_counter = make_counter() 
print(my_counter()) # 输出: 1
#上一次执行后，所引用的外部的作用域的count变为了1
#再次执行的时候，还时上次的环境，
print(my_counter()) # 输出: 2
another_counter = make_counter() # 独立的新计数器
print(another_counter()) # 输出: 1