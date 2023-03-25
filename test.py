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


def solution(spell, dic):
    answer = 0
    for i in dic:
        cnt = len(i)
        temp = [0] * len(spell)
        for idx, s in enumerate(spell):
            if s in i:
                cnt -= 1
                temp[idx] += 1
        if cnt == 0:
            if not 0 in temp:
                answer = 1
    return answer


solution(["s", "o", "m", "d"], ["moos", "dzx", "smm", "sunmmo", "som"])
