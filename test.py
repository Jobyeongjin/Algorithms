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


delta = ((-1, 0), (1, 0), (0, -1), (0, 1))


def DFS(r, c, limit, length):
    global MAX_L

    if visited[r][c] == 1:
        return

    visited[r][c] = 1

    for dr, dc in delta:
        nr, nc = r + dr, c + dc

        if not (-1 < nr < N and -1 < nc < N):
            continue

        if visited[nr][nc] == 1:
            continue

        if MAP[nr][nc] < MAP[r][c]:
            DFS(nr, nc, limit, length + 1)

        elif MAP[nr][nc] >= MAP[r][c] and limit > 0:
            for i in range(1, K + 1):
                MAP[nr][nc] -= i

                if MAP[nr][nc] < MAP[r][c]:
                    DFS(nr, nc, limit - 1, length + 1)
                MAP[nr][nc] += i

    MAX_L = max(MAX_L, length)
    visited[r][c] = 0


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)] for _ in range(N)]
    HIGH = max(map(max, MAP))
    MAX_L = 0

    for i in range(N):
        for j in range(N):
            if MAP[i][j] == HIGH:
                DFS(i, j, 1, 1)

    print(f'#{tc} {MAX_L}')
