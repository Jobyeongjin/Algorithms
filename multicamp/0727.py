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


# 유학 금지 🐳
# 문제 : 입력으로 주어진 단어를 정부가 검열을 하면 어떻게 변하는지를 출력한다.
#       즉, 단어에서 CAMBRIDGE에 포함된 알파벳을 모두 지운 뒤 출력한다. 항상 정답의 길이는 0보다 크다.
# 접근 : 검열하는 문자와 입력한 문자를 2중 for문으로 비교한 뒤, 검열 문자와 같다면 제거하고 출력

alpha = 'CAMBRIDGE'
word = list(input())

for i in alpha:
    for j in range(len(word)):
        if word[j] == i:
            word[j] = ''

for i in word:
    print(i, end='')


# 태보태보 총난타 🐳
# 문제 : 주먹의 잔상은 =로 시작하여 @로 끝나고, 잔상이 남지 않는 경우는 없다.
#       얼굴 형태가 (^0^) 꼴이고, 주먹의 잔상이 같은 곳에 위치하지 않는다.
#       첫째 줄에 왼손의 잔상의 수와 오른손의 잔상의 수를 출력한다.
# 접근 : 문자열로 받아 얼굴을 기준으로 나누고 '@' 카운팅

le, ri = input().split('0')

le_cnt = 0
for i in le:
    if i == '@':
        le_cnt += 1

ri_cnt = 0
for i in ri:
    if i == '@':
        ri_cnt += 1

print(le_cnt, ri_cnt)

# 또는
le, ri = input().split('0')

print(le.count('@'), ri.count('@'))


# 오타맨 고창영 🐳
# 문제 : 창영이가 오타를 낸 문장과 오타를 낸 위치가 주어졌을 때, 오타를 지운 문자열을 출력하는 프로그램을 작성하시오.
#       창영이는 오타를 반드시 1개만 낸다.
# 접근 : 오타낸 자리에서 문자열 슬라이싱

t = int(input())


for _ in range(1, t + 1):
    num, word = input().split()

    n = int(num)
    print(word[:n-1], word[n:], sep='')


# 음계 🐳
# 문제 : 1부터 8까지 차례대로 연주한다면 ascending, 8부터 1까지 차례대로 연주한다면 descending, 둘 다 아니라면 mixed 이다.
#       연주한 순서가 주어졌을 때, 이것이 ascending인지, descending인지, 아니면 mixed인지 판별하는 프로그램을 작성하시오.
# 접근 : 숫자 리스트를 만들어 입력된 숫자와 비교

n = list(map(int, input().split()))

num = [1, 2, 3, 4, 5, 6, 7, 8]

if n == num:
    print('ascending')
elif n == num[::-1]:
    print('descending')
else:
    print('mixed')


# 셀프 넘버 🐳🚨
# 문제 : -
# 접근 : -

def func(n):
    n = n + sum(map(int, str(n)))
    return n


non_self = set()
for i in range(1, 10001):
    non_self.add(func(i))

for i in range(1, 10001):
    if i not in non_self:
        print(i)


# 카드놀이 🐳
# 문제 : 0부터 9까지의 카드 10장을 가진 두 사람, 두 카드를 비교하여 높은 수가 나온 사람이 승리
#       승자는 승점 3점, 패자는 0, 비기면 모두 1점, 두 사람의 승점과 이긴 사람 출력하기
# 접근 : a, b 리스트를 비교하면서 카운팅(승점), 조건문으로 이긴 사람 출력

a = list(map(int, input().split()))
b = list(map(int, input().split()))

a_cnt = 0
b_cnt = 0
for i in range(10):
    if a[i] < b[i]:
        b_cnt += 3
    elif a[i] > b[i]:
        a_cnt += 3
    else:
        a_cnt += 1
        b_cnt += 1

print(a_cnt, b_cnt)

if a_cnt < b_cnt:
    print('B')
elif a_cnt > b_cnt:
    print('A')
elif a_cnt == b_cnt == 10:
    print('D')
else:
    for i in range(1, 11):
        if a[-i] < b[-i]:
            print('B')
            break
        elif a[-i] > b[-i]:
            print('A')
            break
        else:
            continue


# 세로읽기 🐳🚨
# 문제 : 총 다섯줄의 문자, 숫자 입력, 가로가 아닌 세로로 읽은 순서대로 글자를 공백없이 한 줄로 출력
# 접근 : -

# words = [input() for i in range(5)], 한 줄 코드
words = []
for i in range(5):
    word = input()
    words.append(word)

for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')
