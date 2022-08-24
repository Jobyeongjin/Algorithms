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


T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    answer = 0
    for i in range(2, N - 2):
        left = max(data[i - 1], data[i - 2])
        right = max(data[i + 1], data[i + 2])

        answer += max(data[i] - max(left, right), 0)

    print(f'#{tc} {answer}')
