# 텍스트 데이터 출력

from pprint import pprint
import json
import csv  # 파일을 읽고 써주는 라이브러리
import csv
print('2회차 조병진')
print('Hello, Python!')

for i in range(1, 6):  # 렌지 사용, 1 ~ 5번 반복
    print(i, f'일차 파이썬 공부중')


# 텍스트 데이터 입력 🐳
# 과일 데이터를 활용하여 총 과일의 갯수를 기록하기

# 파일을 읽고 써주는 라이브러리

# 파일 불러오기
# '파일 경로'와 '읽기 또는 쓰기', '불러올 문자' 를 정하고 열 파일의 이름을 지정
with open('./data/fruits.txt', 'r', encoding='utf-8') as f:
    # 읽은 결과를 변수로 지정
    text = f.read()

# 변수를 개행을 기준으로 쪼개기
a = text.split('\n')

# 리스트 길이 반환
print(len(a))


# 텍스트 데이터 활용 🐳
# 과일 데이터를 활용하여 berry로 끝나는 과일의 갯수와 목록을 기록하기


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


# 텍스트 데이터 활용 - 등장 횟수 🐳
# 과일 데이터를 활용하여 과일의 이름과 등장 횟수를 기록하기


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


# JSON 데이터 활용 - 영화 단일 정보 🐳
# 영화 데이터를 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하기

# json 이란? 인터넷에서 자료를 주고받을 때 그 자료들을 표현하는 방법
# 프린트 대신 예쁘게 출력하는 모듈 (리스트나 딕셔너리 등)


def movie_info(movie):
    pass

    # 딕셔너리 형태로 변수 지정
    result = {
        # 키 값은 설정하고, 무비 안에서 해당 값들 가져오기
        'genre_ids': movie.get('genre_ids'),
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')
    }

    pprint(result)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    pprint(movie_info(movie))


# JSON 데이터 활용 - 영화 단일 정보 응용 🐳
# 영화 데이터를 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하기


def movie_info(movie, genres):
    pass
    # 여기에 코드를 작성합니다.

    a = []
    # 무비 안에 해당 키 값을 반복
    for n in movie.get('genre_ids'):
        # 장르도 반복
        for i in genres:
            # 만약 장르 안에 아이디 값이 (무비)키 값이랑 같다면
            if n == i.get('id'):
                # a라는 변수에 장르 안에 이름 값을 추가
                a.append(i.get('name'))

    # 이하 설명은 04 문제에...
    result = {
        'genre_names': movie.get('genre_ids'),
        'id': movie.get('id'),
        'overview': movie.get('overview'),
        'title': movie.get('title'),
        'vote_average': movie.get('vote_average')
    }

    pprint(result)

    # 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='UTF8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))


# JSON 데이터 활용 - 영화 다중 정보 활용 🐳
# 영화 데이터를 활용하여 필요한 정보로만 구성된 리스트를 출력하기
# 전체 영화 정보는 평점 높은 20개의 영화 데이터


def movie_info(movies, genres):
    pass

    # 결과 값을 리스트에 저장
    result = []

    # 무비들 반복
    for movie in movies:
        # 무비 안에 아이디 값으로 반복
        for n in movie.get('genre_ids'):
            # 장르들 반복
            for i in genres:
                # 만일 장르의 아이디 값이 (무비) 아이디 값이라면
                if n == i.get('id'):
                    a = []
                    # a라는 변수에 장르 이름 추가
                    a.append(i.get('name'))

        l = {
            # a를 밸류 값으로 지정
            'genre_names': a,
            'id': movie.get('id'),
            'overview': movie.get('overview'),
            'title': movie.get('title'),
            'vote_average': movie.get('vote_average')
        }

        # 결과 값에 l값 추가
        result.append(l)

    # 정의된 movie_info 함수 밖으로 결과 값 내보내기
    return result


# 결과 값 출력
pprint(movie_info)

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='UTF8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='UTF8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
