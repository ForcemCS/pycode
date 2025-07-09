from pprint import pprint

import json

## code1
json_str = '''
{
    "name": "Eric Smith",
    "age": 32,
    "phoneNumbers": [
        {
            "type": "home",
            "number": "(212) 555-3276"
        },
        {
            "type": "work",
            "number": "(332) 555-1234"
        }
    ],
    "spouse": null,
    "children": [],
    "employed": true
}
'''
# 解析为python对象
eric = json.loads(json_str)
pprint(eric)
print("--" * 20)

#序列化为json
json_str_2 = json.dumps(eric, indent=4)
print(json_str_2,type(json_str_2))


## code2

from datetime import datetime

d  = {
    "name": "wu kui",
    "dob": datetime(2025, 7, 9)
}

def my_encoder(obj):
    print(f'my_encoder({obj}) called ...' )
    
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError

# 当遇到无法直接序列化的对象时（比如 datetime），就调用我指定的函数 my_encoder(obj)，用它的返回值来代替这个对象。
print(json.dumps(d,default=my_encoder))

## code3

from decimal import Decimal
from datetime import date

# 这是一个dict ,要序列化为json
d = {
    "symbol": "IBM",
    "date": date(2020, 9, 21),
    "day": {
        "open": Decimal('120.475'),
        "high": Decimal('120.70'),
        "low": Decimal('118.58'),
        "close": Decimal('120.25'),
        "volume": 5_205_413
    }
}


def stock_encoder(obj):
    if isinstance(obj, date):
        return obj.isoformat()
    if isinstance(obj, Decimal):
        #return str(obj)
        return round(float(obj),2)
    raise TypeError

print(json.dumps(d, default=stock_encoder, indent=4))
