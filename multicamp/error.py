# 03. [오류해결] 입력 받기
# 문제 : 두 수를 input으로 받아 합을 구하는 코드

from pprint import pprint
numbers = input().split()

print(sum(numbers))

# 풀이 : 넘버스라는 변수에 값을 입력받는데 들어오는 값은 '문자열' 이고, 문자열인 두 수를 나눈 것이다.
#       sum() 함수는 숫자를 더해주는 것이기 때문에 넘버스를 숫자형으로 바꿔줘야 한다.
# 원인 : 타입 에러(TypeError)

numbers = map(int, input().split())

print(sum(numbers))


# 04. [오류해결] 입력 받기
# 문제 : 문자열을 입력받아 단어별로 나누는 코드

words = list(map(int, input().split()))

print(words)

# 풀이 : 워드스라는 변수에 값을 리스트로 입력받는데 '숫자형' 이고, 공백을 기준으로 나누게 돤다.
#       문제는 문자형을 나누는 것이기에 숫자형으로 변환할 필요가 없다.
# 원인 : 타입 에러(TypeError)

words = list(input().split())

print(words)


# 05. [오류 해결] 숫자의 길이 구하기
# 문제 : 숫자의 길이를 구하는 코드

number = 22020718

print(len(number))

# 풀이 : 넘버라는 변수에 값은 '숫자형' 이고,
#       len() 함수는 문자형의 길이를 반환하기 때문에 문자형으로 변환해줘야 한다.
# 원인 : 타입 에러(TypeError)

number = 22020718

print(len(str(number)))


# 06. [오류 해결] 1부터 N까지의 2의 곱 저장하기
# 문제 : 1부터 N까지의 2의 곱해서 변수에 저장하는 코드

N = 10
answer = ()

for number in range(N + 1):
    answer.append(number * 2)

print(answer)

# 풀이 : 엔이라는 숫자형 변수를 반복문을 돌려 정답이라는 변수에 저장하는 문제인데,
#       정답이라는 변수는 '튜플' 이고, append() 함수는 리스트에 요소를 추가하는 함수이다.
# 원인 : 속성 에러(AttributeError)


# 07. [오류 해결] 평균 구하기
# 문제 : 평균을 구하는 논리적으로 오류가 있는 코드

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
count += 1

print(total // count)

# 풀이 : 1~10까지의 리스트를 반복문을 돌려 토탈에는 숫자의 총합을, 카운트에는 총수를 넣고 나눠야 하는데,
#       카운트가 반복문 밖에 있기 때문에 반복이 끝나고서야 실행하게 된다.

number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
    count += 1

print(total // count)


# 08. [오류 해결] 모음의 개수 찾기
# 문제 : 문자열에서 모음의 개수를 찾는 코드

word = 'HappyHacking'

count = 0

for char in word:
    if char == 'a' or 'e' or 'i' or 'o' or 'u':
        count += 1

print(count)

# 풀이 : 오류없이 돌아가지만 카운트가 원하는 모음을 세는 것이 아닌 계속해서 늘어나는 걸 볼 수 있다.
#       모음이 있는지를 확인해야 하기 때문에 모음 리스트 안에서 찾는다.

word = 'HappyHacking'

count = 0

for char in word:
    if char in ['a', 'e', 'i', 'o', 'u']:
        count += 1

print(count)


# 09. [오류 해결] 과일 개수 구하기
# 문제 : 과일 개수를 구하는 논리적 오류가 있는 코드의 일부분

fruits = [
    "Soursop",
    "Grapefruit",
    "Apricot",
    "Juniper berry",
    "Feijoa",
    "Blackcurrant",
    "Cantaloupe",
    "Salal berry",
]

fruit_count = {}

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count = {fruit: 1}
    else:
        fruit_count[fruit] += 1

pprint(fruit_count)

# 풀이 : 리스트인 과일들을 딕셔너리에 담아야 하고 밸류 값을 추가해야 하는데,
#       조건문에서 키와 밸류 값을 넣고 있으니, 조건문을 아래와 같이 변경해야 한다.

for fruit in fruits:
    if fruit not in fruit_count:
        fruit_count[fruit] = 1
    else:
        fruit_count[fruit] += 1


# 10. [오류 해결] 더 큰 최댓값 찾기
# 문제 : 리스트에서 최댓값을 구하는 코드

number_list = [1, 23, 9, 6, 91, 59, 29]
max = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")

# 풀이 : 변수 이름이 max로 지정이 되어있었고,
#       함수는 변수 이름으로 지정할 수 없다.

number_list = [1, 23, 9, 6, 91, 59, 29]
max1 = max(number_list)

number_list2 = [2, 5, 100, 20, 50, 10, 91, 82]
max2 = max(number_list2)

if max1 > max2:
    print("첫 번째 리스트의 최댓값이 더 큽니다.")

elif max1 < max2:
    print("두 번째 리스트의 최댓값이 더 큽니다.")

else:
    print("첫 번째 리스트의 최댓값과 두 번째 리스트의 최댓값은 같습니다.")


# 11. [오류 해결] 영화 정보 찾기
# 문제 : 영화의 장르id를 장르 이름으로 바꿔서 영화 정보를 출력하는 코드


def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }


if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))

