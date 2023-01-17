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

lectures = []
for _ in range(n):
    pay, day = map(int, input().split())
    lectures.append([day, pay])

lectures.sort()

heap = []
for day, pay in lectures:
    heapq.heappush(heap, pay)
    if day < len(heap):
        heapq.heappop(heap)
print(sum(heap))
