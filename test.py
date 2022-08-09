# 파일 불러오기
from collections import deque
from collections import Counter
import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


N = 19
board = [list(map(int, input().split())) for _ in range(N)]

dx = [0, 1, -1, 1]
dy = [1, 0, 1, 1]
answer = 0
for y in range(N):
    for x in range(N):
        if board[y][x] == 1 or board[y][x] == 2:
            for d in range(4):
                cnt = 1

                ny = y + dy[d]
                nx = x + dx[d]

                while True:
                    if not(-1 < ny < N and -1 < nx < N):
                        break

                    if board[ny][nx] != board[y][x]:
                        break

                    cnt += 1

                    ny = y + dy[d]
                    nx = x + dx[d]

                if cnt == 5:
                    prev_y = y - dy[d]
                    prev_x = x - dx[d]

                    if not (-1 < prev_y < N and -1 < prev_x < N) or board[y][x] != board[prev_y][prev_x]:
                        print(board[y][x])

                        print(y + 1, x + 1)
                        answer = board[y][x]

if answer == 0:
    print(answer)
