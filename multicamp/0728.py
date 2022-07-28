# 나머지 🐳
# 문제 : 42로 나눴을 때, 서로 다른 나머지가 몇 개인지 출력
# 접근 : 42로 나눈 나머지를 구하고, 중복 값을 제거해 남은 개수를 구함

arr = []
for i in range(10):
    n = int(input())
    n_ = n % 42
    arr.append(n_)

print(len(set(arr)))


# SASA 모형을 만들어보자 🐳
# 문제 : SASA 모형 개수의 최댓값을 출력하기
#       모형 1개는 S, A가 각각 2개씩 필요
# 접근 : 더 작은 수를 찾아서 모형에 필요한 개수인 2로 나누기

S, A = map(int, input().split())

result = min(S, A)

print(result // 2)


# 쉽게 푸는 문제 🐳🚨
# 문제 : 수열(12233344445...)을 만들고 해당 구간에 속하는 숫자의 합 구하기
# 접근 : d

a, b = map(int, input().split())

data = [0]
sum = 0
# 수열 만들기
for i in range(1, b + 1):
    for j in range(i):
        data.append(i)

for i in range(a, b + 1):
    sum += data[i]

print(sum)


# 뒤집힌 덧셈 🐳
# 문제 : 두 양의 정수 X와 Y가 주어졌을 때,
#       Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오
# 접근 : 문자열로 입력받아 뒤집어서 더하고, 다시 뒤집기

x, y = input().split()

x_rev = x[::-1]
y_rev = y[::-1]

sum_ = str(int(x_rev) + int(y_rev))
print(int(sum_[::-1]))


# 다이얼 🐳🚨
# 문제 : 첫째 줄에 다이얼을 걸기 위해 필요한 최소 시간을 출력
# 접근 : 입력받은 문자를 리스트 안에서 찾고, 해당 인덱스 값으로 더해가기

number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = list(input())

time = 0

for i in alpha:
    for j in number:
        if i in j:
            time += number.index(j) + 3  # 인덱스는 0부터, 알파벳은 3부터

print(time)


# 숫자 카드 2 🐳🚨
# 문제 : 상근이는 숫자 카드 N개를 가지고 있다. 정수 M개가 주어졌을 때,
#       이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
# 접근 : 딕셔너리 형태로 담은 카드 리스트와 정수를 비교해 키의 밸류값인 카드의 수를 출력

n = int(input())  # 상근이의 카드
cards = list(map(int, input().split()))
cards.sort()

m = int(input())  # 비교할 정수
targets = list(map(int, input().split()))

dict_ = {}


# 카드 수를 딕셔너리에 담기 🐳
for i in cards:
    if i in dict_:
        dict_[i] += 1  # 딕셔너리 키로 접근, 밸류에 1씩 추가
    else:
        dict_[i] = 1

# 정수와 비교
for i in range(m):
    if targets[i] in dict_:
        print(dict_[targets[i]], end=' ')  # 딕셔너리 키로 접근해 밸류값 출력
    else:
        print(0, end=' ')


# 회사에 있는 사람 🐳
# 문제 : 상근이는 모든 사람의 출입카드 시스템의 로그를 가지고 있다. 이 로그는 어떤 사람이 회사에 들어왔는지, 나갔는지가 기록되어져 있다.
#       로그가 주어졌을 때, 현재 회사에 있는 모든 사람을 구하는 프로그램을 작성하시오.
# 접근 : 딕셔너리에 이름과 로그를 추가하고 퇴근하면 요소 제거, 키값만 출력

n = int(input())

check_list = {}
for _ in range(n):
    name, check = input().split()

    if check == 'enter':
        check_list[name] = 'enter'

    else:
        del check_list[name]


for i in sorted(check_list.keys(), reverse=True):
    print(i)

# 베스트셀러 🐳
# 문제 : 오늘 하루 동안 팔린 책의 제목이 입력으로 들어왔을 때,
#       가장 많이 팔린 책의 제목을 출력하는 프로그램을 작성하시오.
#       첫째 줄에 가장 많이 팔린 책의 제목을 출력한다.
#       만약 가장 많이 팔린 책이 여러 개일 경우에는 사전 순으로 가장 앞서는 제목을 출력한다.
# 접근 : 딕셔너리에 책 제목과 팔린 수를 입력, 가장 많이 팔린 수를 변수로 저장
#       가장 많이 팔린 책과 같다면 리스트에 추가

n = int(input())

books = {}
for _ in range(n):
    title = input()

    if title in books:
        books[title] += 1
    else:
        books[title] = 1

title_list = []

max_ = max(books.values())
for i in books:
    if max_ == books[i]:
        title_list.append(i)

title_list.sort()
print(title_list[0])


# 듣보잡 🐳
# 문제 : 듣보잡의 수와 그 명단을 사전순으로 출력한다.
# 접근 : 각각 집합 자료형에 담아 중복되는 값을 찾고, 알파벳순으로 정렬

n, m = map(int, input().split())

a = set()
for i in range(n):
    a.add(input())  # set은 add로 요소 추가

b = set()
for i in range(m):
    b.add(input())

result = sorted(list(a & b))  # 교집합, 중복되는 문자열 구하기

print(len(result))

for i in result:
    print(i)


# 카드 🐳
# 문제 : 준규가 가지고 있는 카드가 주어졌을 때, 가장 많이 가지고 있는 정수를 구하는 프로그램을 작성하시오.
#       만약, 가장 많이 가지고 있는 정수가 여러 가지라면, 작은 것을 출력한다.
# 접근 : 딕셔너리 안에 카드를 넣고 중복되는 값은 1씩 추가(밸류), 가장 큰 수를 변수로 저장
#       딕셔너리 안에 가장 큰 수를 찾아 키값을 리스트에 담기

n = int(input())

cards = {}
for i in range(n):
    card = int(input())

    if card in cards:
        cards[card] += 1
    else:
        cards[card] = 1

card_num = []
max_ = max(cards.values())
for i in cards:
    if max_ == cards[i]:
        card_num.append(i)

card_num.sort()
print(card_num[0])
