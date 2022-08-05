import sys

sys.stdin = open("_파리퇴치.txt")

# 4. 파리 퇴치

t = int(input())

for tc in range(1, t + 1):
    N, M = map(int, input().split())
    # 파리 수가 있는 그리드 생성
    grid = [list(map(int, input().split())) for _ in range(N)]

    fly = []  # 16번(1번 케이스 기준) 때려잡은 파리 수 리스트
    # 이중 for문 안에 이중 for문
    for i in range(N - M + 1):  # 파리채가 이동하는 만큼의 인덱스 범위를 생각해봐야 한다
        for j in range(N - M + 1):

            total = 0  # 파리잡은 수
            for x in range(M):  # 파리채의 크기의 반복문
                for y in range(M):
                    total += grid[i + x][j + y]  # 해당 좌표값을 모두 더하기

            fly.append(total)

    print(f'#{tc} {max(fly)}')


# 또는
def hap(lst):  # 리스트의 합을 리턴
    f_sum = 0

    for i in lst:  # 이차원인 lst를 하나씩 일차원 리스트로 반복
        f_sum += sum(i)  # 리스트의 합

    return f_sum


for tc in range(1, int(input()) + 1):
    n, m = map(int, input().split())

    fly = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            answer = max(answer, hap([fly[i + x][j:j + m] for x in range(m)]))

    print(f'#{tc} {answer}')


# 또는
t = int(input())

for i in range(1, t + 1):
    n, m = map(int, input().split())

    fly = []
    for j in range(n):
        fly.append(list(map(int, input().split())))
    # 잡을 수 있는 파리 수를 저장할 2차원 리스트
    result = [[0] * (n - m + 1) for _ in range(n - m + 1)]

    for j in range(n - m + 1):
        for k in range(n - m + 1):
            # 파리채의 길이만큼 행, 열로 이동하며 파리 수 누적
            sum_ = 0
            for a in range(m):
                for b in range(m):
                    sum_ += fly[j + a][k + b]
            # 잡을 수 있는 파리의 수를 2차원 리스트에 저장
            result[j][k] = sum_

    print(f'#{i} {max(map(max, result))}')
