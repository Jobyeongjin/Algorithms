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
