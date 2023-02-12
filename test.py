# 파일 불러오기
from collections import deque
from collections import Counter
from itertools import permutations
import sys
import math
import heapq
import operator

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 재귀함수의 한계를 10만까지 늘림
sys.setrecursionlimit(100_000)


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에

M, N, H = map(int, input().split())
tomatoBox = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

delta = ((0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (-1, 0, 0), (1, 0, 0))


def BFS():
    while queue:
        h, r, c = queue.popleft()
        for dh, dr, dc in delta:
            nh = dh + h
            nr = dr + r
            nc = dc + c

            if (
                -1 < nh < H
                and -1 < nr < N
                and -1 < nc < M
                and not tomatoBox[nh][nr][nc]
            ):
                tomatoBox[nh][nr][nc] = tomatoBox[h][r][c] + 1
                queue.append((nh, nr, nc))


queue = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomatoBox[h][i][j] == 1:
                queue.append((h, i, j))


BFS()

answer = 0
for boxFloors in tomatoBox:
    for days in boxFloors:
        for day in days:
            if day == 0:
                print(-1)
                exit()
            answer = max(answer, day)

print(answer - 1)
