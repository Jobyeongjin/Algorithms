# 직사각형 길이 찾기

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
