# 1. 导入库
import matplotlib.pyplot as plt
import numpy as np # 通常和 matplotlib 一起使用，方便创建数据

# 2. 准备数据
x = np.linspace(0, 10, 100) # 生成从0到10的100个点
y1 = np.sin(x)
y2 = np.cos(x)

# 3. 创建 Figure 和 Axes (准备画板和画布)

fig, ax = plt.subplots()

# 4. 在 Axes 上绘图 (在画布上画画)

ax.plot(x, y1, label='Sine Wave')      # 画第一条线，并给它一个标签
ax.plot(x, y2, label='Cosine Wave')    # 在同一个画布上画第二条线，并给它一个标签

# 5. 设置 Axes 的属性 (美化画布)
# 这就是第四张幻灯片的内容
ax.set_title("Sine and Cosine Waves")   # 设置标题
ax.set_xlabel("X-axis")                 # 设置x轴标签
ax.set_ylabel("Y-axis")                 # 设置y轴标签
ax.legend()                             # 显示图例

# 6. 显示图形 (在 Jupyter 中此步可省略)
plt.show()



# import matplotlib.pyplot as plt
# import numpy as np

# # =======================================================
# # 解决中文显示问题的关键代码
# plt.rcParams['font.sans-serif'] = ['SimHei']  # 指定默认字体为黑体
# plt.rcParams['axes.unicode_minus'] = False    # 解决保存图像是负号'-'显示为方块的问题
# # =======================================================


# # --- 实验 1: 只用 10 个点 ---
# x_few = np.linspace(0, 10, 10) # 在0到10之间只取10个点
# y_few = np.sin(x_few)

# # --- 实验 2: 使用 100 个点 (原始代码) ---
# x_many = np.linspace(0, 10, 100) # 在0到10之间取100个点
# y_many = np.sin(x_many)

# # 创建一个包含两个子图的 Figure，方便对比
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4)) # 1行2列的画布

# # 在第一个子图上画 10 个点的结果
# ax1.plot(x_few, y_few, 'o-') # 'o-' 样式会同时显示点和线
# ax1.set_title("10 Points (明显的折线)")

# # 在第二个子图上画 100 个点的结果
# ax2.plot(x_many, y_many, 'o-') # 为了看的清楚，我们也标记出点
# ax2.set_title("100 Points (看起来平滑)")

# plt.show()