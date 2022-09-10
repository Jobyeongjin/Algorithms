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


n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (n + 1)
answer = [0] * (n + 1)

for i in graph:
    i.sort()


def BFS(s):
    answer[s] = 1
    queue = deque([s])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not answer[i]:
                queue.append(i)
                answer[i] = 1


def DFS(s):
    visited[s] = 1
    print(s, end=' ')

    for i in graph[s]:
        if not visited[i]:
            DFS(i)


DFS(v)
print()
BFS(v)
