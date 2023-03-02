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


n, m = map(int, input().split())
todays = [int(input()) for _ in range(n)]

left, right = min(todays), sum(todays)
ans = 0

while left <= right:
    mid = (left + right) // 2

    total = mid
    cnt = 1

    for today in todays:
        if total < today:
            total = mid
            cnt += 1
        total -= today

    if cnt > m or mid < max(todays):
        left = mid + 1
    else:
        right = mid - 1
        ans = mid

print(ans)
