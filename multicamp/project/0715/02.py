# 텍스트 데이터 활용
# 과일 데이터를 활용하여 berry로 끝나는 과일의 갯수와 목록을 기록하기

import csv  # 파일을 읽고 써주는 라이브러리

# 파일 불러오기
# '파일 경로'와 '읽기 또는 쓰기', '불러올 문자' 를 정하고 열 파일의 이름을 지정
with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    # 읽은 결과를 변수로 지정
    text = f.read()

# 변수를 개행을 기준으로 쪼개기
a = text.split('\n')
berry_list = []

for i in a:
    # 만일 뒤에서 5번째 글자가 '베리' 라면 ?
    if i[-5:] == 'berry':
        n = i.split('\n')
        # 나온 결과는 새 변수에 하나씩 저장
        berry_list = n + berry_list

# set으로 중복된 값을 제거하고 리스트 형태로 전환
result = list(set(berry_list))

# 리스트 길이 반환
print(len(result))

# 리스트 형태인 값을 한 줄씩 출력
for i in result:
    for j in i:
        print(j, end='')
    print()
