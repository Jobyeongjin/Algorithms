# 1. 손익분기점 🐳
# 문제 : A, B, C가 주어졌을 때, 손익분기점을 구하는 프로그램을 작성하시오.
#       A = 고정비용, B = 가변비용, C = 노트북 가격

a, b, c = map(int, input().split())

margin = c - b  # 순이익
if b >= c:  # 노마진이면 -1
    print('-1')
else:
    print(a // margin + 1)  # 손익분기는 순이익에서 고정비용을 뺀 값에 1대를 더 팔아야 함


# 2. 벌집 🐳
# 문제 : 숫자 N이 주어졌을 때, 벌집의 중앙 1에서 N번 방까지 최소 개수의 방을 지나서 갈 때 몇 개의 방을 지나가는지(시작과 끝을 포함하여)를 계산하는 프로그램을 작성하시오. 예를 들면, 13까지는 3개, 58까지는 5개를 지난다.

n = int(input())

house = 1  # 방 1부터 시작
cnt = 1  # 지나는 방의 개수
while n > house:
    house += 6 * cnt  # 6의 배수로 방(둘레) 개수 증가
    cnt += 1  # 카운팅

print(cnt)


# 3. 분수찾기 🐳🚨
# 문제 : 이와 같이 나열된 분수들을 1/1 → 1/2 → 2/1 → 3/1 → 2/2 → … 과 같은 지그재그 순서로 차례대로 1번, 2번, 3번, 4번, 5번, … 분수라고 하자.
#       X가 주어졌을 때, X번째 분수를 구하는 프로그램을 작성하시오.

n = int(input())

line = 1
while n > line:
    n -= line  # 라인 안에 위치 확인
    line += 1  # 몇 번째 라인인지

if line % 2 == 0:  # 짝수 라인이라면 분자는 위치 값 그대로 사용
    up = n
    down = line - n + 1
else:  # 홀수 라인은 분모를 위치 값 그대로 사용
    up = line - n + 1
    down = n

print(f'{up}/{down}')


# 4. 달팽이는 올라가고 싶다 🐳

a, b, v = map(int, input().split())

goal = v - b  # 올라가야 하는 높이
going = a - b  # 하루에 올라가는 높이
if goal % going == 0:
    print(goal // going)
else:
    print(goal // going + 1)

# 시간초과 코드 😱
# a, b, v = map(int, input().split())

# day = 0
# height = 0
# while True:
#     day += 1
#     if a * day - b * (day - 1) >= v:
#         break

# print(day)
