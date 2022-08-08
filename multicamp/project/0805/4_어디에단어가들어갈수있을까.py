import sys

sys.stdin = open("_어디에단어가들어갈수있을까.txt")

# 어디에 단어가 들어갈 수 있을까

t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())
    # 0과 1로 구성된 퍼즐
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    # 행 구하기
    row = 0
    for x in range(N):

        cnt = 0
        for y in range(N):
            if puzzle[x][y] == 1:  # 퍼즐의 해당 좌표가 1이라면 카운팅
                cnt += 1
            else:
                if cnt == K:  # 카운트가 K가 되면 row에 1씩 더하고 리셋
                    row += 1
                cnt = 0

        if cnt == K:  # 마지막 카운팅
            row += 1

    # 열 구하기
    col = 0
    for x in range(N):

        cnt = 0
        for y in range(N):
            if puzzle[y][x] == 1:  # 행과 똑같으나 좌표값만 다르게 설정
                cnt += 1
            else:
                if cnt == K:
                    col += 1
                cnt = 0

        if cnt == K:
            col += 1

    print(f'#{tc} {row + col}')


# 또는
for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())
    maps = [list(map(str, input().split())) for _ in range(n)]
    # zip 함수는 maps의 각각의 열을 각각 행으로 가져온다 💡
    maps2 = list(map(list, zip(*maps)))

    cnt = 0
    for i in maps:
        # 문자열을 붙이고, 0을 기준으로 나누면 0과 1이 분리가 된다 💡
        # 예시 : ['', '', '111']
        cnt += ''.join(i).split('0').count('1' * k)  # 1이 k만큼 있다면 카운팅

    for i in maps2:
        cnt += ''.join(i).split('0').count('1' * k)

    print(f'#{tc} {cnt}')


# 또는
t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())

    word = []
    fit = []
    result = 0

    for j in range(n):
        word.append(list(map(int, input().split())))

    for j in range(n):
        r_cnt = 0
        c_cnt = 0

        for l in range(n):
            # 행
            if word[j][l] == 1:  # 행에서 글자가 들어갈 수 있는 칸이라면
                r_cnt += 1  # 카운팅
                if l == n - 1:  # 한 행을 끝까지 반복했다면
                    fit.append(r_cnt)  # 누적된 카운트 값을 저장
            else:  # 끝까지 반복하지 않고 벽을 만난다면
                fit.append(r_cnt)  # 누적된 카운트 값을 저장하고 0으로 초기화
                r_cnt = 0
            # 열
            if word[l][j] == 1:  # 좌표만 바꾸어 행을 그대로 전치
                c_cnt += 1
                if l == n - 1:
                    fit.append(c_cnt)
            else:
                fit.append(c_cnt)
                c_cnt = 0

    for j in fit:
        if j == k:  # 원하는 길이의 글자와 빈칸의 길이가 같다면
            result += 1

    print(f'#{i} {result}')


# 또는
t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]

    row = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                cnt += 1
            if puzzle[i][j] == 0:
                if cnt == K:
                    row += 1
                cnt = 0

        if cnt == K:
            row += 1

    col = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if puzzle[j][i] == 1:
                cnt += 1
            if puzzle[j][i] == 0:
                if cnt == K:
                    row += 1
                cnt = 0

        if cnt == K:
            row += 1

    print(f'#{tc} {row + col}')
