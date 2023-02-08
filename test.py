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
sys.setrecursionlimit(100_000)


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에

n = int(input())
s, e = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(graph)
visited = [0] * (n + 1)


def DFS(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = visited[s] + 1
            DFS(i)


DFS(s)
print(visited[e]) if visited[e] > 0 else print(-1)
