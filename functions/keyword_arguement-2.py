##code1
def func(a, b=2, c=3, *, d=10, e, f=30):
    print(a, b, c, d, e, f)

func(1,e=20)

##code2

def process_data(data, *,item_sep=',', line_sep='\n'):
    row_strings = [item_sep.join([str(element) for element in row])
                   for row in data]
    return line_sep.join(row_strings)

a = [
    [10, 20, 30],
    [100, 200, 300],
    [1000, 2000, 3000]
]

print(process_data(a))
print('-' * 10 )
print(process_data(a,item_sep=':',line_sep='\n\n'))
print('-' * 10 )

##code3

def coords_to_json(bascissa, ordinate):
    return f"{{bascissa: {bascissa}, ordinate: {ordinate}}}"
print(coords_to_json(bascissa=10,ordinate=20))

##code3
def func(a, b, *args, c, d, **kwargs):
    print("a:", a)
    print("b:", b)
    print("args:", args)
    print("c:", c)
    print("d:", d)
    print("kwargs:", kwargs)

#func(a = 1, b = 2, 3, 4, 5, c=6, d=7, e = 8,f = 'aa')  错误的写法
#一旦你开始使用关键字参数（a = 1, b = 2），那么之后所有的参数都必须是关键字参数


##code4

def to_json(args1, *, kwl1, **extras):
    formatted_extras = ', '.join([f"{k}: {v}"   for k,v in  extras.items()])
    result = f'{{ args1: {args1}, kwl1: {kwl1}, extras: {{{formatted_extras}}}'

    return result

print(to_json(10, kwl1=20, a =1, b=2,c='ro3'))