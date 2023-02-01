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

# 재귀함수의 한계를 10만까지 늘림
sys.setrecursionlimit(100_000)


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에

gate = int(input())
planes = [int(input()) for _ in range(int(input()))]

parent = [i for i in range(gate + 1)]


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    pa = find(a)
    pb = find(b)
    parent[pa] = pb


answer = 0
for plane in planes:
    temp = find(plane)
    if temp == 0:
        break
    union(temp, temp - 1)
    answer += 1

print(answer)
