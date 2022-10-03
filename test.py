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

n, m = map(int, input().split())
a = list(input().strip())[::-1]
b = list(input().strip())
t = int(input())
ant = a + b

for _ in range(t):
    for i in range(len(ant) - 1):
        if ant[i] in a and ant[i + 1] in b:
            ant[i], ant[i + 1] = ant[i + 1], ant[i]
            if ant[i + 1] == a[n - 1]:
                break

print(*ant, sep="")
