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


def makeSnail():
    r = c = n // 2
    step = num = 2
    board[r][c] = 1
    r -= 1
    c -= 1

    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = 0

    while True:
        for _ in range(4):
            dr, dc = delta[direction]

            for _ in range(step):
                r += dr
                c += dc
                board[r][c] = num

                if num == find:
                    ans[0], ans[1] = r + 1, c + 1
                if num == n**2:
                    return

                num += 1
            direction = (direction + 1) % 4

        step += 2
        r -= 1
        c -= 1


n = int(input())
find = int(input())
board = [[0] * n for _ in range(n)]
ans = [n // 2 + 1, n // 2 + 1]

makeSnail()

for i in board:
    print(*i)
print(*ans)
