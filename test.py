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
leftNums = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    num = leftNums[i]
    id = i + 1
    left = 0
    for j in range(n):
        if left == num and answer[j] == 0:
            answer[j] = id
            break
        elif answer[j] == 0:
            left += 1
print(*answer)
