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


n, w, l = map(int, input().split())
truck = deque(list(map(int, input().split())))

bg = deque([0] * w)
cnt = 0

while bg:
    cnt += 1
    bg.popleft()
    if truck:
        if sum(bg) + truck[0] <= l:
            bg.append(truck.popleft())
        else:
            bg.append(0)
    # if len(bg) == 1 and bg[0] != 0:
    #     bg.extend([0] * (w - 1))
    #     if truck:
    #         bg.append(truck.popleft())
    #     bg.popleft()
    #     cnt += 1
    # if not bg:
    #     break


print(cnt)
