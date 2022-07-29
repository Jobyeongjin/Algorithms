# 최빈수 구하기

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
