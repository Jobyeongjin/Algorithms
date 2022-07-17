# 92. 이상한 출석 부르기 1
# 입력 : 첫 번째 줄에 출석 번호를 부른 횟수인 정수 n(1~10000)
#       두 번째 줄에는 무작위로 부른 n개의 번호(1~23)이 공백을 두고 순서대로 입력
# 출력 : 1번부터 번호가 불린 횟수를 순서대로 공백으로 구분하여 한 줄로 출력

n = int(input())
m = input().split()

for i in range(n):
    m[i] = int(m[i])

v = []
for i in range(24):
    v.append(0)

for i in range(n):
    v[m[i]] += 1

for i in range(1, 24):
    print(v[i], end=' ')


# 93. 이상한 출석 부르기 2
# 입력 : 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력,
#       n개의 랜덤 번호(k, 1 ~ 23)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력
# 출력 : 출석을 부른 번호 순서를 바꾸어 공백을 두고 출력

n = int(input())
nl = input().split()

nl.reverse()

for i in range(0, n):
    print(nl[i], end=' ')


# 94. 이상한 출석 부르기 3
# 입력 : 번호를 부른 횟수(n, 1 ~ 10000)가 첫 줄에 입력
#       n개의 랜덤 번호(k)가 두 번째 줄에 공백을 사이에 두고 순서대로 입력
# 출력 : 출석을 부른 번호 중에 가장 빠른 번호를 출력

n = int(input())
nl = map(int, input().split())

a = min(nl)
print(a)


# 95. 바둑판에 흰 돌 놓기
# 입력 : 바둑판에 올려 놓을 흰 돌의 개수(n)가 첫 줄에 입력
#       둘째 줄 부터 n+1 번째 줄까지 힌 돌을 놓을 좌표(x, y)가 n줄 입력
#       n은 10이하의 자연수이고 x, y 좌표는 1 ~ 19 까지이며, 똑같은 좌표는 입력되지 않음
# 출력 : 흰 돌이 올려진 바둑판의 상황을 출력
#       흰 돌이 있는 위치는 1, 없는 곳은 0으로 출력

d = []

for i in range(20):
    d.append([])
    for j in range(20):
        d[i].append(0)

n = int(input())
for i in range(n):
    x, y = input().split()
    d[int(x)][int(y)] = 1

for i in range(1, 20):
    for j in range(1, 20):
        print(d[i][j], end=' ')

    print()


# 95. 바둑알 십자 뒤집기
# 입력 : 바둑알이 깔려 있는 상황이 19 * 19 크기의 정수값으로 입력
#       십자 뒤집기 횟수(n)가 입력
#       십자 뒤집기 좌표가 횟수(n) 만큼 입력된다. 단, n은 10이하의 자연수
# 출력 : 십자 뒤집기를 출력
