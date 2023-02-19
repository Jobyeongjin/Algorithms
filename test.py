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


def binarySearch(nums, target):
    cnt, temp = 0, 200000000
    for i in range(n):
        print(i)
        left, right = i + 1, n - 1

        while left <= right:
            mid = (left + right) // 2
            sumNums = nums[i] + nums[mid]
            print(nums)
            print(left, right)
            print(mid, sumNums, target)

            if sumNums < target:
                left = mid + 1
            else:
                right = mid - 1

            if abs(target - sumNums) < temp:
                cnt = 1
                temp = abs(target - sumNums)
            elif abs(target - sumNums) == temp:
                cnt += 1

    return cnt


for _ in range(int(input())):
    n, k = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    print(binarySearch(numbers, k))
