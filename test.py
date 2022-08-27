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


sys.setrecursionlimit(10**9)


def DFS(r, c):
    delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

    for dr, dc in delta:
        nr = r + dr
        nc = c + dc

        if -1 < nr < N and -1 < nc < M:
            if farm[nr][nc] == 1:
                farm[nr][nc] = 0
                DFS(nr, nc)


for _ in range(int(input())):
    M, N, K = map(int, input().split())

    farm = [[0 for _ in range(M)] for _ in range(N)]

    answer = 0
    for _ in range(K):
        x, y = map(int, input().split())
        farm[y][x] = 1

    for i in range(N):
        for j in range(M):
            if farm[i][j] == 1:
                DFS(i, j)
                answer += 1

    print(answer)
