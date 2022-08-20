# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


S = [list(map(int, input().split())) for _ in range(int(input()))]

for i in S:
    RANK = 1
    for j in S:
        if i[0] < j[0] and i[1] < j[1]:
            RANK += 1

    print(RANK, end=' ')
