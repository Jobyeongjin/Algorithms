from collections import deque

# 퍼펙트 셔플

for tc in range(1, int(input()) + 1):
    N = int(input())
    DECK = input().split()
    cut = N - N // 2

    one = deque(DECK[:cut])
    two = deque(DECK[cut:])

    answer = []
    while one or two:
        if one:
            answer.append(one.popleft())
        if two:
            answer.append(two.popleft())

    print(f'#{tc} {" ".join(answer)}')


# 또는


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    CARD = list(input().split())

    CUT = N - (N // 2)  # 바라던 컷 💡
    F_CARD = deque(CARD[:CUT])  # 디큐(문자열 슬라이싱)
    S_CARD = deque(CARD[CUT:])

    result = []
    while F_CARD or S_CARD:
        if F_CARD:
            result.append(F_CARD.popleft())  # 하나씩 빼면서 결과에 담아주기
        if S_CARD:
            result.append(S_CARD.popleft())

    print(f'#{tc}', end=' ')
    print(*result)


# 또는


for tc in range(1, int(input()) + 1):
    N = int(input())
    word = list(map(str, input().split()))

    K = N % 2
    if not K:  # 짝수라면
        A = word[:N // 2]  # 카드의 중앙값 기준으로 반환
        B = word[N // 2:]
        print(f'#{tc}', end=' ')

        for i in range(len(A)):
            print(A[i], end=' ')
            print(B[i], end=' ')

    else:  # 홀수라면 + 1
        A = word[:len(word) // 2 + 1]
        B = word[len(word) // 2 + 1:]
        print(f'#{tc}', end=' ')

        for i in range(len(B)):
            print(A[i], end=' ')
            print(B[i], end=' ')

        print(A[-1], end=' ')  # A의 마지막 요소 출력
    print()


# 또는


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    BOX = list(map(str, input().split()))

    ONE = BOX[:(N + 1) // 2]
    TWO = BOX[(N + 1) // 2:]

    print(f'#{tc}', end=' ')

    for j in range(len(TWO)):  # 짧은 리스트 길이 기준, 순서대로 출력
        print(ONE[j], TWO[j], end=' ')

    if N % 2 == 1:  # 리스트에 남아있다면, 남은 마지막 요소 출력
        print(ONE[-1], end=' ')
    print()
