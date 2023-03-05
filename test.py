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


n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

house, chickens = [], []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append((i + 1, j + 1))
        elif maps[i][j] == 2:
            chickens.append((i + 1, j + 1))

answer = 10e9

for chicken in combinations(chickens, m):
    totalRoad = 0
    for hr, hc in house:
        road = 10e9
        for cr, cc in chicken:
            road = min(road, (abs(hr - cr) + abs(hc - cc)))
        totalRoad += road
    answer = min(answer, totalRoad)

print(answer)
