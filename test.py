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
reports = []
answer = [0] * 1001

for _ in range(n):
    day, value = map(int, input().split())
    reports.append([-value, day, value])

heapq.heapify(reports)

while reports:
    temp = heapq.heappop(reports)
    for i in range(temp[1], 0, -1):
        if answer[i] == 0:
            answer[i] = temp[2]
            break

print(sum(answer))
