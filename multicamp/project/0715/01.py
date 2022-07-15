# 텍스트 데이터 입력
# 과일 데이터를 활용하여 총 과일의 갯수를 기록하기

# 파일을 읽고 써주는 라이브러리
import csv

# 파일 불러오기
# '파일 경로'와 '읽기 또는 쓰기', '불러올 문자' 를 정하고 열 파일의 이름을 지정
with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    # 읽은 결과를 변수로 지정
    text = f.read()

# 변수를 개행을 기준으로 쪼개기
a = text.split('\n')

# 리스트 길이 반환
print(len(a))
