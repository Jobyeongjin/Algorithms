# 00. API 문서와 requests 활용 🐳
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


# 01. 인기 영화 조회 🐳
# 인기 영화 목록의 개수를 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# 응답 받은 데이터 영화 개수를 반환하는 함수를 작성합니다.
# API key : 837e86c41f738f95ed4b63bd28dabae4


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


# 02. 특정 조건에 맞는 인기 영화 조회 🐳
# 인기 영화 목록 중 평점이 8점 이상인 영화 목록을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# 응답 받은 데이터 중 평점(`vote_average`)이 8점 이상인 영화 목록을 리스트로 반환하는 함수를 작성합니다.


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


def vote_average_movies():
    pass

    # 리스트 안 딕셔너리를 반복
    for i in li:
        # 딕셔너리 안에 키값인 'vote_average'가 8이상이라면
        if i['vote_average'] >= 8:
            return [i]


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록중 vote_average가 8 이상인 영화목록 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(vote_average_movies())
    """
    [{'adult': False,
      'backdrop_path': '/ocUp7DJBIc8VJgLEw1prcyK1dYv.jpg',
      'genre_ids': [28, 12, 878],
      'id': 634649,
      'original_language': 'en',
      'original_title': 'Spider-Man: No Way Home',
      'overview': '미스테리오의 계략으로 세상에 정체가 탄로난 스파이더맨 피터 파커는 하루 아침에 평범한 일상을 잃게 된다. 문제를 '
                  '해결하기 위해 닥터 스트레인지를 찾아가 도움을 청하지만 뜻하지 않게 멀티버스가 열리면서 각기 다른 차원의 '
                  '불청객들이 나타난다. 닥터 옥토퍼스를 비롯해 스파이더맨에게 깊은 원한을 가진 숙적들의 강력한 공격에 피터 파커는 '
                  '사상 최악의 위기를 맞게 되는데…',
      'popularity': 1842.592,
      'poster_path': '/voddFVdjUoAtfoZZp2RUmuZILDI.jpg',
      'release_date': '2021-12-15',
      'title': '스파이더맨: 노 웨이 홈',
      'video': False,
      'vote_average': 8.1,
      'vote_count': 13954},
    ..생략..,
    }]
    """


# 03. 특정 조건에 맞는 인기 영화 조회 🐳
# 인기 영화 목록을 평점이 높은 순으로 5개의 정렬하여 영화 데이터 목록을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# 응답 받은 데이터 중 평점(`vote_average`)이 높은 영화 5개의 정보를 리스트로 반환하는 함수를 작성합니다.


url = 'https://api.themoviedb.org/3'
path = '/movie/popular'
params = {
    'api_key': '837e86c41f738f95ed4b63bd28dabae4',
    'language': 'ko-KR',
    'page': 1
}

response = requests.get(url+path, params=params)
data = response.json()
li = data.get('results')


def ranking():
    pass
    # sorted() 함수 사용, 람다 사용, reverse가 참이면 역순으로 정렬(즉 평점이 높은 순으로 정렬) 🚨
    a = sorted(li, key=lambda x: x['vote_average'], reverse=True)
    # 앞에서 5번째까지만 담기
    result = a[:5]

    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록을 정렬하여 평점순으로 5개 영화 반환
    (주의) popular 영화목록의 경우 시기에 따라 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(ranking())
    """
    [{'adult': False,
      'backdrop_path': '/odJ4hx6g6vBt4lBWKFD1tI8WS4x.jpg',
      'genre_ids': [28, 18],
      'id': 361743,
      'original_language': 'en',
      'original_title': 'Top Gun: Maverick',
      'overview': '최고의 파일럿이자 전설적인 인물 매버릭은 자신이 졸업한 훈련학교 교관으로 발탁된다. 그의 명성을 모르던 팀원들은 '
                  '매버릭의 지시를 무시하지만 실전을 방불케 하는 상공 훈련에서 눈으로 봐도 믿기 힘든 전설적인 조종 실력에 모두가 '
                  '압도된다. 매버릭의 지휘 아래 견고한 팀워크를 쌓아가던 팀원들에게 국경을 뛰어넘는 위험한 임무가 주어지자 매버릭은 '
                  '자신이 가르친 동료들과 함께 마지막이 될지 모를 하늘 위 비행에 나서는데…',
      'popularity': 911.817,
      'poster_path': '/jMLiTgCo0vXJuwMzZGoNOUPfuj7.jpg',
      'release_date': '2022-06-22',
      'title': '탑건: 매버릭',
      'video': False,
      'vote_average': 8.4,
      'vote_count': 1463},
    ..생략..,
    }]
    """


