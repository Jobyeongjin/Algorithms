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
arr = list(map(int, input().split()))
answer = []

for i in range(len(arr)-1, -1, -1):
    answer.insert(arr[i], i + 1)

print(*answer)
