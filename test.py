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

sticks = list()
for _ in range(n):
    stick = int(input())
    sticks.append(stick)

start = sticks[-1]

cnt = 0
for i in range(len(sticks) - 1, -1, -1):
    if sticks[i] > start:
        cnt += 1
        start = sticks[i]

print(cnt + 1)
