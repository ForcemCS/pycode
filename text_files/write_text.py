##code1
f = open('test.csv', 'w')

f.write('abc')
f.write('123456')

f.close()

with open('test.csv') as f:
    print(f.readlines())
    
##code2

with  open('test.csv', 'w') as f:
    f.write('abc\n')
    f.write('123\n')
    
with open('test.csv') as f:
    print(f.readlines())
    
##code3
data = ['line 1', 'line 2', 'line 3']

with open('test.csv', 'w') as f:
    f.writelines(data)

with open('test.csv') as f:
    print(f.readlines())
    
data = ['line 1\n', 'line 2\n', 'line 3\n']

with open('test.csv', 'w') as f:
    f.writelines(data)

with open('test.csv') as f:
    print(f.readlines())
    
##code4
data = ['line 1', 'line 2', 'line 3']
with  open('test.csv', 'w') as f:
    f.writelines('\n'.join(data))
    
with open('test.csv') as f:
    print(f.readlines())
    
##code5
with open('test.csv', 'a') as f:
    f.write('line4\n')
    f.write('line\n')

with open('test.csv') as f:
    print(f.readlines())
    
##code5

source_file = 'DEXUSEU.csv'
with open(source_file)  as f :
    for _  in range(5):
        print(next(f).strip())
        
##code6
with open(source_file)  as f :
    data = f.readlines()
    print(data[:5])

del data[0]
print(data[:5])

data = [line.strip() for line in data]

print(data[:5])

def split_date(dt_str):
    return dt_str[:4], dt_str[5:7], dt_str[8:]

print(split_date('2015-04-03'))


##code7

def transform_row_for_output(row):
    row = row.strip()
    dt_str, rate = row.split(',')
    
    try:
        float(rate)
    except ValueError:
        return None
    year, month, day = split_date(dt_str)
    result = ','.join([year,month,day,rate])
    result += '\n'
    return  result

a =  transform_row_for_output('2015-04-03,.\n')

print(type(a).__name__)


##code8

def split_date(dt_str):
    return dt_str[:4], dt_str[5:7], dt_str[8:]

def transform_row_for_output(row):
    row = row.strip()
    dt_str, rate = row.split(',')
    
    try:
        float(rate)
    except ValueError:
        return None
    year, month, day = split_date(dt_str)
    result = ','.join([year,month,day,rate])
    result += '\n'
    return  result

target_file = 'output.csv'

with open(source_file) as f:
    data = f.readlines()
    
del data[0]

with open(target_file, 'w') as f:
    f.write('YEAR,MONTH,DAY,EXCH\n')
    for row in data:
        transformd = transform_row_for_output(row)
        if transformd is not None:
            f.write(transformd)
        
with open(target_file) as f:
    for row in f:
        print(row.strip())
        
    
##code9

def transform_file_batch(source_file, target_file):
    with open(source_file) as f:
        data = f.readlines()
    del data[0]
    
    with open(target_file, 'w') as f:
        f.write('YEAR,MONTH,DAY,EXCH\n')
        for row in data:
            transformd = transform_row_for_output(row)
            if transformd is not None:
                f.write(transformd)

transform_file_batch(source_file=source_file,target_file=target_file)
                
with open(target_file) as f:
    for row in f:
        print(row.strip())
        
##接下来编写一种更高效的方式


def transform_file_batch(source_file, target_file):
    with open(source_file) as source:
        with open(target_file, 'w') as target:
            next(source)
            target.write('YEAR,MONTH,DAY,EXCH\n')
            
            for row in source:
                transformd = transform_row_for_output(row)
                if transformd is not None:
                    target.write(transformd)

transform_file_batch(source_file=source_file,target_file=target_file)