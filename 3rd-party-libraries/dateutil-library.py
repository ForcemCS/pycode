from datetime import datetime
## code1
##时间字符串解析为特定格式的datetime对象
a = datetime.strptime('2025-07-08T09:50:00','%Y-%m-%dT%H:%M:%S')

print(type(a), a, sep='\n')


b = datetime.strptime('2020-01-01 10:30:00 am', '%Y-%m-%d %I:%M:%S %p')

print(b)


## code2 

from dateutil import parser

a = parser.parse('2025-07-08T09:50:00')
print(a)

b = parser.parse('2020-01-01 10:30:00 am +08:00')
print(b)
print(b.tzinfo)
print(b.isoformat())

##code 3

c  = parser.parse('12/11/2025', dayfirst=False)
print(c)

d = "This is July the 8th, 2025 at 10:20 am +08:00"
s = "Let's meet on March the 4th, 2020 at 3pm"

try:
    dt, tokens = parser.parse(d, fuzzy_with_tokens=True)
    print(dt)
except Exception as ex:
    print(type(ex), ex)
    
    
## code4 

source_file = 'DEXUSEU.csv'

import csv
import pytz

with open(source_file) as source:
    csv_reader = csv.reader(source)
    
    header = next(csv_reader)
    print(header)
    
    for row in csv_reader:
        print(row)
    

dt_eastern = pytz.timezone('US/Eastern')  #美国东部时区，有纽约，华盛顿，亚特兰大等城市
dt_shanghai = pytz.timezone('Asia/Shanghai')


#为naive datetime附加时区信息
aa = dt_shanghai.localize(parser.parse('7/8/2025 1:00pm'))

print(aa)

print('---' * 20 )


## code 5 

with open(source_file) as source:
    csv_reader = csv.reader(source)
    
    header = next(csv_reader)
    print(header)
    
    for dt, rate in csv_reader:
        dt_naive = parser.parse(dt).replace(hour=8)
        dt_aware = dt_shanghai.localize(dt_naive)
        dt_uct = dt_aware.astimezone(pytz.UTC)
        
        print(f"{dt} : {dt_naive} : {dt_uct} : 上海时间_{dt_aware.isoformat()}  : {rate} ")
        
        
## code6

from datetime import datetime

import dateutil
import pytz
import csv

def convert(source_file, target_file):
    tz_eastern = pytz.timezone('US/Eastern')
    
    with open(source_file) as source:
        with open(target_file, mode='w', newline='') as target:
            csv_reader = csv.reader(source)
            csv_writer = csv.writer(target)
            
            header = next(csv_reader)
            csv_writer.writerow(header)
            
            for dt, rate in csv_reader:
                dt_naive = parser.parse(dt).replace(hour=8)
                dt_aware = dt_shanghai.localize(dt_naive)
                dt_uct = dt_aware.astimezone(pytz.UTC)
                
                csv_writer.writerow([dt_uct.isoformat(), rate])
                
source_file = 'DEXUSEU.csv'

target_file = 'converted.csv'

convert(source_file, target_file)              
            