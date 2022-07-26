# 파일 불러오기
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에

n = int(input())

for _ in range(n):
    score = list(map(int, input().split()))
    average = sum(score[1:]) / score[0]

    cnt = 0
    for i in score[1:]:
        if i > average:
            cnt += 1

    per = (cnt / score[0]) * 100

    # round 함수는 사용불가, 40.0%는 소숫점 표기가 안됨 🚨
    print('{:.3f}%'.format(per))
