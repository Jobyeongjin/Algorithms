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

bg.popleft()
while truck:
    if sum(bg) + truck[0] < l:
        bg.append(truck.popleft())
        cnt += 1
    else:
        bg.popleft()
        cnt += 1
print(cnt)
