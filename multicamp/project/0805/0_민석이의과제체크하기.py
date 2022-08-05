import sys

sys.stdin = open("_민석이의과제체크하기.txt")

# 민석이의 과제 체크하기
t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())
    pass_ = list(map(int, input().split()))

    people = [i for i in range(1, N + 1)]

    set_pass = set(people) - set(pass_)

    print(f'#{tc}', end=' ')
    print(*set_pass)
