# 파일 불러오기
from collections import deque
import sys
from collections import Counter

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


n = list(map(int, input()))

print(sum(n))
