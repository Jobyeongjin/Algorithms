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


N = int(input())
CARD = list(map(int, input().split()))
M = int(input())
CHECK = list(map(int, input().split()))

dic = {}
for i in CARD:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(M):
    if CHECK[i] in dic:
        print(dic[CHECK[i]], end=' ')
    else:
        print(0, end=' ')
