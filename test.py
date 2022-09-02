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


n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])

arr = []
while q:
    for i in range(k - 1):
        q.append(q.popleft())
    arr.append(q.popleft())

print('<', end='')
print(*arr, sep=', ', end='')
print('>')
