##delimiter定界符 

# with open('actors.csv') as file:
#     for row in file:
#         print(row)
        

# with open('actors.csv') as file:
#     for row in file:
#         row = row.strip()
#         fields = row.split(',')
#         print(fields)
# print('-'  * 10 )
        

# import csv
# with open('actors.csv') as f:
#     reader = csv.reader(f,delimiter=',',quotechar='"')
#     for row in reader:
#         print(row)


nasdaq = 'nasdaq.csv'
st = 'st-2001est-01.csv'

# with open(nasdaq) as f :
#     for _ in range(5):
#         row = next(f)
#         print(row)

##code1        
import csv
from pprint  import pprint

def parse_nasdaq(f_name):
    
    result = []
    
    with open(f_name) as f:
        reader = csv.reader(f)
        
        headers = next(reader)
        
        for row in reader:
            row[-1] = float(row[-1])
            result.append(row)
    
    return result
    

pprint(parse_nasdaq(nasdaq)[:3])  
print('-' * 20 )

##code2

import csv
from pprint  import pprint

def parse_nasdaq2(f_name):
    
    
    with open(f_name) as f:
        reader = csv.reader(f)
        
        headers = next(reader)
        
        for row in reader:
            area = row[0]
            data = row[1:]
            data = [area]  + [ int(field.replace(',','_')) for field in  data ]
            
            print(data)
    
parse_nasdaq2(st)