# 파일 불러오기
from importlib.util import find_spec
from sys import stdin
from pprint import pprint
from collections import Counter

stdin = open("input.txt", "r")

input = stdin.readline

# 문제풀이는 여기에

#

n = int(input())

for _ in range(n):
    words = list(input().split())

    reverse_ = []
    for word in words:
        reverse_.append(word[::-1])

    print(*reverse_)
