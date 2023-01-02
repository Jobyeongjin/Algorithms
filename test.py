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
numbers = [int(input()) for _ in range(n)]
numbers.sort()

def average(arr):
    return round(sum(arr) / n)
print(average(numbers))

def center(arr):
    return arr[n // 2]
print(center(numbers))

def more(arr):
    list = Counter(arr).most_common()
    if len(arr) > 1:
        if list[0][1] == list[1][1]:
            return list[1][0]
        else:
            return list[0][0]
    else:
        return list[0][0]
print(more(numbers))

def scope(arr):
    return max(arr) - min(arr)
print(scope(numbers))