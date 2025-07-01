### 状态与行为的封装

**封装**意味着将两样东西打包在一起：

1. **数据 (Data / State)**：对象是什么。
2. **操作数据的函数 (Functions / Behavior)**：对象能做什么。

```python
from math import pi

class Circle:
    def __init__(self, center_x, center_y, radius):
        self.center = center_x, center_y
        self.radius = radius

    def area(self):
        return pi * self.radius ** 2

    def translate(self, x, y):
        self.center = (self.center[0] + x, self.center[1] + y)

    def scale(self, factor):
        self.radius *= factor
```

1. `__init__`：设置对象的初始状态 (Initial State)

```python
def __init__(self, center_x, center_y, radius):
    self.center = center_x, center_y
    self.radius = radius
```

- 当你创建一个 `Circle` 实例时（例如 `c = Circle(10, 20, 5)`），`__init__` 就会运行。
- 它的工作是接收外部数据（`10, 20, 5`），并用这些数据来定义这个**全新对象**的**初始状态**。
- 从此，这个圆就“知道”了它的圆心是 `(10, 20)`，半径是 `5`。这就是它的**状态**。

2. `area`：一个“只读”的行为 (Read-Only Behavior)

```python
def area(self):
    return pi * self.radius ** 2
```

- 这个方法代表了圆的一种**行为**：计算自己的面积。
- 这是一个“**查询 (Query)**”方法。它**读取**对象的当前状态（`self.radius`），进行计算，然后返回一个结果。
- **关键是：它不会改变对象的状态。** 调用 `c.area()` 一百万次，圆的半径和圆心都不会有任何变化。

3. `translate` 和 `scale`：“可写”的行为 (Mutator Behavior)

```python
def translate(self, x, y):
    self.center = (self.center[0] + x, self.center[1] + y)

def scale(self, factor):
    self.radius *= factor
```

- 这两个方法也代表了圆的**行为**：移动自己和缩放自己。
- 这些是“**修改 (Mutator)**”或“命令 (Command)”方法。它们接收一些指令（移动多少，缩放多少），然后用这些指令来**直接修改对象自身的状态**。
- 调用 `c.translate(2, 3)` 后，`c` 这个对象的状态就**永久地改变了**（它的 `self.center` 被更新了）。
- 调用 `c.scale(2)` 后，`c` 的 `self.radius` 也被更新了。

### 类即蓝图 (Classes as Blueprints)

1. **类通常被称为创建对象的蓝图 (classes are often referred to as blueprints for creating objects)**
   - 一个**类**本身不是一个对象，它是一个定义，说明如何创建特定类型的对象。
2. **一个单一的类可以用来创建该类的许多实例 (a single class can be used to create many instances of that class)**
   - 你可以用同一张蓝图建造许多栋房子。
   - 同样，你可以用同一个**类**（如 `Person` 类）创建许多个**实例**（如 `john` 和 `eric` 这两个对象）。
3. **“每个实例都将有它自己的状态” (each instance will have it's own state)**
   - 用同一张蓝图建造的每栋房子都是独立的。你可以把一栋房子漆成红色，另一栋漆成蓝色。它们的“颜色”就是它们各自的“状态”。
   - 同样，每个由 `Person` 类创建的实例都是独立的对象。`john` 对象的状态（姓名是 'John Cleese'）和 `eric` 对象的状态（姓名是 'Eric Idle'）是完全分开的。
4. **在类中定义的函数成为绑定到实例的方法 (the functions defined in the class become methods bound to the instance)**
   - 这是关键点。当你在一个类里面定义一个函数时，比如 `greet()`，它本身只是一个通用的指令。
   - 但是，当你通过一个具体的实例来调用它（如 `john.greet()`）时，这个函数就变成了**方法 (method)**，并且它被**绑定 (bound)** 到了 `john` 这个实例上。
   - 因为这些函数被绑定到实例上(because these functions are bound to the instance)
     - 它们可以访问该实例的状态 (they can access the state of the instance)
       - 这就是绑定的真正意义。因为 `greet()` 方法在被 `john` 调用时是与 `john` 绑定的，所以它能够访问并使用 `john` 内部的状态（比如他的名字）。

### 自定义类 (Custom Classes)

1. 我们可以定义我们自己的自定义类型（类）
   + 我们不局限于 Python 内置的 `list`, `str`, `int` 等类型。我们可以通过定义一个**类 (class)** 来创建一个全新的数据类型。例如，我们可以创建一个 `Car` 类、一个 `Dog` 类或一个 `BankAccount` 类。
   + **类 (Class)** 本质上是创建对象的**蓝图**或**模板**。
2. **当我们使用自定义的类（蓝图）创建一个具体的对象（实例）时，这个实例会具备以下属性：**
   + **类型 (a type)**: 它的类型就是我们创建的那个自定义类。例如，如果我们用 `Car` 类创建了一个 `my_car` 对象，那么 `my_car` 的类型就是 `Car`。
   + **状态 (some state)**: 我们可以为每个实例存储特定的值。例如，一个 `Car` 实例的状态可以是它的颜色 `color='red'` 和型号 `model='Tesla Model 3'`。
   + **功能 (functionality)**: 这些是绑定到实例上的函数，称为**方法 (methods)**。例如，`Car` 类可以定义一个 `start_engine()` 方法。当你对一个具体的 `Car` 实例调用 `my_car.start_engine()` 时，这个操作是针对 `my_car` 这个特定对象的。

### 初始化器 (Initializers)

1. **初始化的需求**
   - 当我们创建一个类的新**实例**时，我们通常希望立即为它设置一个初始**状态**。例如，创建一辆车时，我们希望马上就指定它的颜色和型号，而不是创建一个“空”车，然后再去设置。
   - 这个在创建对象时就设置其初始状态的过程，被称为**初始化阶段 (initialization phase)**。
   - 这通常是通过在创建对象时传递**参数 (arguments)** 来完成的。

1. **创建和初始化的过程**
   - 创建过程是通过**调用类**（就像调用一个函数一样）来启动的。
   - 示例: `a = tuple([1, 2, 3])`
     - 我们正在调用 tuple 类（使用()）, 这里 `tuple` 是一个类（类型）。通过在它后面加上括号 `()`，我们就在“调用”它，意图创建一个它的新实例。
     - 向它传递一个参数：[1, 2, 3], 列表 `[1, 2, 3]` 就是我们传递给初始化过程的数据。
     - **结果**: 这个调用会返回一个全新的 `tuple` 实例，并且这个实例已经被**初始化**了，它的状态就是包含了元素 `1`, `2`, `3`。

初始化是一个在对象被创建时运行的特殊机制，它接收外部传入的参数，并用这些参数来设定该对象的初始状态。这个过程让我们能够方便地创建出“一出生就准备好”的、具有完整初始状态的对象。

