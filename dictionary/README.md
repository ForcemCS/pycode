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