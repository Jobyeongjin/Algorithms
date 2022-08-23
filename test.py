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


T = int(input())
N, M = map(int, input().split())
K = int(input())

JOIN = [[] for _ in range(T + 1)]

for _ in range(K):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0] * (T + 1)


def DFS(v):
    for i in JOIN[v]:
        if not visited[i]:
            visited[i] = visited[v] + 1
            DFS(i)


DFS(N)

if visited[M] > 0:
    print(visited[M])
else:
    print(-1)
