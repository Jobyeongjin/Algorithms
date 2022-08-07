# 파일 불러오기
from collections import deque
import sys
from pprint import pprint
from collections import Counter

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 문제풀이는 여기에

N = int(input())

members = [list(input().split()) for _ in range(N)]
members.sort(key=lambda x: int(x[0]))

for i in members:
    print(i[0], i[1])
