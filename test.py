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


def DFS(c, r):
    for dr, dc in delta:
        nr = dr + r
        nc = dc + c

        if -1 < nc < h and -1 < nr < w and maps[nc][nr] == 1:
            maps[nc][nr] = 0
            DFS(nc, nr)


while True:
    w, h = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(h)]

    delta = ((0, -1), (1, -1), (1, 0), (1, 1),
             (0, 1), (-1, 1), (-1, 0), (-1, -1))

    if w == 0 and h == 0:
        break

    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                maps[i][j] = 0
                DFS(i, j)
                cnt += 1

    print(cnt)
