### 1. 列表推导式 (List Comprehensions)

列表推导式用于快速创建一个新的列表。

**基本语法：** `[表达式 for 元素 in 可迭代对象 if 条件]`

- `表达式`: 对每个元素进行的操作。
- `for 元素 in 可迭代对象`: 遍历可迭代对象（如列表、元组、字符串、range等）。
- `if 条件` (可选): 只有满足条件的元素才会被处理并加入新列表。

**例子1：生成一个包含0-9的平方的列表**

- **传统写法：**

  ```python
  squares = []
  for x in range(10):
      squares.append(x**2)
  print(squares)
  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

- **列表推导式写法：**

  ```python
  squares = [x**2 for x in range(10)]
  print(squares)
  # 输出: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
  ```

  这里，`x**2` 是表达式，`x` 是元素，`range(10)` 是可迭代对象。

**例子2：从一个列表中筛选出偶数，并计算它们的平方**

- **传统写法：**

  ```python
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  even_squares = []
  for num in numbers:
      if num % 2 == 0:
          even_squares.append(num**2)
  print(even_squares)
  # 输出: [4, 16, 36, 64, 100]
  ```

- **列表推导式写法：**

  ```python
  numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
  even_squares = [num**2 for num in numbers if num % 2 == 0]
  print(even_squares)
  # 输出: [4, 16, 36, 64, 100]
  ```

  这里，`num**2` 是表达式，`num` 是元素，`numbers` 是可迭代对象，`if num % 2 == 0` 是条件。

### 2. 集合推导式 (Set Comprehensions)

集合推导式和列表推导式非常相似，只是它创建的是一个集合 (set)

**例子：从一个包含重复元素的列表中，获取所有元素的平方，并确保结果中没有重复值**

- **传统写法 (结合set转换)：**

  ```python
  numbers = [1, 2, 2, 3, 4, 4, 5]
  unique_squares_list = []
  for num in numbers:
      unique_squares_list.append(num**2)
  unique_squares_set = set(unique_squares_list)
  print(unique_squares_set)
  # 输出: {1, 4, 9, 16, 25} (顺序可能不同)
  ```

- **集合推导式写法：**

  ```python
  numbers = [1, 2, 2, 3, 4, 4, 5]
  unique_squares_set = {num**2 for num in numbers}
  print(unique_squares_set)
  # 输出: {1, 4, 9, 16, 25} (顺序可能不同)
  ```

### 3. 字典推导式 (Dictionary Comprehensions)

字典推导式用于快速创建一个新的字典。语法上也是使用花括号 `{}`，但表达式部分是 `key: value` 的形式。

**基本语法：** `{键表达式: 值表达式 for 元素 in 可迭代对象 if 条件}`

**例子1：创建一个字典，键是0-4的数字，值是它们的平方**

- **传统写法：**

  ```python
  squared_dict = {}
  for x in range(5):
      squared_dict[x] = x**2
  print(squared_dict)
  # 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  ```

- **字典推导式写法：**

  ```python
  squared_dict = {x: x**2 for x in range(5)}
  print(squared_dict)
  # 输出: {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
  ```

  这里，`x` 是键表达式，`x**2` 是值表达式。

**例子2：从一个列表中创建字典，只包含长度大于3的字符串及其长度**

```python
words = ["apple", "bat", "cat", "dragonfruit", "egg"]
word_lengths = {word: len(word) for word in words if len(word) > 3}
print(word_lengths)
# 输出: {'apple': 5, 'dragonfruit': 11}
```

### 4. 生成器表达式 (Generator Expressions)

生成器表达式看起来和列表推导式非常相似，但它使用圆括号 `()` 而不是方括号 `[]`。
最大的区别在于：

- 列表推导式会立即计算所有元素并创建一个完整的列表，占用内存。
- 生成器表达式不会立即计算所有元素，而是返回一个**生成器对象 (generator object)**。这个对象在你迭代它的时候（例如在一个 `for` 循环中，或者使用 `next()` 函数）才会逐个计算并产生值。这使得生成器在处理大量数据时非常节省内存。

**基本语法：** `(表达式 for 元素 in 可迭代对象 if 条件)`

**例子：生成0-9的平方，但不立即创建列表**

- **没有直接的“传统写法”来完全模拟生成器的惰性求值，但可以想象一个函数使用 `yield`：**

  ```python
  def squares_generator_func(n):
      for i in range(n):
          yield i**2
  
  squares_gen_obj = squares_generator_func(10)
  # print(squares_gen_obj)  # 输出: <generator object squares_generator_func at 0x...>
  for val in squares_gen_obj:
      print(val, end=" ") # 0 1 4 9 16 25 36 49 64 81
  print()
  ```

- **生成器表达式写法：**

  ```python
  squares_gen_obj = (x**2 for x in range(10))
  print(squares_gen_obj) # 输出: <generator object <genexpr> at 0x...>
  
  # 迭代生成器以获取值
  for val in squares_gen_obj:
      print(val, end=" ") # 0 1 4 9 16 25 36 49 64 81
  print()
  
  # 或者一次获取一个值
  squares_gen_obj_2 = (x**2 for x in range(3))
  print(next(squares_gen_obj_2)) # 0
  print(next(squares_gen_obj_2)) # 1
  # print(next(squares_gen_obj_2)) # 4
  # print(next(squares_gen_obj_2)) # 会抛出 StopIteration 异常，因为没有更多元素了
  ```

  生成器表达式特别适合处理可能非常大的数据集，因为你不需要一次性把所有数据都加载到内存里。