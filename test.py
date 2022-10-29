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


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에


n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

delta = ((0, -1), (1, 0), (0, 1), (-1, 0))


def BFS(i, j):
    q = deque()
    q.append((i, j))

    while q:
        r, c = q.popleft()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            print(nr, nc)
            if -1 < nr < n and -1 < nc < m and arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))

    return arr[n - 1][m - 1]


print(BFS(0, 0))
