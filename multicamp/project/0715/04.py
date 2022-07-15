# JSON 데이터 활용 - 영화 단일 정보
# 영화 데이터를 활용하여 필요한 정보로만 구성된 딕셔너리를 출력하기

# json 이란? 인터넷에서 자료를 주고받을 때 그 자료들을 표현하는 방법
import json
# 프린트 대신 예쁘게 출력하는 모듈 (리스트나 딕셔너리 등)
from pprint import pprint


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
