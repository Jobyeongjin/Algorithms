# 01. 인기 영화 조회
# 인기 영화 목록의 개수를 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.
# API key : 837e86c41f738f95ed4b63bd28dabae4

import requests
from pprint import pprint

# https://api.themoviedb.org/3/movie/popular?api_key=837e86c41f738f95ed4b63bd28dabae4&language=en-US&page=1
url = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '837e86c41f738f95ed4b63bd28dabae4',
    'language': 'ko-KR',
    'page': 1
}

response = requests.get(url+path, params=params)
data = response.json()

# 리스트 안에 딕셔너리 형태
li = data.get('results')


def popular_count():
    pass

    # 리스트의 길이 값을 구해 리턴 / 딕셔너리 총 개수 구하기
    return len(li)


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
