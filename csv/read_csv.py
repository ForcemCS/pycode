##delimiter定界符 

with open('actors.csv') as file:
    for row in file:
        print(row)
        

with open('actors.csv') as file:
    for row in file:
        row = row.strip()
        fields = row.split(',')
        print(fields)
print('-'  * 10 )
        

import csv
with open('actors.csv') as f:
    reader = csv.reader(f,delimiter=',',quotechar='"')
    for row in reader:
        print(row)