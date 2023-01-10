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

name = input().strip()
n = int(input())
teams = [input().strip() for _ in range(n)]

answer = []
for team in teams:
    sum_ = name + team
    L = sum_.count('L')
    O = sum_.count('O')
    V = sum_.count('V')
    E = sum_.count('E')
    result = ((L+O) * (L+V) * (L+E) * (O+V) * (O+E) * (V+E)) % 100
    answer.append((team, result))

answer.sort(key=lambda x: (-x[1], x[0]))

print(answer[0][0])