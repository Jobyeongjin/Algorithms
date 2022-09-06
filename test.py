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


n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))


def dfs(r, c):
    stack = []
    stack.append((r, c))

    area = 0
    while stack:
        pr, pc = stack.pop()

        if visited[pr][pc] == 0 and graph[pr][pc] == 1:
            visited[pr][pc] = 1
            area += 1

        for dr, dc in delta:
            nr = dr + pr
            nc = dc + pc

            if -1 < nr < n and -1 < nc < n:
                if visited[nr][nc] == 0 and graph[nr][nc] == 1:
                    stack.append((nr, nc))

    return area


answer = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            answer.append(dfs(i, j))
answer.sort()

print(len(answer))
for i in answer:
    print(i)