# 풀이 : new_movie_info 변수의 값을 밖으로 내보내야 하기 때문에 리턴을 추가
# 원인 : None


def movie_info(movie, genres):
    genres_names = []
    genre_ids = movie["genre_ids"]
    for genre_id in genre_ids:
        for genre in genres:
            if genre_id == genre["id"]:
                genre_name = genre["name"]
                genres_names.append(genre_name)

    new_movie_info = {
        "genre_names": genres_names,
        "id": movie["id"],
        "overview": movie["overview"],
        "title": movie["title"],
        "vote_average": movie["vote_average"],
    }
    return new_movie_info


if __name__ == "__main__":
    movie = {
        "adult": False,
        "backdrop_path": "/tXHpvlr5F7gV5DwgS7M5HBrUi2C.jpg",
        "genre_ids": [18, 80],
        "id": 278,
        "original_language": "en",
        "original_title": "The Shawshank Redemption",
        "overview": "촉망받는 은행 간부 앤디 듀프레인은 아내와 그녀의 정부를 살해했다는 누명을 쓴다. 주변의 증언과 살해 현장의 그럴듯한 증거들로 그는 종신형을 선고받고 악질범들만 수용한다는 지옥같은 교도소 쇼생크로 향한다. 인간 말종 쓰레기들만 모인 그곳에서 그는 이루 말할 수 없는 억압과 짐승보다 못한 취급을 당한다. 그러던 어느 날, 간수의 세금을 면제받게 해 준 덕분에 그는 일약 교도소의 비공식 회계사로 일하게 된다. 그 와중에 교도소 소장은 죄수들을 이리저리 부리면서 검은 돈을 긁어 모으고 앤디는 이 돈을 세탁하여 불려주면서 그의 돈을 관리하는데...",
        "popularity": 67.931,
        "poster_path": "/3hO6DIGRBaJQj2NLEYBMwpcz88D.jpg",
        "release_date": "1995-01-28",
        "title": "쇼생크 탈출",
        "video": False,
        "vote_average": 8.7,
        "vote_count": 18040,
    }

    genres_list = [
        {"id": 28, "name": "Action"},
        {"id": 12, "name": "Adventure"},
        {"id": 16, "name": "Animation"},
        {"id": 35, "name": "Comedy"},
        {"id": 80, "name": "Crime"},
        {"id": 99, "name": "Documentary"},
        {"id": 18, "name": "Drama"},
        {"id": 10751, "name": "Family"},
        {"id": 14, "name": "Fantasy"},
        {"id": 36, "name": "History"},
        {"id": 27, "name": "Horror"},
        {"id": 10402, "name": "Music"},
        {"id": 9648, "name": "Mystery"},
        {"id": 10749, "name": "Romance"},
        {"id": 878, "name": "Science Fiction"},
        {"id": 10770, "name": "TV Movie"},
        {"id": 53, "name": "Thriller"},
        {"id": 10752, "name": "War"},
        {"id": 37, "name": "Western"},
    ]

    pprint(movie_info(movie, genres_list))
