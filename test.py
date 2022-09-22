# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math
import heapq

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


c, r = map(int, input().split())
paper = [[0] * c for _ in range(r)]
n = int(input())

for _ in range(n):
    cut, line = map(int, input().split())
    for i in range(r):
        for j in range(c):
            if cut == 0:
                if i >= line:
                    paper[i][j] += 1
            if cut == 1:
                if j >= line:
                    paper[i][j] += 100

answer = {}
answer = Counter(answer)
for i in range(r):
    dic = {}
    dic = Counter(paper[i])
    answer += dic

print(max(answer.values()))
