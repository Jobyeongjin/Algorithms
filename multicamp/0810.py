# 삼각형 외우기 🐳
# 문제 : 삼각형의 종류 구분하기

from collections import deque
import sys
angle = [int(input()) for _ in range(3)]

total = sum(angle)
if total == 180:  # 세 각의 합이 180이라면 조건대로 출력
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
W.sort(reverse=True)  # 득점이 높은 순(내림차순)으로 정렬
K.sort(reverse=True)

print(W[0] + W[1] + W[2], end=' ')
print(K[0] + K[1] + K[2])


# 소가 길을 건너간 이유 1 🐳
# 문제 : 길을 건너간 소의 최소 횟수 구하기

N = int(input())

move = [-1] * (N + 1)
cnt = 0
for _ in range(N):
    cow, position = map(int, input().split())

    if move[cow] == -1:  # 해당 인덱스에 값을 변경
        move[cow] = position
    else:
        if move[cow] != position:  # 값이 다르면 이동했으니 카운팅
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
HAPPY = WORD.count(':-)')  # 문자열 안에서 해당 문자가 몇 개인지 카운팅
SAD = WORD.count(':-(')

if HAPPY == 0 and SAD == 0:  # 조건 비교
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

JOIN = [[] for _ in range(N + 1)]  # 인접 리스트 생성

for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)  # 해당 인덱스 값에 추가
    JOIN[v2].append(v1)

visited = [0] * (N + 1)  # 방문 여부 확인


def DFS(v):
    stack = [v]  # 돌아갈 곳을 기록하는 리스트
    visited[v] = 1  # 방문 처리

    while stack:  # 스택이 비어있을 때까지 반복
        cur = stack.pop()  # 정점을 빼면서 변수에 저장

        for d in JOIN[cur]:  # 뺀 정점과 인접한 모든 정점 확인
            if not visited[d]:  # 방문을 하지 않은 정점이라면
                visited[d] = 1  # 방문 처리
                stack.append(d)  # 스택에 추가


DFS(1)  # 1번 컴퓨터가 바이러스에 걸림

# visited = [0, 1, 1, 1, 0, 1, 1, 0] -> 0번 인덱스는 제외하고 1번 컴퓨터와 연결된 하나의 요소
total = 0
for i in visited:
    if i == 1:
        total += 1

print(total - 1)  # 1번은 제외하고 출력

# 또는

N = int(input())
M = int(input())

graph = [[] for _ in range(N + 1)]  # 인접 리스트 생성
for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * (N + 1)  # 방문 여부 확인
stack = []

visited[1] = True  # 초기값 설정
stack.append(1)

cnt = 0
while stack:
    cur = stack.pop()  # 스택의 요소를 빼가면서 인접 요소들 방문 처리

    for adj in graph[cur]:  # 인접 요소 반복
        if visited[adj] == False:  # 만일 방문한 적이 없다면
            visited[adj] = True  # 방문 처리
            stack.append(adj)  # 스택에 추가
            cnt += 1  # 카운팅

print(cnt)


# 연결 요소의 개수 🐳
# 문제 : 연결 요소의 개수 구하기

# sys.getrecursionlimit()을 활용해 파이썬 최대 재귀 깊이 확인, 백준은 기본 1000으로 설정 🚨
sys.setrecursionlimit(10000)  # 재귀허용치를 1000 -> 10000으로 변경
input = sys.stdin.readline

N, M = map(int, input().split())

JOIN = [[] for _ in range(N + 1)]  # 인접 리스트 생성
for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0] * (N + 1)  # 방문 여부 확인


def DFS(v):
    visited[v] = 1  # 방문 처리

    for d in JOIN[v]:  # 방문한 수의 인접한 수 반복
        if not visited[d]:  # 동일한 코드, if visited[d] == 0:
            DFS(d)


cnt = 0
for i in range(1, N + 1):  # [1, 2, 3, 4, 5, 6]
    if not visited[i]:
        DFS(i)
        cnt += 1  # DFS가 끝나면 카운팅

print(cnt)

# 또는

N, M = map(int, input().split())

JOIN = [[] for _ in range(N + 1)]  # 인접 리스트 생성
for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

stack = []
visited = [False] * (N + 1)  # 방문 여부 확인
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]


def DFS(v):
    visited[v] = True  # 방문 처리
    stack.append(v)  # 스택에 추가

    while stack:  # 스택에 비어있을 때까지 반복
        cur = stack.pop()  # 스택에서 제거

        for adj in JOIN[cur]:  # 제거한 수의 인접 요소들 반복

            if not visited[adj]:  # 인접 요소가 방문 리스트에 없다면
                visited[adj] = True  # 방문 처리
                stack.append(adj)  # 스택에 추가


