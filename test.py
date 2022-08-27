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


def hanoi(f, s, t, c):
    if c == 1:
        print(f, t)
        return

    hanoi(f, t, s, c - 1)
    print(f, t)

    hanoi(s, f, t, c - 1)


N = int(input())

print(2**N - 1)

if N <= 20:
    hanoi(1, 2, 3, N)
