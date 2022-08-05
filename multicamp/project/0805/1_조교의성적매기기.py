import sys

sys.stdin = open("_조교의성적매기기.txt")

# 조교의 성적 매기기

t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())

    RANK = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    total_score = []
    for i in range(N):
        a, b, c = map(int, input().split())

        score = (a * 0.35) + (b * 0.45) + (c * 0.20)
        total_score.append(score)

    student = total_score[K - 1]
    total_score.sort(reverse=True)
    result = total_score.index(student) // (N // 10)

    print(f'#{tc} {RANK[result]}')
