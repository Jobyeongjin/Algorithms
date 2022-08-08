# 파일 불러오기
from collections import deque
import sys
from pprint import pprint
from collections import Counter

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 문제풀이는 여기에


def go(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= N or ny <= -1 or ny >= M:
                continue


N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

go = (0, 0)
print(grid[N - 1][M - 1])

for x in range(N):  # 0 1 2 3
    for y in range(M):  # 0 1 2 3 4 5
        # 상하좌우 이동할 좌표
        for i in range(4):  # 0 1 2 3
            nx = x + dx[i]
            ny = y + dy[i]
            # 범위를 벗어나지 않기
            if 0 <= nx < N and 0 <= ny < M:
                x = nx
                y = ny

                if grid[nx][ny] == 1:
                    grid[nx][ny] = grid[x][y] + 1
                    queue.append((nx, ny))

print()
