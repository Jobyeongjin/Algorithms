# 반반

T = int(input())

for tc in range(1, T + 1):
    alpha = input()
    TWO_LIST = set(alpha)  # 중복 제거

    if len(TWO_LIST) == 2:  # 리스트 요소 길이가 2라면 "Yes", 아니면 "No"
        print(f'#{tc} {"Yes"}')
    else:
        print(f'#{tc} {"No"}')
