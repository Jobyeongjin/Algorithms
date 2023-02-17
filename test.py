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
solution = list(map(int, input().split()))

left, right = 0, n - 1
temp = 2000000000
a, b = 0, 0

while left < right:
    check = solution[left] + solution[right]

    if abs(check) < temp:
        a, b = solution[left], solution[right]
        temp = abs(check)

    if check < 0:
        left += 1
    else:
        right -= 1

print(a, b)

# temp = abs(solution[0] + solution[n - 1])
# a, b = solution[0], solution[n - 1]

# for i in range(n):
#     for j in range(i + 1, n):
#         if abs(solution[i] + solution[j]) <= temp:
#             temp = abs(solution[i] + solution[j])
#             a, b = solution[i], solution[j]
# print(a, b)
