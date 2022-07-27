# 파일 불러오기
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에

n = int(input())

for i in range(1, n):
    sum_ = 0
    for j in str(i):
        sum_ = sum_ + int(j)

    sum_ = sum_ + i

    if n == sum_:
        print(i)
        break
else:
    print(0)
