widget_sales = [
    {'name': 'widget 1', 'sales': 10},
    {'name': 'widget 2', 'sales': 5},
    {'name': 'widget 3', 'sales': 0}
]

#传统方法
sales_by_widget = {}
for  i in  widget_sales:
    widget_name = i['name']
    widget_sale = i['sales']
    sales_by_widget[widget_name] = widget_sale
print(sales_by_widget)

#dictionary comprehension 
sales_by_widget = { i['name']: i['sales'] for  i in  widget_sales }
print(sales_by_widget)


aa = 'hell,o!.'
bb= ",!."

for char in bb:
    print(char)
    aa = aa.replace(char,'')
print(aa)
print('-' * 10 )


paragraph = """
To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to.
"""
punctuation = " ,.!:-\n"

#我们想提取出paragraph中长度至少为5的单词
for char  in punctuation:
    paragraph = paragraph.replace(char, ' ')
    
print(paragraph.split())  

all_worls = {world.lower()  for  world in  paragraph.split() if len(world) >= 5}
print(all_worls)

#判断每个字符的重复次数
data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd']

freq = {}

for element in set(data):
    counts = len([char for char  in data if char == element])
    freq[element] = counts
print(freq)

#我们可以使用下列方法对其进行简化
freq = {
    element: len([char for char  in data if char == element])
    for element  in set(data)
}

print(freq)


##接下来我们使用更简单的方法
from collections import Counter   #Python 内置模块 collections 中的一个工具类 Counter，它专门用来统计元素出现的频率（次数），本质上是一个特殊的字典。
data = ['a', 'a', 'a', 'b', 'b', 'c', 'c', 'd']
freq = Counter(data)
print(freq)

freq = dict(Counter(data))
print(freq)


paragraph = """
To be, or not to be--that is the question:
Whether 'tis nobler in the mind to suffer
The slings and arrows of outrageous fortune
Or to take arms against a sea of troubles
And by opposing end them. To die, to sleep--
No more--and by a sleep to say we end
The heartache, and the thousand natural shocks
That flesh is heir to.
"""
punctuation = " ,.!:-\n"
freq = {
    k: v
    for k, v in Counter(paragraph.casefold()).items()
    if k not in punctuation
}

print(freq)