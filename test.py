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

n = int(input())
working = [list(map(int, input().split())) for _ in range(n)]
working.sort(key=lambda x: x[1], reverse=True)

limit = working[0][1]
for i in range(n):
    if working[i][1] <= limit:
        limit = working[i][1] - working[i][0]
    else:
        limit -= working[i][0]

if limit < 0:
    print(-1)
else:
    print(limit)
