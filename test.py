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


N = int(input())
M = int(input())

JOIN = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0 for _ in range(N + 1)]


def DFS(v):
    stack = [v]
    visited[v] = 1

    while stack:
        cur = stack.pop()

        for d in JOIN[cur]:
            if not visited[d]:
                visited[d] = 1
                stack.append(d)


DFS(1)

answer = -1
for i in visited:
    if i == 1:
        answer += 1

print(answer)
