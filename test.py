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


n, l = map(int, input().split())
position = list(map(int, input().split()))
position.sort()

end = position[-1]
num = 0
answer = 0
while end >= num:
    if position:
        if num == position[0]:
            del position[0]
            answer += 1
            if ((num - 1) + l) in position:
                idx = position.index((num - 1) + l)
                del position[: idx + 1]
                num = (num - 1) + l
                continue
    else:
        break
    num += 1

print(answer)
# if answer % l == 0:
#     print(answer // l)
# else:
#     print((answer // l) + 1)
