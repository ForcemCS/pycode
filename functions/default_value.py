#在定义函数的时候指定默认值
def  my_func1(a=1):
    print(a)
my_func1()
my_func1(10)

def  my_func2(a, b=10, c= 20):
    print(a,b,c)
my_func2(1,25)

def is_clone(a, b, abs_tol=0.01):
    return abs(a - b) <= abs_tol

print(is_clone(1.23, 1.01))


#是否要对每个分割出来的子项进行去除首尾空白字符处理
def parse(s, sep=',',strip = True):
    items = s.split(sep)
    if strip:
        print([item.strip() for item in items])
    else:
        print(items)

parse('  a,    b,c  ',strip=False)

parse('a\n|b\n|c','|')

a= 'a\n|b\n|c'
print(a)

parse(a,'|')
parse(a,'|',False)

#sep=','设置各个参数之间的分隔符为 ,
#设置打印后结尾不要换行，而是输出 ***。
print(*'abc', sep=',',end='***')
print('next line')


##code1
data = [
    [1, 2, 3],
    [4, 5, 6]
]

def process_data(*args):
    print(args)
process_data(*data)

print(tuple(data))

##code2

a = ''
b = 'cc'
c = 10

d = a + b + str(c)
print(d)

f = b + str(c)
print(f)
print('-' * 10)

##code3

data = [
    [1, 2, 3],
    [4, 5, 6],
    [100, 200, 300]
]


def process_data(data, item_sep=',', line_sep='\n'):
    output = ''

    for row in data:
        for element in row:
            output = output + str(element) + item_sep
        output = output + line_sep

    return output
print(process_data(data))

# 输出的结果如下：
# 1,2,3,
# 4,5,6,
# 100,200,300,
#  空行

##code4
#join字符串对象的方法。,分隔符'.join(可迭代对象)
a = '--'.join(['1', '2', '3'])
print(a)
print('-' * 10)

data = [
    [1, 2, 3],
    [4, 5, 6],
    [100, 200, 300]
]
def process_data(data, item_sep=',', line_sep='\n'):
    output = ''

    for row in data:
        row_str = item_sep.join([str(col) for col in row])
        output = output + row_str + line_sep
    return output
print(process_data(data))

##code5

data = [
    [1, 2, 3],
    [4, 5, 6],
    [100, 200, 300]
]
def process_data(data, item_sep=',', line_sep='\n'):
    row_string = [
        item_sep.join( str(col) for col in row)   #在每次写代码的时候可以考虑是否使用generator
        for row in data
    ]
    return  line_sep.join(row_string)
print(process_data(data))
print('-' * 10)


##我们还可以使用一种更优美的方式
data = [
    [1, 2, 3],
    [4, 5, 6],
    [100, 200, 300]
]

row= [1, 2, 3]
def process_row(row, row_sep=','):
    return row_sep.join(str(ele) for ele in row)

def process_data(data,line_sep='\n'):
    row_strings = ( process_row(row) for row in data )
    return line_sep.join(row_strings)

print(process_data(data))
