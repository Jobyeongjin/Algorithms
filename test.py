# 파일 불러오기
from collections import deque
from collections import Counter
from itertools import permutations
import sys
import math
import heapq
import operator

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 재귀함수의 한계를 10만까지 늘림
sys.setrecursionlimit(10**6)


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에

n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n):
    arr = list(map(int, input().split()))
    nodeNum = arr[0]
    idx = 1
    while arr[idx] != -1:
        v, w = arr[idx], arr[idx + 1]
        graph[nodeNum].append((v, w))
        idx += 2

visited = [-1] * (n + 1)
visited[1] = 0


def DFS(s, wei):
    for v, w in graph[s]:
        if visited[v] == -1:
            visited[v] = w + wei
            DFS(v, w + wei)


DFS(1, 0)

maxNode = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[maxNode] = 0

DFS(maxNode, 0)

print(max(visited))
