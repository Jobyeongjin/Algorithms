# 파일 불러오기
from sys import stdin

stdin = open("input.txt", "r")

input = stdin.readline

# 문제풀이는 여기에


coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    result = []
    for coin in coins:
        a = n // coin
        result.append(a)
        n -= a * coin

    print(f'#{tc}')
    print(*list(map(str, result)))
