# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math
import heapq

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에

n = int(input())
m = 10001
arr = [0] * m

for i in range(n):
    arr[int(input())] += 1

for i in range(m):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
print(arr)
