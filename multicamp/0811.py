# 영수증 🐳
# 문제 : 구매한 물건의 가격과 영수증에 적힌 금액이 일치하는지 확인하기

X = int(input())
N = int(input())

items = [list(map(int, input().split())) for _ in range(N)]  # 이차원 리스트로 입력

total = 0
for i in items:  # 리스트를 하나씩 반복
    price = i[0] * i[1]
    total += price

if X == total:
    print('Yes')
else:
    print('No')


# 와글와글 숭고한 🐳
# 문제 : 세 곳의 대학교의 참여도의 합을 구하고 필요하다면 압박하기

S, K, H = map(int, input().split())

TOTAL = S + K + H
LAST = min(S, K, H)

if TOTAL >= 100:
    print('OK')
else:
    if LAST == S:
        print('Soongsil')
    elif LAST == K:
        print('Korea')
    elif LAST == H:
        print('Hanyang')


# FBI 🐳
# 문제 : FBI명이 들어간 첩보원 찾기

SPY = [input().strip() for _ in range(5)]

FBI = False  # 초기값 0
for i in range(len(SPY)):
    if 'FBI' in SPY[i]:  # 해당 인덱스 문자열에 'FBI' 가 포함되면
        print(i + 1, end=' ')
        FBI = True

if not FBI:
    print('HE GOT AWAY!')


# 연속구간 🐳
# 문제 : 연속하여 나오는 숫자를 찾아 가장 긴 것의 길이 구하기

N = 3
for i in range(N):
    numbers = input()

    answer = 1
    cnt = 1
    for i in range(len(numbers) - 1):  # 숫자의 길이만큼 반복
        if numbers[i] == numbers[i + 1]:  # 문자열의 인덱스로 접근
            cnt += 1
            if cnt > answer:  # 정답보다 카운터가 더 크다면 카운터로 교체
                answer = cnt
        else:
            cnt = 1

    if answer == 0:
        print(1)
    else:
        print(answer)


# 애너그램 🐳
# 문제 : A에 속하는 알파벳의 순서를 바꿔 B를 만들 수 있다면 애너그램, 애너그램인지 아닌지를 구하기

N = int(input())

for _ in range(N):
    A, B = input().split()

    a = sorted(list(A))
    b = sorted(list(B))

    if a == b:
        print(f'{A} & {B} are anagrams.')
    else:
        print(f'{A} & {B} are NOT anagrams.')


# 트럭 주차 🚨 🐳
# 문제 : 상근이 트럭의 총 주차 요금 구하기


# 킹 🚨 🐳
# 문제 : 킹과 돌의 이동한 위치 구하기


# 섬의 개수 🐳
# 문제 : 가로, 세로 또는 대각선으로 연결된 섬의 개수 구하기

while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:  # 입력값에서 0 0은 제외
        break

    MAPS = [list(map(int, input().split())) for _ in range(H)]  # 이차원 리스트 생성

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]  # 8방위 좌표 설정
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    def DFS(i, j):
        stack = []
        stack.append((i, j))  # 스택에 좌표 추가

        while stack:  # 스택이 빌 때까지 반복
            (y, x) = stack.pop()  # 스택에서 제거하면서 변수로 담기
            MAPS[y][x] = 0  # 탐색한 좌표는 바다로 초기화

            for d in range(8):  # 8방위 좌표 탐색
                ny = y + dy[d]
                nx = x + dx[d]

                if -1 < ny < H and -1 < nx < W:  # 범위가 벗어나지 않으면서
                    if MAPS[ny][nx] == 1:  # 땅이라면
                        stack.append((ny, nx))  # 스택에 좌표 추가

        return 1  # 하나의 섬을 완료하면 1을 리턴하면서 카운팅

    cnt = 0
    for i in range(H):  # 완전탐색
        for j in range(W):
            if MAPS[i][j] == 1:  # 섬이라면 DFS 실행
                cnt += DFS(i, j)

    print(cnt)

# 또는

