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


n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]
q = deque(arr)
answer = []

while q:
    q.rotate(-(k - 1))
    answer.append(q.popleft())

print("<", end="")
print(*answer, sep=", ", end="")
print(">")
