import sys

sys.stdin = open("_파리퇴치.txt")

# 4. 파리퇴치

t = int(input())

for tc in range(1, t + 1):
    N, M = map(int, input().split())

    grid = [list(map(int, input().split())) for _ in range(N)]

    fly = []
    for i in range(N - M + 1):
        for j in range(N - M + 1):

            total = 0
            for x in range(M):
                for y in range(M):
                    total += grid[i + x][j + y]

            fly.append(total)

    print(f'#{tc} {max(fly)}')
