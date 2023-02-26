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
k = int(input())

start, end = 1, k
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, n + 1):
        temp += min(mid // i, n)

    if temp >= k:
        end = mid - 1
    else:
        start = mid + 1

print(start)
