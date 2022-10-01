# 파일 불러오기
from collections import deque
from collections import Counter
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
cards = list(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

for i in check:
    if i in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")
