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


n, m = map(int, input().split())
arr = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])

cnt = 0
for i in arr:
    while True:
        if q[0] == i:
            q.popleft()
            break
        else:
            if q.index(i) < len(q) // 2:
                q.rotate(-1)
                cnt += 1
            else:
                q.rotate(1)
                cnt += 1

print(cnt)
