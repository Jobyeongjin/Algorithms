# JSON 데이터 활용 - 영화 다중 정보 활용
# 영화 데이터를 활용하여 필요한 정보로만 구성된 리스트를 출력하기
# 전체 영화 정보는 평점 높은 20개의 영화 데이터

import json
from pprint import pprint


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
