##coe1
file_name = "DEXUSEU.csv"

#返回一个文件对象，用变量 file 来接收它
file = open(file_name, 'r')

#file对象的属性，用来表示它所打开的文件名
print(file.name)
print(file.readable())
print(file.writable())
print(file.closed)  #false

file.close()
print(file.closed)  #true

##code2

f = open(file_name)

data= f.readlines()

f.close()

print(data)

##code3

f  = open(file_name)

for line in f:
    print(line, end='')
    
f.close()


with open(file_name) as f:
    print("ccc")
#完成了with中的内容，自动closed
print(f.closed)

with open(file_name) as f:
    #读取所有的内容到内存中
    print(f.readlines())
print('-' * 10 )
##code4

with open(file_name)  as f:
    print(next(f))
    
    for row in f:
        row = row.strip()
        
        date, value_str = row.split(',')
        
        print(date,value_str)

##code5

data = []
with open(file_name)  as f:
    header = (next(f))
    
    for row in f:
        row = row.strip()
        
        date, value_str = row.split(',')
        try:
            value_str = float(value_str)
            data.append((date,value_str))
        except ValueError:
            pass
print(data)
