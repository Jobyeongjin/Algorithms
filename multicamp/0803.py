# 성 지키기 🐳
# 문제 : 모든 행과 열에 경비원 배치하기, 최소로 배치해야 하는 경비원의 수는?

import sys
n, m = map(int, input().split())

matrix = [list(input()) for _ in range(n)]  # 이차원 리스트 생성

row = [0] * n  # 행렬 리스트
col = [0] * m

for x in range(n):  # 이중 for문으로 전부 확인
    for y in range(m):
        if matrix[x][y] == 'X':  # 좌표값이 'X' 라면 행렬 리스트를 1로 변경
            row[x] = 1
            col[y] = 1

cnt_row = 0
cnt_col = 0

# 비어있는 행렬 찾기 (0)
for i in row:
    if i == 0:
        cnt_row += 1

for i in col:
    if i == 0:
        cnt_col += 1

print(max(cnt_row, cnt_col))  # 최소 경비원의 수


# 유니크 🐳
# 문제 : 자신과 같은 수를 쓴 사람이 없으면 점수를 얻고, 겹치면 점수를 얻을 수 없다.
#       3번의 게임에서 얻은 총 점수 구하기

n = int(input())

one = []  # 게임 점수 리스트
two = []
three = []

for _ in range(n):
    a, b, c = map(int, input().split())
    one.append(a)
    two.append(b)
    three.append(c)

for i in range(n):
    total = 0
    if one.count(one[i]) == 1:  # 게임 점수 리스트에서 i 요소가 1개 있는지 확인
        total += one[i]  # 해당 점수 더하기
    if two.count(two[i]) == 1:
        total += two[i]
    if three.count(three[i]) == 1:
        total += three[i]

    print(total)  # 각각의 플레이어 점수


# 2차원 배열의 합 🐳
# 문제 : 2차원 배열에 저장되어 있는 수의 합 구하기

input = sys.stdin.readline

n, m = map(int, input().split())

stack = [[0] * m] + [list(map(int, input().split())) for _ in range(n)]

for _ in range(int(input())):
    hap = 0
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2 + 1):
        for j in range(y1 - 1, y2):
            if x1 - 1 <= i <= x2 and y1 - 1 <= j <= y2:
                hap += stack[i][j]

    print(hap)


# 하얀 칸 🐳
# 문제 : 체스판의 상태가 주어졌을 때, 하얀 칸 위에 말이 몇 개 있는지 구하기
#      첫째 줄부터 8개의 줄에 체스판의 상태가 주어진다. ‘.’은 빈 칸이고, ‘F’는 위에 말이 있는 칸이다.
#      검정 칸과 하얀 칸이 번갈아가면서 색칠되어 있다. 가장 왼쪽 위칸 (0,0)은 하얀색이다.

chess = [list(input()) for _ in range(8)]

cnt = 0
for x in range(8):
    for y in range(8):
        # 좌표 값을 더하면 짝수, 해당 좌표값이 'F' 라면 1씩 카운팅
        if (x + y) % 2 == 0 and chess[x][y] == 'F':
            cnt += 1

print(cnt)


# 5와 6의 차이 🐳
# 문제 : 두 수 A와 B가 주어졌을 때, 상근이는 이 두 수를 더하려고 한다.
#       이때, 상근이가 구할 수 있는 두 수의 가능한 합 중, 최솟값과 최댓값을 구해 출력하는 프로그램을 작성하시오.
#       상근이가 숫자 5를 볼 때, 5로 볼 때도 있지만, 6으로 잘못 볼 수도 있고, 6을 볼 때는, 6으로 볼 때도 있지만, 5로 잘못 볼 수도 있다.

a, b = input().split()

x = int(a.replace('6', '5')) + int(b.replace('6', '5'))
y = int(a.replace('5', '6')) + int(b.replace('5', '6'))

print(x, y)


# 상금 헌터 🐳
# 문제 : 순위에 맞게 상금 가져오기

award_2017 = {
    '1': 5000000,
    '2': 3000000,
    '3': 3000000,
    '4': 2000000,
    '5': 2000000,
    '6': 2000000,
    '7': 500000,
    '8': 500000,
    '9': 500000,
    '10': 500000,
    '11': 300000,
    '12': 300000,
    '13': 300000,
    '14': 300000,
    '15': 300000,
    '16': 100000,
    '17': 100000,
    '18': 100000,
    '19': 100000,
    '20': 100000,
    '21': 100000
}

award_2018 = {
    '1': 5120000,
    '2': 2560000,
    '3': 2560000,
    '4': 1280000,
    '5': 1280000,
    '6': 1280000,
    '7': 1280000,
    '8': 640000,
    '9': 640000,
    '10': 640000,
    '11': 640000,
    '12': 640000,
    '13': 640000,
    '14': 640000,
    '15': 640000,
    '16': 320000,
    '17': 320000,
    '18': 320000,
    '19': 320000,
    '20': 320000,
    '21': 320000,
    '22': 320000,
    '23': 320000,
    '24': 320000,
    '25': 320000,
    '26': 320000,
    '27': 320000,
    '28': 320000,
    '29': 320000,
    '30': 320000,
    '31': 320000,
}

n = int(input())

for _ in range(n):
    a, b = input().split()

    price = 0
    for i in award_2017:
        if i == a:
            price += award_2017[i]

    for i in award_2018:
        if i == b:
            price += award_2018[i]

    print(price)
