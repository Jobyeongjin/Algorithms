# 최빈수 구하기 🐳

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    score = list(map(int, input().split()))

    # 리스트로 정렬하고 해당 하는 숫자가 나오면 1씩 추가
    arr = [0] * 101
    for i in score:
        arr[i] += 1

    result = []
    # 최대값을 변수로 지정하고, 반복문 안에서 최대값이 나오면 결과값에 추가
    max_ = max(arr)
    for i in range(len(arr)):
        if arr[i] == max_:
            result.append(i)

    print(f'#{tc} {max(result)}')


# 소득불균형 🐳

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


# 문자열의 거울상 🐳

t = int(input())

for tc in range(1, t + 1):
    alpha = list(input())  # 문자열 리스트

    list_ = ''
    reverse_ = alpha[::-1]  # 순서 뒤집기

    for i in reverse_:  # 반복문, 조건문을 활용하여 문자 변경
        if i == 'b':
            list_ += 'd'
        elif i == 'd':
            list_ += 'b'
        elif i == 'p':
            list_ += 'q'
        else:
            list_ += 'p'

    print(f'#{tc} {list_}')


# 직사각형 길이 찾기 🐳

t = int(input())

for tc in range(1, t + 1):
    num = list(map(int, input().split()))

    # 세 자릿 수에 조건을 걸어 출력
    if num[0] == num[1]:
        print(f'#{tc} {num[2]}')
    elif num[0] != num[1] and num[0] != num[2]:
        print(f'#{tc} {num[0]}')
    else:
        print(f'#{tc} {num[1]}')


# 신용카드 만들기 1 🐳

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


# 신용카드 만들기 2 🐳

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


# 암호문 1 🚨

for tc in range(1, 11):
    ori_n = int(input())  # 원본 뭉치의 갯수
    data = list(map(int, input().split()))  # 원본
    cmd = int(input())  # 명령어, 무시해도 됨
    cmd_order = list(input().split())  # 삽입할 명령어 뭉치들

    type = ''  # 명령어 파악
    pos = -1  # 삽입 위치
    cnt = -1  # 삽입 갯수
    for i in range(len(cmd_order)):
        # 암호화 첫번째 단어 체크 I 1 5
        if cmd_order[i] == 'I':
            type = cmd_order[i]
            pos = -1
            cnt = -1
        else:
            # 두번째 단어 체크
            if type == 'I':
                if pos == -1:
                    pos = int(cmd_order[i])
                    continue
                else:
                    # 세번째 단어 체크
                    if cnt == -1:
                        cnt = int(cmd_order[i])
                        continue

                    data.insert(pos, cmd_order[i])
                    pos += 1

    print(f'#{tc}', end=' ')
    print(*data[:10])
