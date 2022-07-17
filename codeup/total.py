# 77.
# 입력 : 정수(0~100) 1개
# 출력 : 짝수의 합
n = int(input())
result = 0

for i in range(n + 1):
    if i % 2 == 0:
        result += i

print(result)


# 78.
# 입력 : 문자들이 1개씩 계속해서
# 출력 : 영문 소문자 'p'가 입력될 때까지 문자 출력
while True:
    a = input()
    print(a)
    if a == 'q':
        break


# 79.
# 입력 : 정수(50) 1개
# 출력 : 순서대로 더해 합을 만들다가, 입력된 정수와 같거나 커졌을 때 마지막에 더한 정수
n = int(input())
a = 0

for i in range(50):
    a = a + i

    if a >= n:
        print(i)
        break


# 80.
# 입력 : 서로 다른 주사위 2개의 면의 개수 n, m(10이하의 자연수)이 공백을 두고
# 출력 : 나올 수 있는 주사위의 숫자를 한 세트씩 줄을 바꿔서, 1부터 오름차순으로
a, b = map(int, input().split())

for x in range(1, a + 1):
    for y in range(1, b + 1):
        print(x, y)


# 81.
# 입력 : 16진수로 한 자리 수 단, A~F 까지만
# 출력 : 입력된 16진수에 1~F까지 순서대로 곱한 16진수 구구단을 줄 바꿔서
a = int(input(), 16)

for i in range(1, 16):
    print('%X*%X=%X' % (a, i, a*i))


# 82.
# 입력 : 30보다 작은 정수(1~29) 1개
# 출력 : 1부터 순서대로 공백을 둔 수, 3 또는 6 또는 9가 포함되는 경우 그 수 대신 대문자 X로
a = int(input())

for i in range(1, a+1):
    if (i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
        print('X', end=' ')
    else:
        print(i, end=' ')


# 83.
# 입력 : 공백을 둔 빨녹파(r,g,b) 각 빛의 가짓수
# 출력 : rgb 색의 정보를 오름차순으로 줄 바꿔서, 마지막에 그 개수를 출력
r, g, b = map(int, input().split())
a = 0

for x in range(r):
    for y in range(g):
        for z in range(b):
            print('%d %d %d' % (x, y, z))

            a = a + 1

print(a)


# 84.
# 입력 : h, b, c, s 공백을 두고, h 48,000이하, b 32이하, c 5이하, s 6,000이하의 자연수
# 출력 : 필요한 저장 공간을 MB 단위로 바꿔서 단, 소수점 첫째 자리까지, MB는 공백을 두고 출력
h, b, c, s = map(int, input().split())
total = h * b * c * s

a = total/8/1024/1024

print('%.1f MB' % a)


# 85.
# 입력 : w,h,b 공백을 두고 단, w,h는 정수(1~1024) b는 40이하의 4의 배수
# 출력 : 필요한 저장 공간을 MB 단위로 바꿔서 단, 소수점 셋째 자리에서 반올림해 둘째 자리까지
w, h, b = map(int, input().split())
total = w * h * b

a = total/8/1024/1024

print('%.2f MB' % a)


# 86.
# 입력 : 언제까지 합을 계산할지, 정수 1개
# 출력 : 순서대로 계속 더하다가 그 합이 정수보다 커지거나 같은 경우까지의 합
a = int(input())
result = 0
i = 1

while result < a:
    result = result + i
    i = i + 1

print(result)


# 87.
# 입력 : 정수(1~100) 1개
# 출력 : 1부터 입력한 정수보다 작거나 같을 때까지 1씩 증가, 3의 배수는 뺴기
a = int(input())

for i in range(1, a+1):
    if i % 3 == 0:
        continue
    print(i, end=' ')


# 88. 수 나열하기
# 입력 : 시작 값(a), 등차 값(d), 몇 번째 수 인지를 의미하는 정수(n), 공백을 두고 입력
# 출력 : n번째 수
a, d, n = map(int, input().split())
x = a

for i in range(2, n+1):
    x += d

print(x)


# 89. 수 나열하기
# 입력 : 시작 값(a), 등비 값(r), 몇 번째 인지를 의미하는 정수(n), 공백을 두고(모두 0~10)
# 출력 : n번째 수
a, r, n = map(int, input().split())

for i in range(1, n):
    a = a * r

print(a)


# 90. 수 나열하기
# 입력 : 시작 값(a), 곱할 값(m), 더할 값(d), 몇 번째 인지를 나타내는 정수(n), 공백을 두고(a, m, d는 -50~ 50, n은 10d이하 자연수)
# 출력 : n번째 수
a, m, d, n = map(int, input().split())

for i in range(1, n):
    a = a * m+d

print(a)


# 91. 함께 문제 푸는 날
# 입력 : 같은 날 동시에 가입한 인원 3명이 규칙적으로 방문하는 방문 주기가 공백을 두고 입력 단, 입력값 100이하
# 출력 : 3명이 다시 모두 함께 방문해 문제를 풀어보는 날
a, b, c = map(int, input().split())

x = 0
while True:
    x = x + 1
    if x % a == 0 and x % b == 0 and x % c == 0:
        print(x)
        break
