# 05. 출연진 및 연출진 데이터 조회
# 제공된 영화 제목을 검색하여 해당 영화의 출연진(`cast`) 그리고 스태프(`crew`) 중 연출진으로 구성된 목록만을 출력합니다.
# requests 라이브러리를 활용하여 TMDB에서 영화제목으로 영화를 검색(Search Movies)합니다.
# 응답 받은 결과 중 첫번째 영화의 id 값을 활용하여 TMDB에서 해당 영화에 대한 출연진과 스태프 목록(Get Credits)을 가져옵니다.
# 출연진 중 `cast_id` 값이 `10 미만`인 출연진만 추출하고, 연출진은 부서(`department`)가 `Directing` 인 데이터만 추출합니다.
# `cast` 와 `directing` 으로 구성된 딕셔너리에 추출된 값을 리스트로 출력하는 함수를 작성합니다.

import requests
from pprint import pprint


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
