# 파일 불러오기
from collections import deque
from collections import Counter
from curses import KEY_LEFT
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

rope = list(int(input()) for _ in range(n))
rope.sort(reverse=True)

answer = list(rope[i] * (i + 1) for i in range(n))
print(max(answer))
