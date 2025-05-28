##测试1
from pprint   import pprint

widgets = [f'w{i}' for i in range(1, 5)]
skus = [f'sku{i}' for i in range(1, len(widgets) + 1)]


print(dict(zip(widgets,skus)))


##测试2
suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']

suits_g = iter(suits)

for  suit in suits_g:
    suit_list = [suit] * len(ranks)
    a = list(zip(ranks, suit_list))
    print(a)

suits_g = iter(suits)

a = [
    list(zip(ranks,[suit] * len(ranks)))
    for suit in suits_g
]

pprint(a)
print('_' * 20)


suits = 'shdc'  # Spades, Hearts, Diamonds, Clubs
ranks = list('23456789') + ['10', 'J', 'Q', 'K', 'A']

def deck(suits,ranks):
    deck = [
        [(r, s) for r in ranks]
        for s in suits
    ]
    pprint(deck)
deck(suits,ranks)

##测试3
data = [10, 3, -5, 3.14, 100, 1]

def list_info(data, *, reverse=False):
    sorted_data = sorted(data, reverse=reverse)
    minimum = min(data)
    maximum = max(data)
    return sorted_data, minimum, maximum    ##return返回的是一个tuple

print(list_info(data))