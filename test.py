# 파일 불러오기
from sys import stdin

stdin = open("input.txt", "r")

input = stdin.readline

# 문제풀이는 여기에

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    word = ''
    for i in range(1, n + 1):
        n, m = input().split()
        word += n * int(m)

    print(f'#{tc}')

    for i in range(0, len(word), 10):
        # print(word[i:i + 10])
        print(i)
