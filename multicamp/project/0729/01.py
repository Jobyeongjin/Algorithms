# 소득불균형

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    money = list(map(int, input().split()))

    # 평균값
    mean = sum(money) / n

    cnt = 0
    # 평균값보다 작거나 같으면 카운팅
    for i in money:
        if i <= mean:
            cnt += 1

    print(f'#{tc} {cnt}')
