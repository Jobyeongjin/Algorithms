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


R = int(input())

UCLID = R * R * math.pi
TAXI = 2 * R * R

print(round(UCLID, 6))
print(round(TAXI, 6))
