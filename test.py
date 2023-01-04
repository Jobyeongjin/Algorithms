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


n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
gems.sort()
bags = [int(input()) for _ in range(k)]
bags.sort()

answer = 0
temp = []
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(temp, -heapq.heappop(gems)[1])
    if temp:
        answer -= heapq.heappop(temp)
print(answer)