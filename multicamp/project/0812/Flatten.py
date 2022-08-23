# Flatten

T = 10
for tc in range(1, T + 1):
    N = int(input())
    BOX = list(map(int, input().split()))  # 박스 리스트

    for _ in range(N):  # 입력으로 주어진 총 이동수만큼 반복
        max_ = max(BOX)  # 가장 큰 수
        min_ = min(BOX)  # 가장 작은 수

        i_max = BOX.index(max_)  # 해당 인덱스 구하기
        i_min = BOX.index(min_)

        BOX[i_max] -= 1  # 해당 인덱스 요소 값에서 큰 값은 빼주고 작은 값은 더해준다
        BOX[i_min] += 1

    print(f'#{tc} {max(BOX) - min(BOX)}')


# 또는


for i in range(1, 11):
    dump = int(input())
    box = list(map(int, input().split()))

    for _ in range(dump):
        max_idx = box.index(max(box))  # 풀이방식은 동일하나 이 부분 💡
        min_idx = box.index(min(box))  # 한번에 가장 큰 수와 작은 수의 인덱스 구하기

        box[max_idx] -= 1
        box[min_idx] += 1

    f_max = box.index(max(box))
    f_min = box.index(min(box))

    print(f'#{i} {box[f_max] - box[f_min]}')


# 또는


for tc in range(1, 11):
    dump = int(input())  # 평탄화 횟수
    N = list(map(int, input().split()))

    while dump:
        N[N.index(max(N))] -= 1  # 가장 높은 인덱스 값을 찾아 - 1
        N[N.index(min(N))] += 1  # 가장 낮은 인덱스 값을 찾아 + 1

        dump -= 1  # 평탄화 수 - 1

    print(f'#{tc} {max(N) - min(N)}')  # 큰 값과 작은 값의 차이 출력


# 또는


for tc in range(1, 11):  # 위랑 풀이는 동일하지만
    N = int(input())
    BOX = list(map(int, input().split()))

    for _ in range(N):  # 반복문을 어떻게 사용하느냐의 차이가 있음 💡
        BOX[BOX.index(max(BOX))] -= 1
        BOX[BOX.index(min(BOX))] += 1

    print(f'#{tc} {max(BOX) - min(BOX)}')


# 또는


for tc in range(1, 11):
    N = int(input())
    BOX = list(map(int, input().split()))

    for _ in range(N):
        if len(set(BOX)) == 1:  # 이미 평탄화된 상태라면
            print(f'#{tc} 0')
            break

        BOX[BOX.index(max(BOX))] -= 1  # 평탄화, 가장 큰 수는 내리고
        BOX[BOX.index(min(BOX))] += 1  # 가장 작은 수는 올리기

    else:
        print(f'#{tc} {max(BOX) - min(BOX)}')