cnt = 0
for i in range(1, N + 1):
    if visited[i] == False:  # 방문 리스트가 비어있다면
        DFS(i)
        cnt += 1  # DFS를 종료하면서 카운팅

print(cnt)


# 촌수계산 🐳
# 문제 : 여러 사람에 대한 관계가 주어질 때, 두사람 간의 촌수 구하기

T = int(input())
N, M = map(int, input().split())
J = int(input())

JOIN = [[] for _ in range(T + 1)]  # 인접 리스트 생성
for i in range(J):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0] * (T + 1)  # 방문 여부 확인


def DFS(v):
    for i in JOIN[v]:  # 확인하고 싶은 수와 인접한 수 반복
        if visited[i] == 0:
            visited[i] = visited[v] + 1  # 인접 정점 = 확인 정점의 인덱스 값 + 1
            DFS(i)


DFS(N)  # 확인하고 싶은 수 N

if visited[M] > 0:
    print(visited[M])
else:
    print(-1)

# 또는


def BFS(v):  # 너비우선탐색
    queue = deque()
    queue.append(v)  # 큐에 추가

    while queue:
        cur = queue.popleft()  # 큐에서 제거

        for adj in JOIN[cur]:  # 인접한 수 반복하기
            if visited[adj] == 0:  # 인접한 수가 방문 리스트에 없다면
                visited[adj] = visited[cur] + 1  # 인접 정점을 확인한 정점의 인덱스 값에서 + 1
                queue.append(adj)  # 큐에 추가


N = int(input())  # 전체 인원
x, y = map(int, input().split())  # 촌수가 궁금한 두 사람
M = int(input())  # 관계의 수

visited = [0] * (N + 1)  # 방문 여부를 확인할 리스트

JOIN = [[] for _ in range(N + 1)]  # 인접 리스트 생성
for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

BFS(x)  # 촌수가 궁금한 x의 BFS 시작

print(visited[y] if visited[y] != 0 else -1)
# 방문 리스트에 있는 요소 값을 출력
# 단, 0이 아니면 출력하고, 아니면 0이라면 -1을 출력

# 또는

N = int(input())  # 전체 인원
START, END = list(map(int, input().split()))  # 촌수가 궁금한 두 사람
M = int(input())  # 관계의 수

visited = [False] * (N + 1)  # 방문 여부를 확인할 이차원 리스트 생성

visited[START] = True  # DFS를 시작하기 위한 기본값 설정
stack = []
stack.append((START, 0))  # 튜플 형태로 입력 (시작값, 촌수를 확인할 인덱스 값)


JOIN = [[] for _ in range(N + 1)]  # 인접 리스트 생성
for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

answer = -1  # 정답을 확인할 변수

while len(stack) != 0:  # 스택이 빌 때까지 반복
    number, count = stack.pop()  # 스택에서 기본값 제거
    cur = JOIN[number]  # 인접 리스트의 인접한 정점을 변수에 저장

    if number == END:  # 원하는 촌수까지 도달하면 끝
        answer = count  # 카운팅한 값을 정답에 저장
        break

    for adj in cur:  # 인접한 정점들의 순환
        if not visited[adj]:  # 인접한 정점이 방문하지 않았다면
            stack.append((adj, count + 1))  # 스택에 추가
            visited[adj] = True  # 방문 처리

print(answer)


# 섬의 개수 🚨 🐳
# 문제 : 가로, 세로 또는 대각선으로 연결된 섬의 개수 구하기

while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:  # 입력값에서 0 0 은 제외
        break

    MAPS = [list(map(int, input().split())) for _ in range(H)]  # 이차원 리스트 생성

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]  # 8방위 좌표 설정
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    cnt = 0

    def DFS(i, j):
        stack = []
        stack.append((i, j))  # 스택에 좌표 추가

        while stack:  # 스택이 빌 때까지 반복
            (y, x) = stack.pop()  # 스택에서 제거하면서 변수로 설정
            MAPS[y][x] = 0  # 탐색을 했으니 바다로 초기화

            for d in range(8):  # 8방위 좌표 탐색
                ny = y + dy[d]
                nx = x + dx[d]

                if -1 < ny < H and -1 < nx < W:  # 범위를 벗어나지 않으면서
                    if MAPS[ny][nx] == 1:  # 땅이라면
                        stack.append((ny, nx))  # 스택에 좌표 추가

        return 1  # 하나의 섬을 완료하고 1을 리턴하면서 카운팅

    for i in range(H):  # 완전탐색
        for j in range(W):
            if MAPS[i][j] == 1:  # 섬이라면 DFS 실행
                cnt += DFS(i, j)

    print(cnt)