while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:  # 입력값에서 0은 제외
        break

    MAPS = [list(map(int, input().split())) for _ in range(H)]  # 인접 리스트 생성

    dy = [-1, -1, -1, 0, 0, 1, 1, 1]  # 8방위 델타 좌표
    dx = [-1, 0, 1, -1, 1, -1, 0, 1]

    cnt = 0
    for i in range(H):  # 이중 반복문으로 완전 탐색
        for j in range(W):
            if MAPS[i][j] == 1:  # 좌표에서 1을 만나면
                stack = []
                stack.append((i, j))  # 스택에 좌표 추가

                while stack:  # 스택에 빌 때까지 반복
                    (y, x) = stack.pop()  # 스택에서 좌표 제거 후 변수에 저장
                    if MAPS[y][x] == 1:
                        MAPS[y][x] = 0  # 좌표 초기화

                        for k in range(8):  # 델타 탐색
                            ny = y + dy[k]  # 다음 좌표는 기존 좌표 + 델타 좌표
                            nx = x + dx[k]

                            if -1 < ny < H and -1 < nx < W:  # 구역을 벗어나지 않게 설정
                                if MAPS[ny][nx] == 1:  # 다음 좌표가 1이라면
                                    stack.append((ny, nx))  # 스택에 좌표 추가
                # 반복문이 끝나면 카운팅 / 섬의 개수
                cnt += 1

    print(cnt)


# 로봇 🚨 🐳

M, CC = map(int, input().split())  # 11 14
area = [['.' for _ in range(M)] for _ in range(M)]

RR, RC = M - 1, 0
area[RR][RC] = 'R'
vector = [0, 1]

for _ in range(CC):
    command, number = input().strip('\n').split()
    number = int(number)

    if command == 'MOVE':
        nr = RR + (vector[0] * number)
        nc = RC + (vector[1] * number)

        if not (0 <= nr < M and 0 <= nc < M):
            print(-1)
            break

        area[RR][RC], area[nr][nc] = area[nr][nc], area[RR][RC]
        RR, RC = nr, nc

    elif command == 'TURN':
        if number == 0:
            vector[0], vector[1] = (
                0 * vector[0]) + (-1 * vector[1]), (1 * vector[0]) + (0 * vector[1])
        elif number == 1:
            vector[0], vector[1] = (
                0 * vector[0]) + (1 * vector[1]), (-1 * vector[0]) + (0 * vector[1])
        else:
            print(-1)
            break

    else:
        print(-1)
        break

else:
    RX = RC
    RY = (M - 1) - RR
    print(RX, RY)

# 또는

M, N = map(int, input().split())

y, x = 0, 0
dir_ = 0
dir_m = [(0, 1), (-1, 0), (0, -1), (1, 0)]  # 델타 좌표

result = True
for i in range(N):
    order, num = input().split()
    num = int(num)

    if order == 'MOVE':  # 로봇이 움직이라는 명령을 받으면
        ny = y + dir_m[dir_][0] * num  # 방향을 보고 각 좌표에 거리만큼 곱하기
        nx = x + dir_m[dir_][1] * num

        if -1 < ny < M and -1 < nx < M:  # 경계를 넘어가지 않으면
            y = ny  # 좌표 수정
            x = nx
        else:  # 경계를 넘어가면 명령은 유효하지 않음
            result = False

    elif order == 'TURN':  # 로봇이 방향을 바꾸라는 명령을 받으면
        if num == 0:  # 0이면 왼쪽으로 90도 회전
            dir_ -= 1
            if dir_ < 0:  # 0보다 작아질 경우 3으로 변경 / 방향 0 ~ 3
                dir_ = 3
        elif num == 1:  # 1이면 오른쪽으로 90도 회전
            dir_ += 1
            if dir_ == 4:  # 방향이 3보다 커지면 0으로 변경
                dir_ = 0

if result:
    print(x, y)  # 좌표를 선언할 때 반대로 지정했기 때문에 다시 되돌려서 출력
else:
    print(-1)  # 유효하지 않은 명령이라면 -1


# 그림 🚨 🐳

N, M = map(int, input().split())
PAINT = [list(map(int, input().split())) for _ in range(N)]  # 인접 리스트 생성

visited = [[0 for _ in range(M)] for _ in range(N)]  # 방문 리스트 생성
DELTA = ((0, 1), (1, 0), (-1, 0), (0, -1))  # 델타 좌표


def DFS(r, c):
    area = 0  # 그림 안에 1을 카운팅
    stack = list()
    stack.append((r, c))  # 스택에 좌표 추가

    while stack:
        pr, pc = stack.pop()  # 스택에서 좌표 제거 후 변수에 저장

        if visited[pr][pc] == 0 and PAINT[pr][pc] == 1:  # 방문 좌표가 0이면서 그림 좌표가 1이라면
            visited[pr][pc] = 1  # 방문 처리 후 카운팅
            area += 1

        for dr, dc in DELTA:  # 델타 탐색
            nr = pr + dr  # 다음 좌표 = 기존 좌표 + 델타 좌표
            nc = pc + dc

            if 0 <= nr < N and 0 <= nc < M:  # 구역을 벗어나지 않게 설정
                if visited[nr][nc] == 0 and PAINT[nr][nc] == 1:  # 방문 좌표가 0이면서 그림 좌표가 1이라면
                    stack.append((nr, nc))  # 스택에 좌표 추가

    return area


