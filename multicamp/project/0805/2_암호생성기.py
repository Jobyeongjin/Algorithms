import sys

sys.stdin = open("_암호생성기.txt")

# 3. 암호생성기

for _ in range(10):
    t = int(input())
    numbers = list(map(int, input().split()))

    i = 1
    while True:
        move = numbers.pop(0) - i
        numbers.append(move)

        i += 1
        if i > 5:
            i = 1

        if numbers[-1] <= 0:
            numbers[-1] = 0
            break

    print(f'#{t}', end=' ')
    print(*numbers)
