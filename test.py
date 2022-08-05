# 파일 불러오기
from collections import deque
from sys import stdin
from pprint import pprint
from collections import Counter

stdin = open("input.txt", "r")

input = stdin.readline

# 문제풀이는 여기에
g = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

t = int(input())

for i in range(1, t + 1):
    n, k = map(int, input().split())

    grade = []
    score = {}
    idx = 0
    # 학생 수만큼 등급을 배로 늘리기
    for j in g:
        for l in range(n // 10):
            grade.append(j)

    for j in range(1, n + 1):
        mid, final, hw = map(int, input().split())
        score[j] = (mid * 0.35) + (final * 0.45) + (hw * 0.2)

    score = sorted(score.items(), key=lambda x: (-x[1], x[0]))

    for j in range(n):
        if k == score[j][0]:
            idx = score.index(score[j])

    print(f'#{i} {grade[idx]}')
