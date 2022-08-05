import sys
from collections import deque

sys.stdin = open("_암호생성기.txt")

# 3. 암호생성기

for _ in range(10):  # 테스트 케이스는 10개
    t = int(input())
    numbers = list(map(int, input().split()))  # 8개의 숫자 암호 리스트

    i = 1
    while True:
        move = numbers.pop(0) - i  # 숫자 암호 리스트의 첫번째 요소를 -i(1 ~ 5)만큼 빼고 리스트에서 제거
        numbers.append(move)  # 다시 넣기 (맨 뒤로)
        i += 1

        if i > 5:  # i는 5까지만 올라가고 그 이상은 리셋
            i = 1

        if numbers[-1] <= 0:  # 리스트의 마지막 요소가 0일때까지만 반복
            numbers[-1] = 0
            break

    print(f'#{t}', end=' ')
    print(*numbers)


# 또는
for _ in range(10):
    n = int(input())
    nums = deque(list(map(int, input().split())))

    cnt = 1
    while True:
        if cnt == 6:  # 카운트가 6이면 리셋
            cnt = 1

        nums[0] -= cnt  # 리스트 맨 앞 요소는 카운트만큼 빼기

        if nums[0] <= 0:  # 맨 앞이 0이 되면
            nums[0] = 0  # 0으로 설정
            # rotate 함수는 리스트를 이동시킨다. 양수면 오른쪽으로, 음수면 왼쪽으로 이동한다 💡
            nums.rotate(-1)
            break
        else:  # 0이 아니면 카운트 1씩 올려주고 리스트를 왼쪽으로 회전
            cnt += 1
            nums.rotate(-1)

    print(f'#{n}', end=' ')
    print(*nums, sep=' ')


# 또는
for _ in range(10):
    n = int(input())
    pw = deque(list(map(int, input().split())))

    cnt = 1
    while True:
        if cnt == 6:
            cnt = 1

        temp = pw.popleft()  # 맨 앞의 요소를 뽑아 temp에 저장
        if temp - cnt > 0:  # (temp - cnt)가 0보다 크면 뒤에 저장
            pw.append(temp - cnt)
        else:
            pw.append(0)  # 작으면 0으로 넣고 끝내기
            break

        cnt += 1

    print(f'#{n}', end=' ')
    print(*pw)
