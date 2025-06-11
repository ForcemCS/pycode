
import csv

#code1 
header = ['姓名', '年龄', '城市']

# data = [
#     ['张三', '25', '北京'],
#     ['李四', '30', '上海'],
#     ['王五', '22', '广州']
# ]


data = [
    ['First Name', 'Last Name', 'DOB', 'Sketches'],
    ['John', 'Cleese', '10/27/39', "The Cheese Shop, Ministry of Silly Walks, It's the Arts"],
    ['Eric', 'Idle', '3/29/43', 'The Cheese Shop, Nudge Nudge, "Spam"'],
    ['Peter', "O'Toole", '8/2/32', 'Lawrence of Arabia']
]

filename = 'students.csv'

# newline='' 是一个很重要的参数，可以防止在 Windows 系统下写入时每行后都多一个空行。
with open(filename, 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)             #申明以csv的方式进行写

    writer.writerow(header)            #这个方法每次接收一个可迭代对象（比如列表 [] 或元组 ()）
    for row in data:
        writer.writerow(row)

print(f"数据已成功写入到文件 '{filename}' 中！")


#code2

data = [
    ['First Name', 'Last Name', 'DOB', 'Sketches'],
    ['John', 'Cleese', '10/27/39', "The Cheese Shop, Ministry of Silly Walks, It's the Arts"],
    ['Eric', 'Idle', '3/29/43', 'The Cheese Shop, Nudge Nudge, "Spam"'],
    ['Peter', "O'Toole", '8/2/32', 'Lawrence of Arabia']
]


csv.register_dialect(
    'pdv',
    delimiter='|',
    quotechar="'",
    doublequote=False,
    escapechar="\\"
)


with open('test-1.csv', 'w', newline='') as f:
    writer = csv.writer(f,dialect='pdv')
    for row in data:
        writer.writerow(row)
        