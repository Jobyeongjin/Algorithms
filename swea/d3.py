"""📝 View"""

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
