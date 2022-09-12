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


"""📝 거듭 제곱"""

t = 10
for tc in range(1, t + 1):
    n = int(input())
    a, b = map(int, input().split())

    print(f'#{tc} {a ** b}')


"""📝 Magnetic"""

t = 10
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()) for _ in range(n))

    cnt = 0
    for i in range(n):
        stack = []
        check = False
        for j in range(n):
            if arr[j][i] == 1:
                stack.append(1)
            if stack and arr[j][i] == 2:
                stack.clear()
                cnt += 1

    print(f'#{tc} {cnt}')


"""📝 GNS"""

t = int(input())
alpha = ['ZRO', 'ONE', 'TWO', 'THR', 'FOR', 'FIV', 'SIX', 'SVN', 'EGT', 'NIN']

for _ in range(1, t + 1):
    tc, n = input().split()
    s = input().split()

    dic = {}
    for i in range(len(alpha)):
        dic[alpha[i]] = 0

    for i in s:
        dic[i] += 1

    print(tc)
    for i in alpha:
        print(' '.join([i] * dic[i]), end=' ')
    print()


"""📝 암호생성기"""

t = 10
for _ in range(t):
    tc = int(input())
    n = list(map(int, input().split()))

    i = 1
    while True:
        move = n.pop(0) - i
        n.append(move)
        i += 1

        if i > 5:
            i = 1

        if n[-1] <= 0:
            n[-1] = 0
            break

    print(f'#{tc}', end=' ')
    print(*n)


"""📝 암호문1 🚨"""

for tc in range(1, 11):
    n = int(input())
    base = list(map(int, input().split()))
    o = int(input())
    order = list(input().split())

    type = ''
    pos = -1
    cnt = -1
    for i in range(len(order)):  # 인덱스 접근
        if order[i] == 'I':  # I라면 해당값 리셋
            type = order[i]
            pos = -1
            cnt = -1
        else:  # 숫자라면
            if type == 'I' and pos == -1:  # I인데, 위치값이 지정되지 않았다면
                pos = int(order[i])
                continue
            else:
                if cnt == -1:  # 위치는 지정되었는데, 삽입할 개수가 지정되지 않았다면
                    cnt = int(order[i])
                    continue

                base.insert(pos, order[i])  # 해당 위치에 값 입력
                pos += 1

    print(f'#{tc}', end=' ')
    print(*base[:10])
