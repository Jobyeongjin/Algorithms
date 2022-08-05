import sys

sys.stdin = open("_민석이의과제체크하기.txt")

# 민석이의 과제 체크하기
t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())
    pass_ = list(map(int, input().split()))  # 과제를 제출한 사람

    people = [i for i in range(1, N + 1)]  # 학생 수

    fail = set(people) - set(pass_)  # 학생 수에서 제출한 사람은 제외, 셋을 사용해 중복 제거

    print(f'#{tc}', end=' ')
    print(*fail)


# 또는
for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    homework = list(map(int, input().split()))

    answer = []

    for i in range(1, n + 1):
        if i not in homework:  # 과제를 제출한 사람이 아니라면 정답에 추가
            answer.append(i)

    print(f'#{tc} {" ".join(map(str, answer))}')


# 또는
t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())

    submit = list(map(int, input().split()))
    result = [0] * (n + 1)  # 과제의 결과를 저장하기 위한 리스트

    for j in submit:
        result[j] = 1  # 과제를 제출했다면 해당 인덱스를 1로 변경

    print(f'#{i}', end=' ')

    for j in range(1, n + 1):
        if result[j] == 0:  # 결과가 0이라면 과제를 제출 안한 사람
            print(j, end=' ')

    print()
