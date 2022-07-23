# 파일 불러오기
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에

t = int(input())

for tc in range(1, t + 1):
    # 학생 수 n, 학점이 궁금한 학생 번호 k
    n, k = map(int, input().split())
    # 학생들의 총점 리스트
    data = []
    # 평점
    RANK = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(n):
        # 시험 및 과제 점수
        a, b, c = map(int, input().split())
        # 총점 구하기
        sum = (a * 0.35) + (b * 0.45) + (c * 0.20)
        data.append(sum)
    # 구하고자 하는 학생 점수
    score = data[k - 1]
    # 내림차순으로 정렬
    data.sort(reverse=True)
    # 구하고자 하는 학생의 점수를 인덱스로 접근하고
    # 동일한 평점을 부여받은 10명의 학생들은 나누기
    result = data.index(score) // (n//10)
    # 해당 랭크 출력
    print(f'#{tc} {RANK[result]}')
