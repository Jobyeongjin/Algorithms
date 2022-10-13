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


s = input().split("-")

answer = 0
for i in s[0].split("+"):
    answer += int(i)

for i in s[1:]:
    for j in i.split("+"):
        answer -= int(j)

print(answer)
