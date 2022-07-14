# 14. 문자열 word가 주어질 때, 해당 문자열에서 a의 개수 구하기 / count() 사용금지
# 입력 : apple
# 출력 : 1

word = 'apple'
result = 0

for i in word:
    if i == 'a':
        result += 1

print(result)


# 15. 문자열 word가 주어질 때, 해당 문자열에서 a가 처음으로 등장하는 위치 출력하기 (a가 없는 경우 -1 출력) / find(), index() 사용금지
# 입력 : banana
# 출력 : 1

word = 'banana'

for i in range(len(word)):  # 문자로 순회가 아닌 인덱스로 접근 / range(6) => 0 ~ 5
    if word[i] == 'a':
        print(i)
        break
else:
    print(-1)


# 15-1. 리스트에 담기

word = 'banana'
result = []

for i in range(len(word)):
    if word[i] == 'a':
        result.append(i)

print(result)

# 15-2. 그때 그때 출력

word = 'banana'
result = []

for idx in range(len(word)):
    if word[idx] == 'a':
        print(idx, end=' ')


# 16. 문자열 word가 주어질 때, 해당 문자열에서 모음의 갯수 찾기 (모음 : a, e, i, o, u)
# 입력 : apple
# 출력 : 2

word = 'apple'
result = 0

for i in word:
    # 'aeiou'
    if i in ['a', 'e', 'i', 'o', 'u']:  # 해당 리스트의 값이라면 ?
        result += 1  # 결과값에 1씩 추가

print(result)


# 17. 소문자로 구성된 문자열 word가 주어질 때, 모두 대문자로 바꾸기 / .upper(), .swapcase() 사용 금지
# 입력 : banana
# 출력 : BANANA

word = 'banana'
result = ''  # 결과값을 받을 빈 공간

for i in word:
    # 아스키코드(알파벳은 숫자로) 변환 / ord() > 반대는 chr(), 대문자와 소문자의 차이는 32
    result += str(chr(ord(i) - 32))

print(result)

# 또는

word = 'banana'
result = ''

for char in word:
    # 1. 알파벳을 숫자로 바꾸고
    number = ord(char)
    # 2. 그 숫자를 -32를 하고
    number = number-32
    # 3. 다시 숫자를 알파벳으로 바꾼다.
    result += chr(number)

print(result)

# 한 줄로 하면

for char in word:
    print(chr(ord(char)-32), end='')


# 18. 문자열 word가 주어질 떄, distionary를 활용해서 해당 문자열에서 등장한 모든 알파벳 개수 구하기
# 입력 : banana
# 출력 : b 1, a 3, n 2 줄 바꿔서

word = 'banana'
result = dict()  # 또는 {}, 빈 딕셔너리 생성

for i in word:
    if i in result:  # 만일 resilt에 i가 있다면 ?
        result[i] += 1  # 1씩 추가
    else:  # 딕셔너리 안에 i가 없다면 ?
        result[i] = 1  # 해당 값에 1 추가

for x, y in result.items():  # 딕셔너리 안에 있는 키, 밸류 값만 가져오기
    print(x, y)

# 또는

word = 'banana'
result = {}

for i in word:
    # result['a'] 없으면 KeyError
    # result.get('a') 기본값이 None
    # result.get('a', 0) 기본값이 0
    result[i] = result.get(i, 0) + 1

# 출력 부분
for key in result:
    print(key, result[key])
