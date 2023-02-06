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
sys.setrecursionlimit(100_000)


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에

l, r = input().split()
L, R = len(l), len(r)

if L != R:
    print(0)
else:
    answer = 0
    for i in range(L):
        if l[i] != r[i]:
            break
        else:
            if l[i] == "8":
                answer += 1

    print(answer)
