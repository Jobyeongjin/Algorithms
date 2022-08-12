# 반반

T = int(input())

for tc in range(1, T + 1):
    alpha = input()
    TWO_SET = set(alpha)  # 중복 제거

    if len(TWO_SET) == 2:  # 셋의 길이가 2라면 "Yes", 아니면 "No"
        print(f'#{tc} {"Yes"}')
    else:
        print(f'#{tc} {"No"}')


# 또는

t = int(input())

for i in range(1, t + 1):
    s = input()
    chk = set(s)  # 중복 제거

    len_ = len(s) - len(chk)  # 입력 문자 - 중복 제거한 문자

    if len_ == 2 and len(chk) == 2:
        print(f'#{i} Yes')
    else:
        print(f'#{i} No')


# 또는

for tc in range(1, int(input()) + 1):
    S = set(input())  # 중복 제거

    if len(S) == 2:  # 셋의 길이가 2라면
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')


# 또는

T = int(input())
for tc in range(1, T + 1):
    S = input()

    for i in range(4):
        if S.count(S[i]) != 2:
            print(f'#{tc} No')
            break
    else:
        print(f'#{tc} Yes')
