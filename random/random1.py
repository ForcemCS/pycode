import random 

##code1
for _ in range(3): 
    print(random.random())
print("-" * 20 )

random.seed(0)
for _ in range(3): 
    print(random.random()) 
print("-" * 20 )
##code2

random.seed(0)
for _ in range(3):
    print(random.randrange(1,6))
    
##code3

data_2 = [
  ('a', 12.3),
  ('b', 30.7),
  ('c', 20.5),
  ('d', 36.5)
]

for k, v in data_2:
    print(f'{k}| { "*" * round(v) }')
    
##code4

data_3 = [
    ('abc', 12.3),
    ('d', 30.7),
    ('ef', 20.5),
    ('ghij', 36.5)
]

for k, v in data_3:
    #print(f'{k.rjust(10, "*")}| { "*" * round(v) }')
    print(f'{k.rjust(10)}| { "*" * round(v) }')
    
    
keys = [  str(ele[0]) for ele  in  data_3]
print(keys)

keys_len = [  len(str(ele[0])) for ele  in  data_3]
print(keys_len)
pad = max(keys_len)
print(pad)
print("-" * 20 )


for k, v in data_3:
    #print(f'{k.rjust(10, "*")}| { "*" * round(v) }')
    print(f'{str(k).rjust(pad)}| { "*" * round(v) }')
print("-" * 20 )
    
##code5

def chart_freq(data):
    pad = max([  len(str(ele[0])) for ele  in  data])
    for k, v in data:
        print(f'{str(k).rjust(pad)}| { "*" * round(v) }')
chart_freq(data_2)


##code6 

random.seed(0)

data = [ random.randint(1, 10) for _ in range (5)]

freq = {}

for ele  in  data:
    freq[ele] = freq.get(ele, 0 ) + 1 
print(freq)


##code7

def freq_distribution(data):
    freq = {}
    for ele  in  data:
        freq[ele] = freq.get(ele, 0 ) + 1 
    return freq

a = freq_distribution(data)

sum_freq = sum(a.values())

relative_freq = a.copy()

for k in  relative_freq:
    relative_freq[k] = relative_freq[k] / sum_freq * 100
    
    print(relative_freq,a)
print('-' * 50 )
    
##code8

relative_freq = {
    k: v / sum_freq * 100  for k, v  in  a.items()
}

print(relative_freq)

print(relative_freq.items())

chart_freq(relative_freq.items())


sorted_items = sorted(relative_freq.items(), key=lambda x: x[0])
print(sorted_items)

chart_freq(sorted_items)
print('-' * 50 )

##code

def analyze_randint(n, a, b):
    data = [random.randint(a, b ) for _ in range(n) ]    
    freq = freq_distribution(data)
    rel = {
        k: v / sum_freq * 100  for k, v  in  freq.items()
    }
    sorted_items = sorted(rel.items(), key=lambda x: x[0])
    chart_freq(sorted_items)
analyze_randint(8,1,20)