result = []
for i in range(N):  # 이중 반복문으로 완전 탐색
    for j in range(M):
        if visited[i][j] == 0 and PAINT[i][j] == 1:  # 방문 좌표가 0이고 그림의 좌표가 1이라면
            result.append(DFS(i, j))  # DFS 실행

print(len(result))  # 총 그림의 수
# 가장 큰 그림의 1의 개수, 만일 총 그림의 개수가 0인 경우 가장 넓은 그림의 넓이는 0
print(max(result)) if len(result) != 0 else print(0)


# 또는

N, M = map(int, input().split())

PAPER = [list(map(int, input().split())) for _ in range(N)]  # 인접리스트 생성

dy = [-1, 0, 0, 1]  # 4방향 델타 좌표 생성
dx = [0, -1, 1, 0]

area = 0  # 총 그림의 개수
one_list = []  # 1의 개수를 담을 리스트
for i in range(N):  # 이중 반복문으로 완전탐색
    for j in range(M):
        if PAPER[i][j] == 1:  # 탐색 중 1을 만나면
            stack = []
            stack.append((i, j))  # 스택에 좌표 추가

            cnt = 0
            while stack:  # 스택이 빌 때까지
                (y, x) = stack.pop()  # 스택에서 좌표 제거 후 변수에 저장

                if PAPER[y][x] == 1:  # 좌표가 1이라면
                    cnt += 1  # 방문 처리 후 초기화
                    PAPER[y][x] = 0

                    for k in range(4):  # 델타 탐색
                        ny = y + dy[k]  # 다음 좌표 = 기존 좌표 + 델타 좌표
                        nx = x + dx[k]

                        if -1 < ny < N and -1 < nx < M:  # 구역을 벗어나지 않게 설정
                            if PAPER[ny][nx] == 1:  # 다음 좌표가 1이라면
                                stack.append((ny, nx))  # 스택에 좌표 추가
            # 반복문이 끝나고
            area += 1  # 그림의 수 카운팅
            one_list.append(cnt)  # 1의 개수 추가

print(area)  # 그림의 수
print(max(one_list))  # 그림의 넓이가 큰 그림의 1의 개수


# 또는

n, m = list(map(int, input().split()))

graph = []
for _ in range(n):  # 인접 리스트 생성
    graph.append(list(map(int, input().split())))

visited = []
for _ in range(n):  # 방문 처리할 이차원 리스트 생성
    visited_list = [False] * m
    visited.append(visited_list)

dy = [-1, 0, 0, 1]  # 4방향 델타 좌표 생성
dx = [0, -1, 1, 0]

paint_cnt = 0
paint_size = []
for y in range(n):  # 이중 반복문으로 완전 탐색
    for x in range(m):
        if not visited[y][x] and graph[y][x] == 1:  # 방문 좌표가 0이면서 그림 좌표가 1이라면
            ''''
            DFS
            '''
            stack = []
            stack.append([y, x])  # 스택에 좌표 추가
            visited[y][x] = True  # 방문 처리

            paint_cnt += 1
            size = 0
            while len(stack) != 0:
                py, px = stack.pop()  # 스택에서 제거 후 변수에 저장
                size += 1  # 그림 안에 1의 개수

                for d in range(4):  # 델타 탐색
                    ny = py + dy[d]  # 다음 좌표 = 기존 좌표 + 델타 좌표
                    nx = px + dx[d]

                    if not (-1 < ny < n and -1 < nx < m):  # 범위가 벗어나지 않으면서
                        continue

                    if visited[ny][nx] == True:  # 벙문 처리를 했다면
                        continue

                    if graph[ny][nx] != 1:  # 그림 좌표가 1이 아니라면
                        continue

                    stack.append((ny, nx))  # 스택에 다음 좌표 추가
                    visited[ny][nx] = True  # 다음 좌표를 방문 처리

            paint_size.append(size)

if len(paint_size) != 0:
    print(paint_cnt)
    print(max(paint_size))
else:
    print(0)
