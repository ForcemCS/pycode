## JSON Data

**核心**：对于Python开发者来说，你完全可以把JSON看作是一个语法更严格的Python字典。

它是一种通用的、所有编程语言都认识的“数据普通话”。

JSON的本质就是一个**字符串**。我们可以把复杂的程序数据（比如一个包含很多信息的用户对象）转换成一个有特定格式的字符串。

字符串是计算机世界里最容易传输的东西。无论是通过网络发送、存成一个`.txt`文件，还是复制粘贴，都非常方便。

### 序列化与反序列化

+ **编码 (Encode) / 序列化 (Serialization)**:

  把你程序中的数据（比如Python的字典）**“打包”**成一个JSON格式的字符串。

  ```
  json.dumps()
  ```

+ **解码 (Decode) / 反序列化 (Deserialization)**:

  把收到的JSON格式字符串**“解包”**，还原成你程序能用的数据（比如Python的字典）。

  ```
  json.loads()
  ```

+ 示例

  ```json
  {
    "firstName": "Eric",
    "lastName": "Smith",
    "address": {
      "country": "USA",
      "state": "New York"
    },
    "age": 28,
    "favoriteNumbers": [ 42, 3.14 ],
    "likesSushi": false,
    "driversLicense": null
  }
  ```

  - **最外层的 `{}`**: 表明整个内容是一个JSON对象（在Python里会变成一个字典）。
  - **`"firstName": "Eric"`**: 一个键值对。键 `"firstName"` 是一个字符串，值 `"Eric"` 也是一个字符串。**注意，键也必须用双引号！**
  - **`"address": { ... }`**: 一个嵌套的例子。键 `"address"` 的值是**另一个JSON对象**。
  - **`"favoriteNumbers": [ 42, 3.14 ]`**: 另一个键值对。键 `"favoriteNumbers"` 的值是一个**JSON数组**（在Python里会变成一个列表）。
  - **`"likesSushi": false`**: 值为布尔类型。注意是小写的 `false`。
  - **`"driversLicense": null`**: 值为 `null`。

### 示例代码

#### JSON字符串 → Python字典

```python
import json

# 这是一个从网络或文件收到的JSON字符串
# 注意：在Python中，为了表示一个多行字符串，我们用三个引号 '''
json_string = '''
{
  "firstName": "Eric",
  "lastName": "Smith",
  "age": 28,
  "likesSushi": false,
  "favoriteNumbers": [42, 3.14],
  "driversLicense": null
}
'''

# 使用 json.loads() 将字符串“解包”成Python对象
python_dict = json.loads(json_string)

# 现在 python_dict 就是一个我们熟悉的字典了
print(f"转换后的类型: {type(python_dict)}")
# 输出: 转换后的类型: <class 'dict'>

# 我们可以像操作普通字典一样操作它
print(f"名字: {python_dict['firstName']}")
# 输出: 名字: Eric

print(f"他喜欢寿司吗? {python_dict['likesSushi']}") # false -> False
# 输出: 他喜欢寿司吗? False

print(f"驾照信息: {python_dict['driversLicense']}") # null -> None
# 输出: 驾照信息: None
```

**注意观察**: JSON中的 `false` 和 `null` 在 `loads` 之后，自动转换成了Python中的 `False` 和 `None`。

#### 序列化 (Encoding): Python字典 → JSON字符串

```python
import json

# 这是一个标准的Python字典
person_data = {
    "name": "Alice",
    "age": 30,
    "isStudent": True,  # Python的 True
    "courses": ["History", "Math"],
    "credentials": None # Python的 None
}

# 使用 json.dumps() 将字典“打包”成JSON字符串
json_string = json.dumps(person_data)

# 打印结果
print(f"转换后的类型: {type(json_string)}")
# 输出: 转换后的类型: <class 'str'>

print(f"生成的JSON字符串: {json_string}")
# 输出: 生成的JSON字符串: {"name": "Alice", "age": 30, "isStudent": true, "courses": ["History", "Math"], "credentials": null}
```

**注意观察**: Python的 `True` 和 `None` 在 `dumps` 之后，被正确地转换成了JSON标准的 `true` 和 `null`。

**让JSON字符串更易读：**
`dumps` 函数有个非常有用的参数 `indent`。

```python
# 使用 indent 参数来格式化输出
pretty_json_string = json.dumps(person_data, indent=4)
print(pretty_json_string)
```

输出结果就会像我们手动写的那样，带缩进和换行，非常便于阅读：

```json
{
    "name": "Alice",
    "age": 30,
    "isStudent": true,
    "courses": [
        "History",
        "Math"
    ],
    "credentials": null
}
```

### 需要注意的限制

+ Python的数据类型比JSON标准多得多。比如 `datetime` (日期时间), `Decimal` (高精度数字), `set` (集合), 还有我们自己创建的类 (custom classes)。

+ `json.dumps()` 默认只认识Python里能直接对应到JSON类型的那些数据。如果你给它一个它不认识的，它就会报错。

  ```python
  import json
  from datetime import datetime
  
  # datetime 对象是JSON不认识的
  data_with_datetime = {
      "name": "Bob",
      "event_time": datetime.now() # 获取当前时间
  }
  
  try:
      json.dumps(data_with_datetime)
  except TypeError as e:
      print(f"出错了! 错误信息: {e}")
  
  # 输出: 出错了! 错误信息: Object of type datetime is not JSON serializable
  ```

  