import requests
import json

## code1 
# 目标：获取用户ID为1的所有文章
# api_url = 'https://jsonplaceholder.typicode.com/posts'
# params = {'userId': 1}

# # 发起 GET 请求
# response = requests.get(api_url, params=params)

# print(response.status_code)
# print(response.headers)
# print(response.reason)
# a = response.json()[0]

# print(json.dumps(a,indent=4))


## code2

# response = requests.get('https://www.baidu.com')

# print(response.status_code)
# print(response.reason)
# print(response.headers)
# print(response.text)
# print('--' * 20 )

# for key, value in response.headers.items():
#     print(f'{key}: {value}')
    
## code3 
# query_params = {
#     'q': 'pyhton http request',
#     'num': 5
# }

# response = requests.get(
#     'https://www.google.com',
#     params=query_params
    
# )

# print(response.status_code,response.reason)
# print(response.headers['Content-Type'])
# print(response.raise_for_status())


## code4 

response = requests.get('https://cn.nytimes.com')
for k , v in response.cookies.items():
    print(f'{k}: {v}')
    

## code5
#
###curl "https://finnhub.io/api/v1/quote?symbol=AAPL&token=xxxxxxxxx"

with open('secrets.txt') as f:
    API_KEY = next(f).strip()

base_url = 'https://finnhub.io/api/v1'

url = f'{base_url}/quote'

params = {
    'token': API_KEY,
    'symbol': 'AAPL'
}

response = requests.get(
    url,
    params=params
)

print(response.status_code)
print(response.json())

from datetime import datetime
print(datetime.fromtimestamp(1752091200))

## code6 

headers = {
    'X-Finnhub-Token' : API_KEY
}

for symbol in ['AAPLE', 'MSFT', 'GOOG']:
    try:
        response = requests.get(
            url = url,
            params = {'symbol': symbol},
            headers = headers
        )
        
        print(f'**** {symbol} ****')
        print(response.json())
    except requests.HTTPError as ex:
        print(f'Unable to retrieve data for {symbol} : {ex}')
        

## code7 

import requests

base_url = 'https://finnhub.io/api/v1'

base_webhook_url = f'{base_url}/webhook'

post_data = {
    'event': 'earnings',
    'symbol': 'AAPL'
}

# 订阅苹果公司发布财报这个事件
response = requests.post(
    url=f'{base_webhook_url}/add',
    headers=headers,
    json=post_data
)

print(response.status_code,response.json())  #{'id': 14897, 's': 'ok'}



response = requests.post(
    url=f'{base_webhook_url}/delete',
    headers=headers,
    json= {
        'id':  14897
    } 
)

print(response.json())