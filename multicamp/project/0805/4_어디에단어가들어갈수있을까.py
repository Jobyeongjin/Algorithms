import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 어디에 단어가 들어갈 수 있을까

t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())

    puzzle = [list(map(int, input().split())) for _ in range(N)]

    row = 0
    for x in range(N):

        cnt = 0
        for y in range(N):
            if puzzle[x][y] == 1:
                cnt += 1
            else:
                if cnt == K:
                    row += 1
                cnt = 0

        if cnt == K:
            row += 1

    col = 0
    for x in range(N):

        cnt = 0
        for y in range(N):
            if puzzle[y][x] == 1:
                cnt += 1
            else:
                if cnt == K:
                    col += 1
                cnt = 0

        if cnt == K:
            col += 1

    print(f'#{tc} {row + col}')
