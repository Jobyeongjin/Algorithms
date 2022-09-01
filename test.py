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


m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

queue = deque([])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])

print(tomato)


def BFS():
    while queue:
        r, c = queue.popleft()

        for dr, dc in delta:
            nr, nc = r + dr, c + dc

            if -1 < nr < n and -1 < nc < m:
                if tomato[nr][nc] == 0:
                    tomato[nr][nc] = tomato[r][c] + 1
                    queue.append([nr, nc])


BFS()
pprint(tomato)
answer = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer - 1)
