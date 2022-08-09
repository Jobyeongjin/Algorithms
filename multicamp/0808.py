from collections import deque
import sys

input = sys.stdin.readline

# R2 🐳
# 문제 : R1 + R2, 두 수의 평균 S, S와 R1이 주어질 때 R2 구하기

R1, S = map(int, input().split())
answer = S * 2 - R1

print(answer)


# 얼마? 🐳
# 문제 : 자동차를 구매하는데 필요한 금액 구하기

T = int(input())

for _ in range(T):
    S = int(input())  # 자동차 가격
    n = int(input())  # 옵션 수

    option = 0
    for i in range(n):
        a, b = map(int, input().split())  # a: 옵션 개수, b: 옵션 가격
        option += a * b

    print(S + option)


# 피시방 알바 🐳
# 문제 : 자리가 비어있지 않다면 거절 당한다. 거절당하는 사람의 수 구하기

T = int(input())
sit = set(map(int, input().split()))  # 거절당하는 사람이 중복값

if sit == T:
    print(0)
else:
    print(T - len(sit))


# 0의 개수 🐳
# 문제 : N부터 M까지의 수들의 '0' 이 몇 개인지 구하기

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    cnt = 0
    for j in range(N, M + 1):  # N부터 M까지 탐색
        word = str(j)  # 숫자로는 비교할 수 없음, 0 != 10
        cnt += word.count('0')  # 0의 개수만큼 카운팅

    print(cnt)


# 성적 통계 🐳
# 문제 : 학생들의 수학 성적의 최대 점수, 최소 점수, 점수 차이 구하기

K = int(input())

for i in range(1, K + 1):
    score = list(map(int, input().split()))
    score.pop(0)  # 첫번째 요소는 쓸 일이 없음

    max_ = max(score)  # 최대값
    min_ = min(score)  # 최소값

    sort_ = sorted(score)  # 정렬한 리스트에서 점수 차이를 구하기
    gap_list = []
    for j in range(len(sort_) - 1):
        gap = sort_[j + 1] - sort_[j]  # 점수 차 = 다음 인덱스 - 현재 인덱스
        gap_list.append(gap)

    print(f'Class {i}')
    print(f'Max {max_}, Min {min_}, Largest gap {max(gap_list)}')


# 블랙잭 🐳
# 문제 : 합이 M을 넘지 않으면서 최대한 가까운 카드 3장 구하기

N, M = map(int, input().split())

cards = list(map(int, input().split()))  # [5, 6, 7, 8, 9]

answer = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = cards[i] + cards[j] + cards[k]  # 해당 인덱스의 값 더하기

            if answer < total <= M:  # M은 넘지 않은 수로 값을 리셋
                answer = total
            if total == M:
                answer = total

print(answer)


# 일곱 난쟁이 🐳
# 문제 : 아홉 명의 난쟁이 중 백설 공주의 난쟁이 7명 구하기, 7명의 키의 합은 100

N = 9
dwarf = [int(input()) for _ in range(N)]

total = sum(dwarf)  # 140
a, b = 0, 0
for i in range(N - 1):  # 가짜 난쟁이 2명 찾기
    for j in range(i + 1, N):
        if total - (dwarf[i] + dwarf[j]) == 100:
            a, b = dwarf[i], dwarf[j]

dwarf.remove(a)
dwarf.remove(b)
dwarf.sort()

print(*dwarf, sep='\n')


# 영화감독 숌 🐳
# 문제 : '666'이 들어간 N번째 영화 제목 구하기

N = int(input())

title = 666
cnt = 0
while True:
    if '666' in str(title):  # title에서 666이 나오면 카운트 1씩 증가
        cnt += 1

    if cnt == N:  # 입력값과 같으면 출력하고 멈춤
        print(title)
        break

    title += 1  # 1씩 증가하면서 완전 탐색


# 문서 검색 🐳
# 문제 : 문서에서 단어가 중복없이 총 몇 번 등장하는지 구하기

paper = input().strip()
word = input().strip()

answer = paper.count(word)

print(answer)

# 또는
paper = input().strip()
word = input().strip()

answer = paper.split(word)  # 구분자를 순차적으로 나눔

print(len(answer) - 1)


# 오목 🐳 🚨
# 문제 : 오목, 검은색이 이기면 1, 흰색일 경우 2, 승부가 안났으면 0
#      가장 왼쪽에 있는 바둑알의 가로줄 번호, 세로줄 번호 출력

# 우 하 우상 우하
dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]
BLACK = 1
WHITE = 2
N = 19

# 오목판 입력
board = []
for _ in range(N):
    row = list(map(int, input().split()))
    board.append(row)
# 무승부가 발생했을 때 출력하기 위한 값
answer = 0
# 이중 반복문
for y in range(N):
    for x in range(N):
        # 검은색돌이나 흰색돌일때만 델타 탐색을 수행
        if board[y][x] == 1 or board[y][x] == 2:
            # 델타 탐색
            for d in range(4):
                # 방향이 바뀔 때마다 동일한 색의 돌의 개수 초기화
                cnt = 1
                # 다음 좌표 탐색
                ny = y + dy[d]
                nx = x + dx[d]

                while True:
                    # 인덱스 조건, 범위를 벗어나면 탈출
                    if not(-1 < ny < N and -1 < nx < N):
                        break
                    # 같은색 돌인지 확인, 다른 색 돌이면 탈출
                    if board[ny][nx] != board[y][x]:
                        break
                    # 같은 값이고 범위를 벗어나지 않으면 같은 색 돌의 수 + 1
                    cnt += 1
                    # 같은 방향으로 다음 좌표를 탐색
                    ny = y + dy[d]
                    nx = x + dx[d]

                if cnt == 5:
                    # 이전 좌표
                    # 기준 좌표(y, x)에서 델타 값을 마이너스
                    prev_y = y - dy[d]
                    prev_x = x - dx[d]
                    # 육목인지 판단
                    # 조건 1. 이전좌표가 범위를 벗어나면 오목
                    # if not -1 < prev_y < N and -1 < prev_x < N:
                    # 조건 2. 기준 좌표의 값과 이전 좌표의 값이 다르면 오목
                    # if board[y][x] != board[prev_y][prev_x]:

                    # 조건 1과 조건 2를 만족하면 오목이 완성
                    if not (-1 < prev_y < N and -1 < prev_x < N) or board[y][x] != board[prev_y][prev_x]:
                        # 현재 돌 색 출력
                        print(board[y][x])
                        # 현재 돌의 좌표를 출력
                        print(y + 1, x + 1)
                        # 승패가 결정났기 때문에 answer 값 출력 X
                        answer = board[y][x]

if answer == 0:
    print(answer)


# 미로 탐색 🐳 🚨
# 문제 : 지나야 하는 최소의 칸 수 구하기

def bfs(x, y):
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= N or ny < 0 or ny >= M:
                continue

            if grid[nx][ny] == 0:
                continue

            if grid[nx][ny] == 1:
                grid[nx][ny] = grid[x][y] + 1
                q.append((nx, ny))

    return grid[N - 1][M - 1]


N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

print(bfs(0, 0))
