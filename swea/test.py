# 파일 불러오기
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에

t = int(input())

for tc in range(1, t + 1):
    n = list(map(int, input().split()))

    result = 0
    for i in n:
        if i % 2 != 0:
            result += i

    print(f'#{tc} {result}')
