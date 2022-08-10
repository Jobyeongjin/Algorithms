# 삼각형 외우기 🐳
# 문제 : 삼각형의 종류 구분하기

import sys
angle = [int(input()) for _ in range(3)]

total = sum(angle)
if total == 180:
    if angle[0] == angle[1] == angle[2] == 60:
        print('Equilateral')
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
        print('Isosceles')
    else:
        print('Scalene')
else:
    print('Error')


# 꼬리를 무는 숫자 나열 🚨 🐳
# 문제 : 두 수 사이의 직각거리 구하기


# 콘테스트 🐳
# 문제 : 참가자 10명 중 득점이 높은 3명의 점수를 합산하기

W = [int(input().strip()) for _ in range(10)]
K = [int(input().strip()) for _ in range(10)]
W.sort(reverse=True)
K.sort(reverse=True)

print(W[0] + W[1] + W[2], end=' ')
print(K[0] + K[1] + K[2])


# 소가 길을 건너간 이유 1 🐳
# 문제 : 길을 건너간 소의 최소 횟수 구하기

N = int(input())

move = [-1] * N
cnt = 0
for _ in range(N):
    cow, position = map(int, input().split())

    if move[cow] == -1:
        move[cow] = position
    else:
        if move[cow] != position:
            cnt += 1
            move[cow] = position

print(cnt)

# 값은 동일하지만 실패
N = int(input())

move = {}
for _ in range(N):
    cow, position = map(int, input().split())

    if cow in move:
        move[cow] += 1
    else:
        move[cow] = 1

total = 0
for i in move.values():
    if i % 2 == 0:
        total += i / 2

print(total)


# 행복한지 슬픈지 🐳
# 문제 : 입력된 문자 메세지에서 이모티콘을 찾아 전체적인 분위기만 구하기

WORD = input()
HAPPY = WORD.count(':-)')
SAD = WORD.count(':-(')

if HAPPY == 0 and SAD == 0:
    print('none')
elif HAPPY == SAD:
    print('unsure')
elif HAPPY > SAD:
    print('happy')
elif HAPPY < SAD:
    print('sad')


# 바이러스 🐳
# 문제 : 바이러스에 걸린 컴퓨터와 인접한 컴퓨터의 개수 구하기

N = int(input())
M = int(input())

JOIN = [[] for _ in range(N + 1)]

visited = [0] * (N + 1)

for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)


def DFS(v):
    stack = [v]
    visited[v] = 1

    while stack:
        cur = stack.pop()

        for x in JOIN[cur]:
            if not visited[x]:
                visited[x] = 1
                stack.append(x)


DFS(1)
total = 0
for i in visited:
    if i == 1:
        total += 1

print(total - 1)


# 연결 요소의 개수 🐳
# 문제 : 연결 요소의 개수 구하기

# sys.getrecursionlimit()을 활용해 파이썬 최대 재귀 깊이 확인, 백준은 기본 1000으로 설정 🚨
sys.setrecursionlimit(10000)  # 재귀허용치를 1000 -> 10000으로 변경
input = sys.stdin.readline

N, M = map(int, input().split())

JOIN = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0] * (N + 1)


def DFS(v):
    visited[v] = 1

    for d in JOIN[v]:
        if not visited[d]:
            DFS(d)


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)


# 촌수계산 🐳
# 문제 : 여러 사람에 대한 관계가 주어질 때, 두사람 간의 촌수 구하기
