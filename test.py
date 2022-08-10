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


N, M = map(int, input().split())

JOIN = [[] for _ in range(N + 1)]
for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0] * (N + 1)


def DFS(v):
    visited[v] = 1

    for d in JOIN[v]:
        if not visited[d]:
            DFS(d)


cnt = 0
for i in range(1, N + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)
