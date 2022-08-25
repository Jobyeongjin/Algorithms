"""📝 View"""
# 맨 왼쪽과 오른쪽 2칸은 제외하고, 현재 건물의 왼쪽과 오른쪽 2칸의 최대 높이를 구한다.
# 현재 건물과 인접 건물의 높이 차가 0 이상이라면 조망권이 확보되고, 현재 건물과 가장 높은 인접 건물의 차를 구해서 더해준다.

T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    answer = []
    for i in range(2, N - 2):
        left = max(data[i - 1], data[i - 2])
        right = max(data[i + 1], data[i + 2])

        if data[i] - left > 0 and data[i] - right > 0:
            max_ = max(left, right)
            answer.append(data[i] - max_)

    print(f'#{tc} {sum(answer)}')

# 또는

T = 10
for tc in range(1, T + 1):
    N = int(input())
    data = list(map(int, input().split()))

    answer = 0
    for i in range(2, N - 2):
        left = max(data[i - 1], data[i - 2])
        right = max(data[i + 1], data[i + 2])

        answer += max(data[i] - max(left, right), 0)

    print(f'#{tc} {answer}')


"""📝 Flatten"""
# 가장 큰 수와 가장 작은 수를 찾아 인덱스로 접근해 반복할 때마다 해당 값을 -1, +1씩 값을 갱신한다.

T = 10
for tc in range(1, T + 1):
    N = int(input())
    BOX = list(map(int, input().split()))

    for _ in range(N):
        i_max = BOX.index(max(BOX))
        i_min = BOX.index(min(BOX))

        BOX[i_max] -= 1
        BOX[i_min] += 1

    print(f'#{tc} {max(BOX) - min(BOX)}')


"""📝 Sum"""
# 행의 합, 열의 합, 각각 대각선의 합을 구해서 가장 큰 값으로 갱신힌다.

M = 100
for tc in range(1, 11):
    N = int(input())
    numbers = [list(map(int, input().split())) for _ in range(M)]

    max_value = 0

    for i in range(M):
        total = 0
        for j in range(M):
            total += numbers[i][j]
        if total > max_value:
            max_value = total

    for i in range(M):
        total = 0
        for j in range(M):
            total += numbers[j][i]
        if total > max_value:
            max_value = total

    total = 0
    for i in range(M):
        total += numbers[i][i]
        if total > max_value:
            max_value = total

    total = 0
    for i in range(M):
        total += numbers[i][M-1-i]

        if total > max_value:
            max_value = total

    print(f'#{tc} {max_value}')


"""📝 String"""

for tc in range(1, 11):
    N = int(input())
    check = input().strip()
    char = input()

    print(f'#{tc} {char.count(check)}')


"""📝 회문 1"""
# 행과 열을 글자 수만큼 완전탐색하고, 해당 문자열을 뒤집어서 결과가 같으면 카운팅을 한다.

M = 8
for tc in range(1, 11):
    N = int(input())
    arr = [list(input().strip()) for _ in range(M)]

    answer = 0
    for i in range(M):
        for j in range(M - N + 1):
            r = []
            for k in range(N):
                r.append(arr[i][j + k])

            if r == r[::-1]:
                answer += 1

    for i in range(M - N + 1):
        for j in range(M):
            c = []
            for k in range(N):
                c.append(arr[i + k][j])

            if c == c[::-1]:
                answer += 1

    print(f'#{tc} {answer}')

# 또는

M = 8
for tc in range(1, 11):
    N = int(input())
    arr = [list(input().strip()) for _ in range(M)]
    rra = list(map(list, zip(*arr)))

    answer = 0
    for i in range(M):
        for j in range(M - N + 1):
            r = arr[i][j:j + N]
            c = rra[i][j:j + N]

            if r == r[::-1]:
                answer += 1

            if c == c[::-1]:
                answer += 1

    print(f'#{tc} {answer}')
