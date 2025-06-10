import  csv

print(csv.list_dialects())

with open('actors.pdv') as f:
    for row in f:
        print(row)
        
        
with open('actors.pdv') as f:
    reader = csv.reader(
        f,
        delimiter='|',                   #reader 会在每一行中寻找 | 字符来切分数据，而不是默认的逗号
        quotechar="'",                   #定义用于包裹字段的引号字符。
        escapechar="\\",                 
        skipinitialspace=True
        
    )
    for row  in reader:
        print(row)
        
        
#code2 

csv.register_dialect(
    'pdv',
    delimiter='|',                   #reader 会在每一行中寻找 | 字符来切分数据，而不是默认的逗号
    quotechar="'",                   #定义用于包裹字段的引号字符。
    escapechar="\\",                 
    skipinitialspace=True
    
)

print(csv.list_dialects())

with open('actors.pdv') as f:
    reader = csv.reader(f, dialect='pdv')
    for row  in reader:
        print(row)