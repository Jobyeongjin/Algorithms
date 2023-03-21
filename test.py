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


def solution(numbers):
    answer = 0
    for i in range(len(numbers)):
        for j in range(i + 1, len(numbers)):
            answer = max(answer, numbers[i] * numbers[j])
    return answer


solution([1, 2, -3, 4, -5])