# 04. 영화 조회 및 추천 영화 조회
# - 영화 제목으로 검색을 하여 추천 영화 목록을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 추천 영화 목록(Get Recommendations)을 가져옵니다.
# 추천 영화 목록을 리스트로 반환하는 함수를 작성합니다.


# 4번부터는 입력값을 받아야 하기 때문에 정의하는 함수 안에서 작업해야 함 🚨 🐳
def recommendation(title):
    pass

    url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    URL = url + path
    params = {
        'api_key': '837e86c41f738f95ed4b63bd28dabae4',
        'language': 'ko-KR',
        # 검색한 영화 제목
        'query': title
    }

    response = requests.get(
        URL, params=params).json().get('results')

    # 검색한 영화가 없다면
    if len(response) == 0:
        # 값은 None
        return None

    url2 = 'https://api.themoviedb.org/3'
    # 검색한 영화의 id 값으로 주소 입력
    # 첫번째 영화의 id값 추출
    path2 = '/movie/'+str(response[0].get('id'))+'/recommendations'
    URL2 = url2 + path2
    params = {
        'api_key': '837e86c41f738f95ed4b63bd28dabae4',
        'language': 'ko-KR',
    }

    # 추천 영화 제목을 넣을 박스
    result = []
    response2 = requests.get(URL2, params=params).json().get('results')

    for i in response2:
        # 제목을 박스에 추가
        result.append(i.get('title'))

    # 결과값은 함수 밖으로 내보내 출력
    return result


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None


# 05. 출연진 및 연출진 데이터 조회 🐳
# 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
# 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
# `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.


def credits(title):
    pass

    url = 'https://api.themoviedb.org/3'
    path = '/search/movie'
    URL = url + path
    params = {
        'api_key': '837e86c41f738f95ed4b63bd28dabae4',
        'language': 'ko-KR',
        # 검색한 영화 제목
        'query': title
    }

    response = requests.get(
        URL, params=params).json().get('results')

    # 검색한 영화가 없다면
    if len(response) == 0:
        # 값은 None
        return None

    url2 = 'https://api.themoviedb.org/3'
    # 검색한 영화의 id 값으로 주소 입력
    # 첫번째 영화의 id값 추출
    path2 = '/movie/'+str(response[0].get('id'))+'/credits'
    URL2 = url2 + path2
    params = {
        'api_key': '837e86c41f738f95ed4b63bd28dabae4',
        'language': 'ko-KR',
    }

    response2 = requests.get(URL2, params=params).json()

    # cast, crew 각각 담을 박스
    cast_result = []
    crew_result = []

    # cast 값 추출
    cast = response2.get('cast')
    for i in cast:
        # 만일 cast_id값이 10 미만이라면
        if i.get('cast_id') < 10:
            # 박스에 이름 추가
            cast_result.append(i.get('name'))

    # crew 값 추출
    crew = response2.get('crew')
    for i in crew:
        # 연출 부서로 접근
        if i.get('department') == 'Directing':
            # 박스에 이름 추가
            crew_result.append(i.get('name'))

    # 딕셔너리 형태로 값 내보내기
    return {'cast': cast_result, 'crew': crew_result}


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
