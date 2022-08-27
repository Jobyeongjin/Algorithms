# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


dr = [-1, 0, 0, 1]
dc = [0, -1, 1, 0]

for _ in range(int(input())):
    M, N, K = map(int, input().split())

    land = [[0] * M for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    for _ in range(K):
        x, y = map(int, input().split())
        land[y][x] = 1

    cnt = 0
    for i in range(N):
        for j in range(M):
            if land[i][j] == 1 and visited[i][j] == 0:
                cnt += 1
                stack = [(i, j)]
                visited[i][j] = 1

                while stack:
                    cur = stack.pop()

                    for k in range(4):
                        nr = cur[0] + dr[k]
                        nc = cur[1] + dc[k]

                        if -1 < nr < N and -1 < nc < M:
                            if land[nr][nc] == 1 and visited[nr][nc] == 0:
                                visited[nr][nc] = 1
                                stack.append((nr, nc))

    print(cnt)
