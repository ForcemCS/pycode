# factorial(n)        → 阶乘函数
# perm(n, k)          → 有序排列
# comb(n, k)          → 无序排列  
# gcd(a, b)           → 最大公约数
# sqrt(x)             → 平方根
# exp(x)              → 指数函数

# fsum(iterable)      高精度浮点数求和
#     作用：对一个可迭代对象（如列表）中的所有浮点数进行求和。它比内置的 sum() 函数更精确，因为它能避免因浮点数累加而导致的精度损失。
  
# prod(iterable, *, start=1) → 连乘积
#     print(math.prod([1, 2, 3, 4]))        # 输出: 24 (1*2*3*4)
#     print(math.prod([1, 2, 3, 4], start=5)) # 输出: 120 (5*1*2*3*4)
  
# dist(p, q) → 欧几里得距离
#     作用：计算两个点 p 和 q之间的欧几里得距离。p 和 q 都是坐标的迭代对象（如列表或元组）。
#     p = [0, 0]
#     q = [3, 4]
#     print(math.dist(p, q))  # 输出: 5.0 
  
# hypot(*coords) → 欧几里得范数 (向量长度)
#   计算一个从原点到指定坐标点的向量的长度。这等同于 sqrt(x*x + y*y + ...)。
  
# log(x, [base]) → 对数
#     作用：计算 x 的对数。如果不提供第二个参数 base，则计算自然对数（以 e 为底）。
#     示例：
#     print(math.log(math.e))    # 自然对数，输出: 1.0
#     print(math.log(100, 10))   # 以 10 为底，输出: 2.0
    
# degrees(x), radians(x) → 角度/弧度转换
#     作用：degrees(x) 将 x 从弧度转换为角度；radians(x) 将 x 从角度转换为弧度。
#     示例：
#     print(math.degrees(math.pi))   # π 弧度等于 180 度，输出: 180.0
#     print(math.radians(180))     # 180 度等于 π 弧度，输出: 3.14159...
    
# sin(x), cos(x), tan(x) → 正弦、余弦、正切
#     作用：计算 x (以弧度为单位) 的三角函数值。
#     示例：计算 90 度的正弦值。
#     angle_rad = math.radians(90) # 先转换为弧度
#     print(math.sin(angle_rad))   # 输出: 1.0