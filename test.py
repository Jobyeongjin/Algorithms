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

n, k = map(int, input().split())
numbers = input()

arr = []
for number in numbers:
    while arr and 0 < k:
        if arr[-1] < number:
            arr.pop()
            k -= 1
        else:
            break
    arr.append(number)

if k > 0:
    print("".join(arr[:-k]))
else:
    print("".join(arr))
