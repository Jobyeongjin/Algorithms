# 파일 불러오기
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


n = []

for i in range(9):
    n.append(int(input()))

print(max(n))
print(n.index(max(n)) + 1)
