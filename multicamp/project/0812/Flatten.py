# Flatten

T = 10
for tc in range(1, T + 1):
    N = int(input())
    BOX = list(map(int, input().split()))  # 박스 리스트

    for _ in range(N):  # 입력으로 주어진 총 이동수만큼 반복
        MAX = max(BOX)  # 가장 큰 수
        MIN = min(BOX)  # 가장 작은 수

        I_MAX = BOX.index(MAX)  # 해당 인덱스 구하기
        I_MIN = BOX.index(MIN)

        BOX[I_MAX] -= 1  # 해당 인덱스 요소 값에서 큰 값은 빼주고 작은 값은 더해준다
        BOX[I_MIN] += 1

    print(f'#{tc} {max(BOX) - min(BOX)}')
