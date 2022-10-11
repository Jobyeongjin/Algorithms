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

answer = 0
while n >= 0:
    if n % 5 == 0:
        answer += n // 5
        print(answer)
        break
    n -= 3
    answer += 1

else:
    print(-1)
