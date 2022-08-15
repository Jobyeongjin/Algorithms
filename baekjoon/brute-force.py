import sys

input = sys.stdin.readline

'''블랙잭 🐳'''

N, M = map(int, input().split())
CARD = list(map(int, input().split()))

answer = 0
for i in range(N - 2):  # 인덱스를 넘지않게 3중 반복문 생성
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = CARD[i] + CARD[j] + CARD[k]  # 카드 3장의 합

            if answer < total <= M:  # M을 넘지않으면서 가까운 수로 저장
                answer = total
            if total == M:
                answer = total

print(answer)


'''분해합 🐳'''

N = int(input())

answer = 0
for i in range(1, N + 1):  # 1부터 N까지 반복한 정수
    LIST = list(map(int, str(i)))  # 문자형으로 나누고 다시 숫자형 리스트로 입력
    SUM = i + sum(LIST)  # 분해합

    if SUM == N:
        answer = i
        break

print(answer)


'''덩치 🐳'''

N = int(input())

PEOPLE = [list(map(int, input().split())) for _ in range(N)]  # 이차원 리스트로 입력

for i in PEOPLE:  # 완전 탐색으로 리스트 순회
    RANK = 1  # 기본값
    for j in PEOPLE:
        if i[0] < j[0] and i[1] < j[1]:  # 다음 리스트 값이 더 크다면 RAMK + 1
            RANK += 1

    print(RANK, end=' ')


'''체스판 다시 칠하기 🐳 🚨'''

N, M = map(int, input().split())

CHESS = [input().strip() for _ in range(N)]

cnt = []
for a in range(N - 7):  # 완전 탐색, 8 * 8 크기의 체스판
    for b in range(M - 7):
        W = 0  # W, B로 시작하는 경우 바뀐 체스판을 카운팅
        B = 0
        for i in range(a, a + 8):  # 시작, 끝점을 가리키는 이중 반복문
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:  # 짝수인 경우 첫번째 값과 동일해야 한다💡
                    if CHESS[i][j] != 'W':  # 흰색이 아니라면 흰색으로 카운팅
                        W += 1
                    if CHESS[i][j] != 'B':
                        B += 1
                else:  # 홀수인 경우 첫번째 값과 달라야 한다💡
                    if CHESS[i][j] != 'B':
                        W += 1
                    if CHESS[i][j] != 'W':
                        B += 1

        cnt.append(min(W, B))

print(min(cnt))


'''영화감독 숌 🐳'''

N = int(input())

TITLE = 666
cnt = 0
while True:
    if '666' in str(TITLE):  # 문자형 타이틀에서 '666' 이 나온다면 카운팅
        cnt += 1

    if cnt == N:  # 카운팅이 N만큼 나왔다면 출력하고 종료
        print(TITLE)
        break

    TITLE += 1  # 1씩 증가
