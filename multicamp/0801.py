# 카드1 🐳
# 문제 : N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
#       이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
#       N이 주어졌을 때, 버린 카드들을 순서대로 출력하고, 마지막에 남게 되는 카드를 출력하는 프로그램을 작성하시오.


import sys
from sys import stdin
n = int(input())
cards = list(range(1, n + 1))

while len(cards) > 1:
    print(cards.pop(0), end=' ')  # 카드의 첫번째 요소를 없애면서 출력
    cards.append(cards.pop(0))  # 다음 요소를 없애면서 추가 (맨 뒤쪽으로)

print(cards[0])  # 마지막 남은 요소


# 자료구조는 정말 최고야 🚨 🐳

input = sys.stdin.readline

N, M = map(int, input().split())
answer = True

for i in range(M):
    bookcount = int(input())  # 더미 수
    bookstack = list(map(int, input().split()))  # 책 넘버 리스트

    for k in range(bookcount - 1):
        if bookstack[k] < bookstack[k + 1]:  # 두 수 비교
            answer = False

if answer:
    print('Yes')
else:
    print('No')


# 괄호 🐳
# 문제 : 그 중에서 괄호의 모양이 바르게 구성된 문자열을 올바른 괄호 문자열(Valid PS, VPS)이라고 부른다.
#       여러분은 입력으로 주어진 괄호 문자열이 VPS 인지 아닌지를 판단해서 그 결과를 YES 와 NO 로 나타내어야 한다.
#       출력은 표준 출력을 사용한다. 만일 입력 괄호 문자열이 올바른 괄호 문자열(VPS)이면 “YES”, 아니면 “NO”를 한 줄에 하나씩 차례대로 출력해야 한다.

n = int(input())

for _ in range(n):
    bracket = input()

    stack = []
    for i in bracket:
        if stack:  # 스택 안에 요소가 있으면
            if i == '(':  # '(' 라면 스택에 추가
                stack.append(i)
            elif i == ')':
                if stack[-1] == '(':  # 스택의 마지막 요소가 ')' 라면
                    stack.pop()  # 스택 안에 '(' 삭제
                else:
                    stack.append(i)
        else:  # 스택 안에 요소가 없으면
            stack.append(i)

    if stack:  # 스택에 요소가 남아있다면
        print('NO')
    else:
        print('YES')


# KMP는 왜 KMP일까? 🐳
# 문제 : 긴 형태의 알고리즘 이름이 주어졌을 때, 이를 짧은 형태로 바꾸어 출력하는 프로그램을 작성하시오.
# 입력 : Knuth-Morris-Pratt
# 츌력 : KMP

word = input().split('-')


for i in word:
    print(i[0], end='')


# 우유 축제 🐳
# 문제 : 영학이가 마실 수 있는 우유의 최대 개수를 구하여라.
#       영학이는 딸기(0) > 초코(1) > 바나나(2) 순으로 마신다.
# 입력 : 7
#       0 1 2 0 1 2 0
# 출력 : 7

n = int(input())
milk = list(map(int, input().split()))

cnt = 0
total = 0
for i in range(len(milk)):  # 리스트 인덱스 값 비교
    if milk[i] == cnt:
        cnt += 1
        total += 1

    if cnt > 2:
        cnt = 0

print(total)


# 저항 🐳
# 문제 : 전자 제품에는 저항이 들어간다. 저항은 색 3개를 이용해서 그 저항이 몇 옴인지 나타낸다. 처음 색 2개는 저항의 값이고, 마지막 색은 곱해야 하는 값이다. 저항의 값은 다음 표를 이용해서 구한다.

colors = {
    'black': [0, 1],
    'brown': [1, 10],
    'red': [2, 100],
    'orange': [3, 1000],
    'yellow': [4, 10000],
    'green': [5, 100000],
    'blue': [6, 1000000],
    'violet': [7, 10000000],
    'grey': [8, 100000000],
    'white': [9, 1000000000]
}

color = []
for _ in range(3):
    n = input()
    color.append(n)

value = str(colors[color[0]][0]) + str(colors[color[1]][0])  # 해당 인덱스 값 더하기
result = int(value) * colors[color[2]][1]

print(result)


# 고무오리 디버깅 🐳
# 문제 : 첫 번째 줄에 "고무오리 디버깅 시작"이라고 주어진다. 두 번째 줄부터 "고무오리" 또는 "문제"가 주어진다. 이는 "고무오리 디버깅 끝"이 주어질 때까지 반복한다.
# 출력 : 고무오리 디버깅이 끝날 때, 주어진 문제를 수진이가 해결하였는지 여부에 따라 남은 문제 없이 모든 문제를 해결하였으면 "고무오리야 사랑해"을 출력하고 하나라도 문제가 남았다면 "힝구"를 출력하라.

stack = []
while True:
    rubber_duck = input()

    if rubber_duck == '문제':  # '문제' 를 스택에 추가
        stack.append(rubber_duck)
    elif rubber_duck == '고무오리':  # 러버덕이 '고무오리' 라면
        if stack:  # 스택 안에 '문제' 가 있으면 제거
            stack.pop()
        else:  # 없으면 '문제' 2개 추가
            stack.append('문제')
            stack.append('문제')
    elif rubber_duck == '고무오리 디버깅 끝':
        break

if stack:
    print('힝구')
else:
    print('고무오리야 사랑해')


# 배부른 마라토너 🐳
# 문제 : 모두가 참가하고 싶어서 안달인데 이런 백준 마라톤 대회에 참가해 놓고 완주하지 못한 배부른 참가자 한 명은 누굴까?

n = int(stdin.readline())

people = {}
# 참가자 입력
for _ in range(n):
    name = stdin.readline()
    if name in people:
        people[name] += 1
    else:
        people[name] = 1

# 완주자 입력
for i in range(n - 1):
    name = stdin.readline()
    if people[name] == 1:
        del people[name]
    elif name in people:
        people[name] -= 1

print(*people)
