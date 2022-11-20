# 파일 불러오기
from collections import deque
from collections import Counter
from itertools import permutations
import sys
import math
import heapq
import operator

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에

<<<<<<< HEAD
for _ in range(3):
    arr = list(map(int, input().split()))
    yut = arr.count(0)
    if yut == 1:
        print("A")
    elif yut == 2:
        print("B")
    elif yut == 3:
        print("C")
    elif yut == 4:
        print("D")
    else:
        print("E")
=======
n = int(input())

for _ in range(n):
    score = list(map(int, input().split()))
    score.sort()
    score.pop(0)
    score.pop(-1)
    if score[2] - score[0] >= 4:
        print("KIN")
    else:
        print(sum(score))
>>>>>>> 9fabf71 (Add: bj - doit)
