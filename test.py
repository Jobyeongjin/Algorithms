# 파일 불러오기
from collections import deque
import sys
from pprint import pprint
from collections import Counter

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 문제풀이는 여기에

t = int(input())
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, t + 1):
    n = int(input())

    snail = [[0] * n for _ in range(n)]
    # 초기 좌표 및 회전 방향 0
    x, y = 0, 0
    rotate = 0

    for i in range(1, n * n + 1):
        snail[x][y] = i  # 순차적으로 좌표 입력
        x += dx[rotate]
        y += dy[rotate]
        # 좌표가 리스트 범위 밖이거나 이미 값이 부여된 경우
        if not 0 <= x < n or not 0 <= y < n or snail[x][y] != 0:
            x -= dx[rotate]
            y -= dy[rotate]
            rotate = (rotate + 1) % 4
            x += dx[rotate]
            y += dy[rotate]

    print(f'#{tc}')

    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=' ')
        print()
