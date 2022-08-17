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


ALPHA = ['a', 'e', 'i', 'o', 'u']
for T in range(1, int(input()) + 1):
    S = input().strip()

    for i in ALPHA:
        S = S.replace(i, '')

    print(f'#{T} {S}')
