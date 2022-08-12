# 1. 민석이의 과제 체크하기 🐳
t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())
    pass_ = list(map(int, input().split()))

    people = [i for i in range(1, N + 1)]

    set_pass = set(people) - set(pass_)

    print(f'#{tc}', end=' ')
    print(*set_pass)


# 2. 조교의 성적 매기기 🐳
t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())

    RANK = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    total_score = []
    for i in range(N):
        a, b, c = map(int, input().split())

        score = (a * 0.35) + (b * 0.45) + (c * 0.20)
        total_score.append(score)

    student = total_score[K - 1]
    total_score.sort(reverse=True)
    result = total_score.index(student) // (N // 10)

    print(f'#{tc} {RANK[result]}')


# 3. 암호생성기 🐳
for _ in range(10):
    t = int(input())
    numbers = list(map(int, input().split()))

    i = 1
    while True:
        move = numbers.pop(0) - i
        numbers.append(move)

        i += 1
        if i > 5:
            i = 1

        if numbers[-1] <= 0:
            numbers[-1] = 0
            break

    print(f'#{t}', end=' ')
    print(*numbers)


# 4. 파리퇴치 🐳
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


# 어디에 단어가 들어갈 수 있을까 🐳
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


# 괄호 짝짓기 🐳
for tc in range(1, 11):
    n = int(input())
    bracket = input()

    stack = []
    left = ['(', '[', '{', '<']
    right = [')', ']', '}', '>']

    answer = 1
    for i in bracket:
        if i in left:
            stack.append(i)
        else:
            if left.index(stack[-1]) == right.index(i):
                stack.pop()
            else:
                answer = 0
                break

    print(f'#{tc} {answer}')
