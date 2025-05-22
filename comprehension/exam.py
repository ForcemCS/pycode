from  time import perf_counter

##测试1
data = [
    {'open': 100, 'high': 120, 'low': 90, 'close': 110},
    {'open': 110, 'high': 130, 'low': 80, 'close': 120},
    {'open': 120, 'high': 140, 'low': 70, 'close': 130},
    {'open': 130, 'high': 150, 'low': 60, 'close': 140},
]

ranges = []
for d in data:
    ranges.append(d['high'] - d['low'])
print(ranges)


ranges = [ 
    d['high'] - d['low']
    for d in data
]
print(ranges)

##测试2
##先找出1-100中能被2-9中任意一个数字整除的所有数字，然后打印出1-100中剩余的数字

###方法1 
start= perf_counter()

dividend  =[a for a in range(1,101)]

divisor = [a for a in range(2,10)]

aim = set()

for d1  in dividend:
    for d2 in divisor:
        if d1 % d2 == 0:
            aim.add(d1)


b =  [b for b in dividend if b not in  aim]
print(b)

end = perf_counter()

print(f"执行时间: {end - start:.8f}秒")

###方法2
start = perf_counter()

dividend = set(range(1, 101))
divisor = range(2, 10)


divisible = {x for d in divisor for x in range(d, 101, d)}


result = sorted(dividend - divisible)

print(result)

end = perf_counter()
print(f"执行时间: {end - start:.8f} 秒")



##测试3
##创建一个新的字典列表，其中包含排名至少为 5 且风险小于 0.6 的字典
##这些字典应包含符号和一个名为weighted的计算键，该键是排名除以风险的结果。(该值应四舍五入到小数点后两位）。请勿以任何方式更改原始数据列表或字典。
data = [
    {'symbol': 'ABCD', 'name': 'ABCD Company', 'ranking': 2, 'risk': 0.2},
    {'symbol': 'BCDE', 'name': 'BCDE Company', 'ranking': 5, 'risk': 0.2},
    {'symbol': 'CDEF', 'name': 'CDEF Company', 'ranking': 8, 'risk': 0.5},
    {'symbol': 'DEFG', 'name': 'DEFG Company', 'ranking': 7, 'risk': 0.8},
    {'symbol': 'EFGH', 'name': 'EFGH Company', 'ranking': 9, 'risk': 0.6},
    {'symbol': 'FGHI', 'name': 'FGHI Company', 'ranking': 10, 'risk': 0.1},
    {'symbol': 'GHIJ', 'name': 'GHIJ Company', 'ranking': 3, 'risk': 0.6},
    {'symbol': 'HIJK', 'name': 'HIJK Company', 'ranking': 5, 'risk': 0.5},
    {'symbol': 'IJKL', 'name': 'IJKL Company', 'ranking': 5, 'risk': 0.7},
    {'symbol': 'JKLM', 'name': 'JKLM Company', 'ranking': 6, 'risk': 0.9},
    {'symbol': 'KLMN', 'name': 'KLMN Company', 'ranking': 6, 'risk': 0.4},
    {'symbol': 'LMNO', 'name': 'LMNO Company', 'ranking': 8, 'risk': 0.4},
    {'symbol': 'MNOP', 'name': 'MNOP Company', 'ranking': 8, 'risk': 0.2},
    {'symbol': 'NOPQ', 'name': 'NOPQ Company', 'ranking': 1, 'risk': 0.5},
    {'symbol': 'OPQR', 'name': 'OPQR Company', 'ranking': 9, 'risk': 0.2},
    {'symbol': 'PQRS', 'name': 'PQRS Company', 'ranking': 10, 'risk': 0.9},
    {'symbol': 'QRST', 'name': 'QRST Company', 'ranking': 3, 'risk': 0.4},
    {'symbol': 'RSTU', 'name': 'RSTU Company', 'ranking': 7, 'risk': 0.3},
    {'symbol': 'STUV', 'name': 'STUV Company', 'ranking': 8, 'risk': 0.1},
    {'symbol': 'TUVW', 'name': 'TUVW Company', 'ranking': 7, 'risk': 0.9}
]


x = [ d1 for d1 in data if d1['ranking'] > 4 and d1['risk'] < 0.6] 
print(x)


result = [
    {
        'symbol': d1['symbol'],
        'weighted': round(d1['ranking'] / d1['risk'], 2)
    }
    for d1 in data if d1['ranking'] > 4 and d1['risk'] < 0.6
]

print(result)