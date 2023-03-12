# 파일 불러오기
from collections import deque
from collections import Counter
from itertools import permutations, combinations
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


def solution(n):
    i = 0
    fact = 1

    while fact <= n:
        i += 1
        fact *= i

    answer = i - 1

    return answer


solution(int(input()))
