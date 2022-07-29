# 신용카드 만들기 1

t = int(input())

for tc in range(1, t + 1):
    card = list(input().split())

    odd = []  # 홀수 리스트
    even = []  # 짝수 리스트
    for i in range(len(card)):
        if i % 2 == 0:
            odd += card[i]
        else:
            even += card[i]

    odd_sum = 0  # 홀수자리는 2를 곱하기
    for i in odd:
        odd_sum += int(i) * 2

    even_sum = 0  # 짝수자리는 그대로 더하기
    for i in even:
        even_sum += int(i)

    total = odd_sum + even_sum
    for i in range(10):
        if (total + i) % 10 == 0:  # 최종 더한 값에서 10으로 나눴을 때 떨어지는 수라면 출력
            print(f'#{tc} {i}')
