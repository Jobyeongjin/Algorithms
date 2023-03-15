# 파일 불러오기
from collections import deque
from collections import Counter
from itertools import permutations, combinations
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
rooms = []
for _ in range(n):
    idx, st, et = map(int, input().split())
    heapq.heappush(rooms, [st, et, idx])

target = []
fs, fe, fi = heapq.heappop(rooms)
heapq.heappush(target, fe)

while rooms:
    st, et, i = heapq.heappop(rooms)
    if target[0] <= st:
        heapq.heappop(target)
    heapq.heappush(target, et)

print(len(target))
