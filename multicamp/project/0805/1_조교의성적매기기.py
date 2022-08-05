import sys

sys.stdin = open("_조교의성적매기기.txt")

# 조교의 성적 매기기

t = int(input())

for tc in range(1, t + 1):
    N, K = map(int, input().split())

    RANK = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    total_score = []  # 학생들의 총점 리스트
    for i in range(N):
        a, b, c = map(int, input().split())

        score = (a * 0.35) + (b * 0.45) + (c * 0.20)  # 총합 구하기
        total_score.append(score)

    student = total_score[K - 1]  # 학점을 알고싶은 학생의 점수
    total_score.sort(reverse=True)  # 내림차순 정렬
    result = total_score.index(student) // (N // 10)  # 학생 수에 따라 성적 비율이 달라짐

    print(f'#{tc} {RANK[result]}')


# 또는
for tc in range(1, int(input()) + 1):
    n, k = map(int, input().split())

    record = ["0", "A+", "A0", "A-", "B+", "B0", "B-", "C+", "C0", "C-", "D0"]

    rate = n // 10

    student = []
    for i in range(1, n + 1):
        mid, end, home = map(int, input().split())

        p = mid * 0.35 + end * 0.45 + home * 0.2
        if i == k:
            data = p

        student.append(p)

    student = sorted(student, reverse=True)

    find = student.index(data) + 1

    for i in range(1, 11):
        if rate * i >= find:
            print(f'#{tc} {record[i]}')
            break


# 또는
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
    # 성적을 기준으로 점수를 정렬
    score = sorted(score.items(), key=lambda x: (-x[1], x[0]))

    for j in range(n):
        # 학생의 번호가 점수 튜플의 첫 번째 인덱스 값과 같다면
        if k == score[j][0]:
            # 해당 인덱스 값 저장
            idx = score.index(score[j])

    print(f'#{i} {grade[idx]}')
