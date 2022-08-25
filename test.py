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
delta = ((-1, 0), (0, -1), (1, 0), (0, 1))


def DFS(r, c, h):

    for dr, dc in delta:
        nr = r + dr
        nc = c + dc

        if -1 < nr < N and -1 < nc < N:
            if visited[nr][nc] == 0 and area[nr][nc] > h:
                visited[nr][nc] = 1
                DFS(nr, nc, h)


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

answer = 1
for k in range(max(map(max, area))):
    visited = [[0 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] > k:
                cnt += 1
                visited[i][j] = 1
                DFS(i, j, k)
    answer = max(answer, cnt)

print(answer)
