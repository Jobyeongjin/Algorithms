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


N, M = map(int, input().split())
PAINT = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
delta = ((0, 1), (1, 0), (-1, 0), (0, -1))

pprint(PAINT)
pprint(visited)


def DFS(r, c):
    area = 0
    stack = []
    stack.append((r, c))

    while stack:
        pr, pc = stack.pop()

        if visited[pr][pc] == 0 and PAINT[pr][pc] == 1:
            visited[pr][pc] = 1
            area += 1

        for dr, dc in delta:
            nr = pr + dr
            nc = pc + dc

            if -1 < nr < N and -1 < nc < M:
                if visited[nr][nc] == 0 and PAINT[nr][nc] == 1:
                    stack.append((nr, nc))

    return area


result = []
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and PAINT[i][j] == 1:
            result.append(DFS(i, j))

print(len(result))
print(max(result)) if len(result) != 0 else print(0)
