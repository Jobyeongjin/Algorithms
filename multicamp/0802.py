# 대칭 차집합 🐳
# 문제 : A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.
#       예를 들어, A = { 1, 2, 4 } 이고, B = { 2, 3, 4, 5, 6 } 라고 할 때,  A-B = { 1 } 이고, B-A = { 3, 5, 6 } 이므로, 대칭 차집합의 원소의 개수는 1 + 3 = 4개이다.

from sys import stdin
import heapq

n, m = map(int, input().split())
a = set(map(int, input().split()))  # set을 이용한 차집합
b = set(map(int, input().split()))

print(len(a - b) + len(b - a))  # 대칭 차집합의 원소 개수


# 절대값 힙 🐳
# 문제 : 배열에 정수 x (x ≠ 0)를 넣는다. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는, 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
#       프로그램은 처음에 비어있는 배열에서 시작하게 된다.
# 출력 : 입력에서 0이 주어진 회수만큼 답을 출력한다. 만약 배열이 비어 있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 된다.

n = int(stdin.readline())

heap = []
for i in range(n):
    num = int(stdin.readline())

    if num == 0:  # 0 이라면
        if heap:
            print(heapq.heappop(heap)[1])  # 튜플 안의 입력 값인 두번째 요소 삭제
        else:
            print(0)
    else:
        heapq.heappush(heap, (abs(num), num))  # heap에 절대값 넣기, 튜플 형태


# TGN 🐳
# 문제 : 광고 효과가 주어졌을 때, 광고를 해야할지 말아야할지 결정하는 프로그램을 작성하시오.
# 출력 : 각 테스트 케이스에 대해서, 광고를 해야 하면 "advertise", 하지 않아야 하면 "do not advertise", 광고를 해도 수익이 차이가 없다면 "does not matter"를 출력한다.

n = int(input())

for i in range(n):
    r, e, c = map(int, input().split())

    margin = e - c
    if r < margin:
        print('advertise')
    elif r == margin:
        print('does not matter')
    else:
        print('do not advertise')


# 수 정렬하기 🐳
# 문제 : N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

n = int(input())

arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)

sort_ = sorted(arr)

for i in sort_:
    print(i)


# 숫자 문자열과 영단어 🐳
# 문제 : 이렇게 숫자의 일부 자릿수가 영단어로 바뀌어졌거나, 혹은 바뀌지 않고 그대로인 문자열 s가 매개변수로 주어집니다. s가 의미하는 원래 숫자를 return 하도록 solution 함수를 완성해주세요.

def solution(s):
    answer = s

    note = {
        'zero': '0',
        'one': '1',
        'two': '2',
        'three': '3',
        'four': '4',
        'five': '5',
        'six': '6',
        'seven': '7',
        'eight': '8',
        'nine': '9'
    }

    for i in note:
        answer = answer.replace(i, note[i])

    return int(answer)


# 균형잡힌 세상 🐳 🚨
# 문제 : 정민이의 임무는 어떤 문자열이 주어졌을 때, 괄호들의 균형이 잘 맞춰져 있는지 판단하는 프로그램을 짜는 것이다.
#       문자열에 포함되는 괄호는 소괄호("()") 와 대괄호("[]")로 2종류이고, 문자열이 균형을 이루는 조건은 아래와 같다.
# 출력 : 각 줄마다 해당 문자열이 균형을 이루고 있으면 "yes"를, 아니면 "no"를 출력한다.

while True:
    word = input()

    if word == '.':
        break

    stack = []
    for i in word:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) != 0 and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']':
            if len(stack) != 0 and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break

    if stack:
        print('no')
    else:
        print('yes')


# 암기왕 🐳
# 문제 : 동규를 도와주기 위해 ‘수첩2’에 적혀있는 순서대로, 각각의 수에 대하여, ‘수첩1’에 있으면 1을, 없으면 0을 출력하는 프로그램을 작성해보자.

input = stdin.readline

for _ in range(int(input())):
    n = int(input())
    n_list = set(map(int, input().split()))
    m = int(input())
    m_list = list(map(int, input().split()))

    for i in m_list:
        print(1 if i in n_list else 0)


# 인사성 밝은 곰곰이 🐳
# 문제 : ENTER는 새로운 사람이 채팅방에 입장했음을 나타낸다. 그 외는 채팅을 입력한 유저의 닉네임을 나타낸다. 닉네임은 숫자 또는 영문 대소문자로 구성되어 있다.
#       새로운 사람이 입장한 이후 처음 채팅을 입력하는 사람은 반드시 곰곰티콘으로 인사를 한다. 그 외의 기록은 곰곰티콘을 쓰지 않은 평범한 채팅 기록이다.
#       채팅 기록 중 곰곰티콘이 사용된 횟수를 구해보자!

n = int(input())

dic = {}
cnt = 0
for _ in range(n):
    name = input()

    if name == 'ENTER':
        for k, v in dic.items():
            if v == 1:
                cnt += 1
        dic = {}
    else:
        if name not in dic:
            dic[name] = 1

for k, v in dic.items():
    if v == 1:
        cnt += 1

print(cnt)
