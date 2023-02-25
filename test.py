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


def blurayCount(bluraySize):
    cnt = 0
    sumLesson = 0

    for i in range(n):
        if sumLesson + lessons[i] > bluraySize:
            cnt += 1
            sumLesson = 0
        sumLesson += lessons[i]

    return cnt + 1


def binarySearch(lessons, target):
    left, right = max(lessons), sum(lessons)

    while left <= right:
        mid = (left + right) // 2
        cnt = blurayCount(mid)

        if cnt > target:
            left = mid + 1
        elif cnt <= target:
            right = mid - 1

    return left


n, m = map(int, input().split())
lessons = list(map(int, input().split()))
print(binarySearch(lessons, m))
