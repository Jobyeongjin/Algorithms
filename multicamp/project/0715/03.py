# 텍스트 데이터 활용 - 등장 횟수
# 과일 데이터를 활용하여 과일의 이름과 등장 횟수를 기록하기

import csv

with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    text = f.read()

a = text.split('\n')
n = {}  # 반복문에서 나온 값을 저장하기 위함

for i in a:
    # 오류가 나는지 확인하는 코드, if i in n: 으로 대체 가능
    try:
        n[i] += 1
    # 오류가 발생하면 이걸 실행, else: 으로 대체 가능
    except:
        n[i] = 1

# n 값인 딕셔너리 안에 키, 밸류 값 가져오기
for x, y in n.items():
    print(x, y)
