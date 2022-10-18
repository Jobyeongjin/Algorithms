# 파일 불러오기
from collections import deque
from collections import Counter
from curses import KEY_LEFT
from itertools import permutations
import sys
import math
import heapq
import operator

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에

n, m, v = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

visited = [0] * (n + 1)

for i in arr:
    i.sort()


def DFS(v):
    visited[v] = 1
    print(v, end=" ")

    for i in arr[v]:
        if visited[i] != 1:
            DFS(i)


def BFS(v):
    visited[v] = 1
    q = deque([v])

    while q:
        qp = q.popleft()
        print(qp, end=" ")

        for i in arr[qp]:
            if visited[i] != 1:
                q.append(i)
                visited[i] = 1


DFS(v)
visited = [0] * (n + 1)
print()
BFS(v)
