from collections import deque

# 퍼펙트 셔플

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    DECK = input().split()
    N = N // 2  # 총 카드의 절반을 찾아 인덱스로 접근하기 위함

    ONE = []
    if len(DECK) % 2 == 0:  # 덱의 길이가 짝수라면 / 정확히 절반
        for i in range(N):
            ONE.append(DECK[i])  # 첫번째 덱으로 추가 -> 인덱스로 접근해 해당 요소 추가
    else:
        for i in range(N + 1):  # 덱의 길이가 홀수라면 절반이 아니기 때문에 + 1
            ONE.append(DECK[i])

    TWO = []
    for i in DECK:  # 덱을 순환하면서
        if i in ONE:  # 첫번째 덱의 요소라면 패스하고
            continue
        else:
            TWO.append(i)  # 그 외 나머지를 두번째 덱으로 추가

    answer = []
    while ONE or TWO:  # 첫번째 또는 두번째 요소가 빌 때까지 반복
        if ONE:
            answer.append(ONE.pop(0))  # 0번 요소부터 하나씩 정답에 추가
        if TWO:
            answer.append(TWO.pop(0))

    print(f'#{tc} {" ".join(answer)}')


# 또는

T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    CARD = list(input().split())

    CUT = N - (N // 2)  # 그토록 바라던 컷 💡
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
