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
floor = [list(input().strip()) for _ in range(n)]

answer = 0
cnt = 0
for r in range(n):
    for c in range(m):
        if floor[r][c] == "-":
            cnt += 1
        elif floor[r][c] != "-" and cnt > 0:
            answer += 1
            cnt = 0
    if cnt > 0:
        answer += 1
        cnt = 0

for c in range(m):
    for r in range(n):
        if floor[r][c] == "|":
            cnt += 1
        elif floor[r][c] != "|" and cnt > 0:
            answer += 1
            cnt = 0
    if cnt > 0:
        answer += 1
        cnt = 0

print(answer)
