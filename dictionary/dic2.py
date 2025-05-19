d1 = {}
d2 = dict()

##可能是订单系统的数据
transactions = [
  {'item': 'widget', 'trans_type': 'sale', 'quantity': 10},
  {'item': 'widget', 'trans_type': 'sale', 'quantity': 5},
  {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
  {'item': 'widget', 'trans_type': 'refund', 'quantity': 2},
  {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
  {'item': 'license', 'trans_type': 'refund', 'quantity': 1}
]

sales_summary = {}

for t  in  transactions:
    if  t['trans_type'] == 'sale':
        item = t['item']
        quantity = t['quantity']
        sales_summary[item] = sales_summary.get(item, 0) + quantity
print(sales_summary) 

transactions = [
  {'item': 'widget', 'trans_type': 'sale', 'quantity': 10},
  {'item': 'widget', 'trans_type': 'sale', 'quantity': 5},
  {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
  {'item': 'widget', 'trans_type': 'refund', 'quantity': 2},
  {'item': 'license', 'trans_type': 'sale', 'quantity': 1},
  {'item': 'license', 'trans_type': 'refund', 'quantity': 1}
]

sales_summary = {}


for t in transactions:
    item  = t['item']
    quantity = t['quantity']
    is_sale = True if t['trans_type'] == 'sale' else False

    if is_sale:
        if  item in sales_summary:
            sales_summary[item]  += quantity
        else:
            sales_summary[item] = quantity
print(sales_summary)


net_sales = {}

for t in transactions:
    item  = t['item']
    quantity = t['quantity']
    is_sale = True if t['trans_type'] == 'sale' else False

    if not is_sale:
        quantity = -quantity
        if  item in net_sales:
            sales_summary[item]  += quantity
        else:
            sales_summary[item] = quantity
print(sales_summary)


d1 = {'a':1, 'b':2}
d2 = {'c':3, 'd':4}

combined = {'a':1, 'b':2,'c':3, 'd':3}

d1.update(d2)
print(d1)