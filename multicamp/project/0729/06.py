# 신용카드 만들기 2

t = int(input())

for tc in range(1, t + 1):
    n = list(input())  # 문자열 리스트

    st = int(n[0])  # 스타트 번호를 찾아 조건문 활용
    cnt = 0
    if st == 3 or st == 4 or st == 5 or st == 6 or st == 9:
        for i in n:
            if i != '-':  # '-' 뺀 숫자만 카운팅
                cnt += 1
        if cnt == 16:  # 카드번호가 16개라면 1, 아니면 0
            print(f'#{tc}', 1)
        else:
            print(f'#{tc}', 0)
    else:
        print(f'#{tc}', 0)
