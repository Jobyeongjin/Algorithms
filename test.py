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


n = int(input())

answer = []
for i in range(1, n + 1):
    arr = [n]
    arr.append(i)

    idx = 1
    while True:
        next_n = arr[idx - 1] - arr[idx]
        if next_n < 0:
            break
        arr.append(next_n)
        idx += 1

    if len(answer) < len(arr):
        answer = arr

print(len(answer))
print(*answer)
