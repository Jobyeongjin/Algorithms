# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math
import heapq

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


n, m = map(int, input().split())

a = [[0] * (n + 1)]
b = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    a_row = [0] + [int(i) for i in input().split()]
    a.append(a_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        b[i][j] = b[i][j-1] + b[i-1][j] - b[i-1][j-1] + a[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = b[x2][y2] - b[x1 - 1][y2] - b[x2][y1 - 1] + b[x1 - 1][y1 - 1]
    print(answer)
