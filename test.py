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


plates = list(input())

answer = 10
for i in range(1, len(plates)):
    if plates[i] == plates[i - 1]:
        answer += 5
    else:
        answer += 10

print(answer)
