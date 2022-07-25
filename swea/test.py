# 파일 불러오기
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if i < x:
        print(i, end=' ')
