# 파일 불러오기
from os import sep
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에

n = int(input())

hansu = 0
for i in range(1, n + 1):

    if i < 100:
        hansu += 1
    else:
        ns = list(map(int, str(i)))
        if ns[0] - ns[1] == ns[1] - ns[2]:
            hansu += 1

print(hansu)
