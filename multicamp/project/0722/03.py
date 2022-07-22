# 03. 특정 조건에 맞는 인기 영화 조회
# 인기 영화 목록을 평점이 높은 순으로 5개의 정렬하여 영화 데이터 목록을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 현재 인기 있는 영화 목록(Get Populations) 데이터를 요청합니다.
# 응답 받은 데이터 중 평점(`vote_average`)이 높은 영화 5개의 정보를 리스트로 반환하는 함수를 작성합니다.


import requests
from pprint import pprint

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
