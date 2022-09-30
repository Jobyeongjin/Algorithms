# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math
import heapq

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에


n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [0] * (n + 1)


def DFS(v):
    visited[v] = 1
    for i in arr[v]:
        if not visited[i]:
            DFS(i)


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        DFS(i)

print(cnt)
