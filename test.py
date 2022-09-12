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


for tc in range(1, 11):
    n = int(input())
    base = list(map(int, input().split()))
    o = int(input())
    order = list(input().split())

    type = ''
    pos = -1
    cnt = -1
    for i in range(len(order)):
        if order[i] == 'I':
            type = order[i]
            pos = -1
            cnt = -1
        else:
            if type == 'I' and pos == -1:
                pos = int(order[i])
                continue
            else:
                if cnt == -1:
                    cnt = int(order[i])
                    continue

                base.insert(pos, order[i])
                pos += 1

    print(f'#{tc}', end=' ')
    print(*base[:10])
