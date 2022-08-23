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


for tc in range(1, int(input()) + 1):
    N = int(input())
    DECK = input().split()
    cut = N - N // 2

    one = deque(DECK[:cut])
    two = deque(DECK[cut:])

    answer = []
    while one or two:
        if one:
            answer.append(one.popleft())
        if two:
            answer.append(two.popleft())

    print(f'#{tc} {" ".join(answer)}')
