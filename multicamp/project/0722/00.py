# 00. API 문서와 requests 활용
# 아래의 문서를 활용하여 BTC(비트코인)의 KRW(원) 전일종가를 출력하시오.
# https://apidocs.bithumb.com/reference/현재가-정보-조회

import requests
from pprint import pprint


order_currency = 'BTC'
payment_currency = 'KRW'
url = f'https://api.bithumb.com/public/ticker/{order_currency}_{payment_currency}'

# 리퀘스트 활용하여 해당 웹사이트 접근
response = requests.get(url)

# json 형태로 변환
data = response.json()

# data 확인
pprint(data)

# get()을 활용하여 'data'안에 전일 '종가'에 접근
print(data.get('data').get('prev_closing_price'))
