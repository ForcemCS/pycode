## Python Dictionary
+ 字符串是不可变的，所以它们是可哈希的
  ```
  my_dict = {'name': 'Alice', 'age': 30}
  ```
+ 数字（整数、浮点数）也是不可变的，所以它们是可哈希的
  ```
  my_dict = {1: 'one', 3.14: 'pi'}
  ```
+ 元组 (tuple) 本身是不可变的。但它能否作为键，取决于它里面的元素是否也都是可哈希的。
  ```
  my_dict = {(1, 'a'): 'value1'} #  OK
  # my_dict = {([1, 2], 'a'): 'value2'} #  Error! list is not hashable
  ```
+ 在 Python 中，几乎所有的东西都是对象。这句话是说，字典的键和值都可以是任何 Python 对象，比如数字、字符串、列表、甚至其他字典等等,但对键的类型有限制，。
  + 键必须是不可变的类型，这样才能计算出它的哈希值，用于快速查找。
  + 在一个字典中，每个键必须是独一无二的。你不能有两个相同的键。如果尝试用一个已经存在的键赋新的值，那么原来的值会被覆盖。
  + 与键不同，字典的“值”可以是任何 Python 数据类型，包括可变的类型（如列表、其他字典）或不可变的类型。
  + 字典不是序列类型（但是按插入顺序排序的。），像列表 (list) 和元组 (tuple) 这样的类型是序列类型。它们的主要特点是有序，并且可以通过数字索引 (0, 1, 2, ...) 来访问元素。
  + 字典是可变的，字典在创建之后可以被修改。你可以添加新的键值对，删除已有的键值对，或者修改已有键对应的值。
  

## 创建字典的其他方法

`dict.fromkeys(iterable, value)` 是 Python 提供的一个类方法，用于**创建一个新字典**，其中：

- 所有的键来自于给定的可迭代对象（如列表、元组、字符串等）；
- 所有的值都被初始化为指定的同一个值（默认为 `None`）。

```
d = dict.fromkeys(['cnt_1', 'cnt_2', 'cnt_3'], 0)
##返回{'cnt_1': 0, 'cnt_2': 0, 'cnt_3': 0}
```

```
d = dict.fromkeys('abc', 100)
##这里的 'abc' 是一个字符串，也可以看作是一个可迭代对象，它会被拆成字符 'a'、'b'、'c'：
```

🧠 注意事项：

1. 可迭代对象必须是**可遍历的**：如 `list`、`tuple`、`str`、`range()` 等。
2.  如果你传的是**可变对象**作为值（如 `list`、`dict`），所有键会**共享**同一个对象：

```
python复制编辑d = dict.fromkeys(['x', 'y'], [])
d['x'].append(1)
print(d)  # {'x': [1], 'y': [1]} ⚠️ 值是共享的！
```

## 将一个字典合并到另一个字典中

**注意插入顺序！！不会改变被更新字字典的顺序**

```
d1.update(d2)
```

🧩 合并的具体规则：

1. **如果 `d2` 中的键不在 `d1` 中：**
   - 会被直接添加到 `d1`，带着它自己的值。
2. **如果 `d2` 中的键已经在 `d1` 中存在：**
   - 会**覆盖 `d1` 中原来的值**，也就是说，以 `d2` 中的值为准。

⚠️ 注意：`d1` 会被“修改”（mutated）

- 合并是直接在 `d1` 上进行的，`d1` 的内容会被改变。
- `update()` 不会返回新的字典，而是**就地修改**原始字典。

我们可以使用d.copy()进行浅拷贝

```python
d1 = {'name': 'Alice', 'age': 25}
d2 = {'age': 30, 'gender': 'female'}

# 创建一个新字典，不改变 d1
merged = d1.copy()
merged.update(d2)

print(merged)
```

