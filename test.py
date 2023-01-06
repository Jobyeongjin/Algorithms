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
numbers = sorted(list(map(int, input().split())))
x = int(input())

answer = 0
for i in range(1):
    start, end = 0, n - 1
    while start < end:
        sum_ = numbers[start] + numbers[end]
        if x < sum_:
            end -= 1
        elif x > sum_:
            start += 1
        else:
            answer += 1
            start += 1
print(answer)