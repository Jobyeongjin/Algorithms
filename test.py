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
j = int(input())

s = 1
next = m
cnt = 0

for _ in range(j):
    position = int(input())

    if s <= position and next >= position:
        continue
    elif s < position:
        cnt += position - next
        s += position - next
        next = position
    else:
        cnt += s - position
        next -= s - position
        s = position

print(cnt)
