### 1. 超越均匀分布：不同的概率分布

`random.randint(1, 10)`，每个数字（1到10）被选中的概率是完全相同的（都是1/10）。这叫**均匀分布 (Uniform Distribution)**。

但在现实世界中，很多事情的发生概率并不是均等的。

- 比喻： 想象一下全班同学的身高。身高特别高（比如2米）和特别矮（比如1米4）的人都很少，大部分人的身高都集中在平均值（比如1米7）附近。这就是**正态分布 (Normal Distribution)**，也叫“钟形曲线”或“高斯分布”。

Python的`random`模块可以模拟这些现实世界中的概率分布。

- **`random.uniform(a, b)`**: 生成一个a到b之间的浮点数，均匀分布。
- **`random.gauss(mu, sigma)`**: 生成一个符合正态分布的随机数。`mu`是平均值，`sigma`是标准差（代表数据的离散程度）。
- 还有很多其他分布，用于模拟不同的场景。

### 2. 打乱一个序列

将一个列表（list）中的元素顺序完全随机地打乱。

- 比喻： 就和洗牌一模一样。你有一副排好序的扑克牌，`random.shuffle()` 就相当于帮你把这副牌彻底洗开。

**重要特点：** `shuffle` 是**就地修改 (in-place)** 的，它不会返回一个新的列表，而是直接改变你给它的那个原始列表。

```python
import random

cards = ['A', 'K', 'Q', 'J', 10, 9, 8, 7, 6, 5, 4, 3, 2]
print("洗牌前:", cards)

random.shuffle(cards) # 就地洗牌，cards本身被改变

print("洗牌后:", cards)
```

### 3. 随机抽样 (Random Sampling)

这是从一个大的群体中随机抽取一部分样本。它分为两种情况：

#### 无放回抽样 (Without Replacement)

```python
import random

players = ['张三', '李四', '王五', '赵六', '孙七', '周八']
# 从6个玩家中随机选出3个组成一队
team = random.sample(players, 3) # 从players里无放回地抽3个

print("所有玩家:", players) # 原列表不变
print("被选中的队伍:", team)
```

####  有放回抽样 (With Replacement)

```
import random

dice_faces = [1, 2, 3, 4, 5, 6]
# 模拟掷两次骰子，k=2代表抽两次
rolls = random.choices(dice_faces, k=2) # 从dice_faces里有放回地抽2个

print("两次掷骰子的结果:", rolls)

# 多运行几次，你可能会看到 [6, 6] 或 [3, 3] 这样的结果
```

