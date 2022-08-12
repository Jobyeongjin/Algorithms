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
