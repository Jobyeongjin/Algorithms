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


i = 1
while True:
    l, p, v = map(int, input().split())
    if l + p + v == 0:
        break

    answer = (v // p) * l
    answer += min((v % p), l)

    print(f"Case {i}: {answer}")
    i += 1
