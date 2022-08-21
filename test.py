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


WORD = input().strip()
C = input().strip()

N = len(C)
i = 0
cnt = 0
while i < len(WORD):
    if WORD[i: i + N] == C:
        cnt += 1
        i += N
    else:
        i += 1

print(cnt)
