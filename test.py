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


M = 8
for tc in range(1, 11):
    N = int(input())
    arr = [list(input().strip()) for _ in range(M)]

    answer = 0
    for i in range(M):
        for j in range(M - N + 1):
            r = []
            for k in range(N):
                r.append(arr[i][j + k])

            if r == r[::-1]:
                answer += 1

    for i in range(M - N + 1):
        for j in range(M):
            c = []
            for k in range(N):
                c.append(arr[i + k][j])

            if c == c[::-1]:
                answer += 1

    print(f'#{tc} {answer}')
