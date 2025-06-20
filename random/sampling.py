# 随机抽样（random sampling）:
#     random.sample() 函数就像是从一个装有很多不同东西的帽子里，一次性抓出一把你想要的数量的东西，而且抓出来的东西不会重复
#     sample(population, k)
#     1. population (总体) 的数据类型可以很灵活。
#     sequence (序列): 最常见的类型，比如列表 (list) 或 元组 (tuple)。
#     set 
#     range object (范围对象)
#     2. population 中的每一个元素被选中的概率都是完全相等的
#     3. without replacements (无放回抽样)
#     这是 sample() 函数最核心的特点！
#     4. sample() 函数返回的结果永远是一个新的列表 
#     5. k cannot exceed len(seq) → ValueError otherwise   样本大小 k 不能超过总体的元素个数。

# random.choices()  是又放回抽样

# shuffle重新洗牌源list,不然会任何东西

import random

#code1
l = [1, 2, 3, 4, 5]

# a = random.shuffle(l)   错误的写法，要直接使用源list
random.shuffle(l)
print(l)

#若想要每次执行程序，shuffle后的结果都一样的话，需要设置seed

l = [1, 2, 3, 4, 5]

random.seed(0)
random.shuffle(l)
print(l)

##code2

s = set('abcdef')
random.seed(0)

print(sorted(s))
for _ in range(5):
    print(random.sample(sorted(s),3))
    
#code3

from time import perf_counter

random.seed(0)

start = perf_counter()
for   _ in range(5):
    #从区间 [2, 100) 中，以步长为 2 生成随机数（只会生成偶数）。
    print([random.randrange(2,1_00,2) for  _ in range(1)])

end = perf_counter()
print(end - start)

##这种方式时间会更短
start = perf_counter()
for   _ in range(5):
    print(random.sample(range(2,1_00,2), 1))

end = perf_counter()
print(end - start)
print('-' * 30 )


##code4

s = 1, 2, 3, 4, 5, 6

random.seed(11)

for _ in range(5):
    #先取出一个放回去，再取出一个
    print(random.choices(s,k=2))
    

#code5
def chart_freq(data):
    pad = max([len(str(el[0])) for el in data])
    for k, v in data:
        print(f"{str(k).rjust(pad)} {'*' * round(v)}")

def freq_distribution(data):
    freq = {}
    for el in data:
        freq[el] = freq.get(el, 0) + 1
    return freq

def relative_freq(freq_dist):
    sum_freq = sum(freq_dist.values())
    return {
        k: v / sum_freq * 100 for k, v in freq_dist.items()
    }


print(freq_distribution([1,2,1,1,3,3]))


##接下来计算二维矩阵的频率分布
def freq_distribution_matrix(data):
    linearized =  [el for row in data for el in row ]
    return freq_distribution(linearized)

random.seed(11)

population = tuple('abcfedghij')
data = [random.choices(population, k = 5) for _ in range(3)]
print(data)

print(freq_distribution_matrix(data))

##code6

#即当样本量足够大时，事件的观测频率会无限接近其理论概率。
#weights 是一个与 population 长度相同的数值列表（或元组）。
def analyze_choices(base_data, num_choices, choice_size, weights=None):
    data = [
        random.choices(base_data, k=choice_size, weights = weights)
        for _ in range(num_choices)
    ]

    freq = freq_distribution_matrix(data)
    rel = relative_freq(freq)

    sorted_items = sorted(rel.items(), key=lambda x: x[0])
    chart_freq(sorted_items)
    
base_data = tuple('abcdefghij')

random.seed(0)
print(analyze_choices(base_data, 10_000, 5))


weights = [1] * 10
weights[0] = 2
weights[1] = 3
weights[-1] = 4

random.seed(0)
print(analyze_choices(base_data, 10_000, 5,weights=weights))