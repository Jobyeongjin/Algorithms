# 파일 불러오기
from collections import deque
from collections import Counter
from curses import KEY_LEFT
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


n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)][::-1]

cnt = 0
for i in coin:
    if k == 0:
        break
    if i > k:
        continue
    cnt += k // i
    k %= i

print(cnt)
