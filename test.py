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

lecture = []
for _ in range(n):
    s, t = map(int, input().split())
    lecture.append([s, t])

lecture.sort()

heap = []
heapq.heappush(heap, lecture[0][1])
answer = 1
for i in range(1, n):
    if lecture[i][0] < heap[0]:
        heapq.heappush(heap, lecture[i][1])
        answer += 1
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lecture[i][1])

print(answer)
