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


for _ in range(int(input())):
    S = list(input().strip())

    total = []
    cnt = 0
    for i in S:
        if i == 'O':
            cnt += 1
            total.append(cnt)
        else:
            cnt = 0

    print(sum(total))
