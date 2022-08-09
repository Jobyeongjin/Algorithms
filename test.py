# 파일 불러오기
from collections import deque
from collections import Counter
import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


COM = int(input())
N = int(input())

JOIN = [[] for _ in range(COM + 1)]

for _ in range(N):
    a, b = map(int, input().split())
    JOIN[a].append(b)
    JOIN[b].append(a)

virus = []
for i in JOIN:
    if i.count(1):
        virus.append(i)

cnt = 0
for i in virus:
    for j in i:
        if j == 1:
            continue
        else:
            cnt += 1

print(cnt)
