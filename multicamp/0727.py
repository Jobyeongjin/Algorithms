# 음양 더하기 🐳
# 문제 : 정수를 담은 리스트와 불리언을 담은 리스트를 비교한다.
#       참이면 더하고, 거짓이면 빼서 결과값 출력

def solution(absolutes, signs):

    result = 0
    for i in range(len(signs)):
        if signs[i] == True:
            result += absolutes[i]
        else:
            result -= absolutes[i]

    return result


# 단어공부 🐳
# 문제 : 대소문자로 구성된 단어에서 가장 많이 사용된 알파벳 구하기
#       가장 많이 사용된 알파벳이 여러 개라면 '?' 출력

word = input().upper()  # MISSISSIPI
word_list = list(set(word))  # S I P M

result = []

for i in word_list:
    cnt = word.count(i)  # 4411
    result.append(cnt)

max_ = max(result)
if result.count(max_) >= 2:
    print('?')
else:
    print(word_list[result.index(max_)])


# 크로아티아 알파벳 🐳
# 문제 : 해당 크로아티아 문자로 변환하고, 변환한 문자열의 글자수를 출력

word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:
    word = word.replace(i, '*')

print(len(word))


# 슈퍼 마리오 🐳
# 문제 : 10개가 일렬로 놓인 버섯의 점수를 먹으면서, 점수가 최대한 100에 가깝게 만들기

mushroom = []  # 10 20 30 40 50 60 70 80 90 100
for _ in range(10):
    mushroom.append(int(input()))

result = 0
score = 0
for i in mushroom:
    score += i
    if abs(score-100) <= abs(result-100):
        result = score

print(result)

# 또는

# for 점수 in 점수리스트:
#     누적점수 += 점수

#     차이 = abs(100 - 누적점수)

#     if 차이 <= 가장작은차이:
#         가장작은차이 = 차이
#         가장큰누적점수 = 누적점수

n = 10  # 10개의 점수
scores = []  # 점수 저장 리스트
for i in range(n):
    score = int(input())  # 숫자형 입력
    scores.append(score)

sum_ = 0
min_ = 10e9  # 가장 큰 값
max_score = 0  # 가장 큰 누적점수
for i in range(n):
    sum_ = sum_ + scores[i]  # 누적 합

    # 누적 점수와 100의 차이
    diff = abs(100 - sum_)

    # 차이가 이전의 가장 작은차이보다 작을 때
    if diff < min_diff:
        # 가장 작은 차이와 가장 큰 누적점수를 갱신
        min_diff = diff
        max_score = sum_

print(max_score)


# 덩치 🐳
# 문제 : 몸무게와 키로 구성된 덩치를 비교하기, 둘다 커야 덩치가 큰 사람

n = int(input())  # 5

student = []  # (wei, hei), (wei, hei), ...

for _ in range(n):
    wei, hei = map(int, input().split())
    student.append((wei, hei))

for i in student:
    rank = 1
    for j in student:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=' ')

# 또는

# 사람의 수
n = int(input())

list_ = []
# 사람의 몸무게와 키 입력
for i in range(n):
    wei, hei = list(map(int, input().split()))
    list_.append((wei, hei))

ranks = [0] * n
# 모든 사람을 비교하기 위한 이중반복문
for a in range(n):
    # 기준이 되는 사람
    A = list_[a]
    for b in range(n):
        # 비교가 되는 사람
        B = list_[b]

        if A[0] > B[0] and A[1] > B[1]:
            ranks[b] += 1

for rank in ranks:
    print(rank + 1, end=' ')
