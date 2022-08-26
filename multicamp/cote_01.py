"""📝 직사각형 별찍기"""

N, M = map(int, input().split())

for _ in range(M):
    print('*' * N)


"""📝 x만큼 간격이 있는 n개의 숫자"""


def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)

    return answer
