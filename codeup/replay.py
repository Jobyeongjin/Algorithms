# 출력 🐳


# 1.
print('Hello')


# 2.
print('Hello World')


# 3.
print('Hello\nWorld')


# 4.
print('\'Hello\'')


# 5.
print('"Hello World"')


# 6.
print('\"!@#$%^&*()\'')


# 7.
print('\"C:\\Download\\\'hello\'.py\"')


# 8.
print('print(\"Hello\\nWorld\")')


# 입출력 🐳 --------------------


# 9.
print(input())


# 10.
print(int(input()))


# 11.
print(float(input()))


# 12.
a = int(input())
b = int(input())

print(a, b)


# 13.
a = input()
b = input()

print(b, a, end='\n')


# 14.
n = float(input())

print(n, n, n, sep='\n')


# 15.
a, b = map(int, input().split())

print(a, b, end='\n')


# 16.
a, b = input().split()

print(b, a)


# 17.
a = input()

print(a, a, a)


# 18.
h, m = input().split(':')

print(h, m, sep=':')


# 19.
y, m, d = input().split('.')

print(d, m, y, sep='-')


# 20.
n, m = input().split('-')

print(n + m)


# 21.
a = input()

for i in a:
    print(i)


# 22.
a = input()

print(a[0:2], a[2:4], a[4:6])


# 23.
a = input().split(':')

print(a[1])


# 24.
a, b = input().split()

print(a + b)


# 값 변환 🐳 --------------------


# 25.
a, b = map(int, input().split())

print(a + b)


# 26.
n = float(input())
m = float(input())

print(n + m)


# 산술 연산 🐳 --------------------


# 32.
n = int(input())

print(-n)


# 33.
print(chr(ord(input()) + 1))


# 34.
n, m = map(int, input().split())

print(n - m)


# 35.
n, m = map(float, input().split())

print(n * m)


# 36.
n, m = input().split()

print(n * int(m))


# 37.
n = int(input())
m = input()

print(n * m)


# 38.
n, m = map(int, input().split())

print(n ** m)


# 39.
n, m = map(float, input().split())

print(n ** m)


# 40.
n, m = map(int, input().split())

print(n // m)


# 41.
n, m = map(int, input().split())

print(n % m)


# 42.
n = float(input())

print(round(n, 2))


# 43.
n, m = map(float, input().split())

z = n / m
print('%.3f' % z)


# 44.
n, m = map(int, input().split())

print(n + m)
print(n - m)
print(n * m)
print(n // m)
print(n % m)
print(round(n / m, 2))


# 45.
x, y, z = map(int, input().split())
a = x + y + z
b = (a) / 3

print(a, '%0.2f' % b)


# 46.
n = int(input())

print(n << 1)


# 47.
n, m = map(int, input().split())

print(n << m)


# 비교 연산 🐳 --------------------


# 48.
n, m = map(int, input().split())

if n < m:
    print('True')
else:
    print('False')


# 49.
n, m = map(int, input().split())

if n == m:
    print('True')
else:
    print('False')


# 50.
n, m = map(int, input().split())

if n <= m:
    print('True')
else:
    print('False')


# 51.
a, b = map(int, input().split())

if (a != b):
    print('True')
else:
    print('False')


# 논리 연산 🐳 --------------------


# 52.
n = int(input())

if n == 0:
    print('False')
else:
    print('True')


# 53.
n = int(input())

if n == False:
    print('True')
else:
    print('False')


# 54.
n, m = map(int, input().split())

if n and m == True:
    print('True')
else:
    print('False')


# 55.
n, m = map(int, input().split())

if n or m == True:
    print('True')
else:
    print('False')


# 56.
n, m = map(int, input().split())

if n != m:
    print('True')
else:
    print('False')


# 57.
n, m = map(int, input().split())

if n == m:
    print('True')
else:
    print('False')


# 58.
a, b = map(int, input().split())

if a == False and b == False:
    print('True')
else:
    print('False')


# 59.
n = int(input())

print(~n)


# 60.
a, b = map(int, input().split())

print(a & b)


# 61.
a, b = map(int, input().split())

print(a | b)


# 62.
a, b = map(int, input().split())

print(a ^ b)


# 63.
n, m = map(int, input().split())

if n < m:
    print(m)
else:
    print(n)


# 64.
a, b, c = map(int, input().split())

print(min(a, b, c))

# 선택 구조 🐳 --------------------


# 65.
n = list(map(int, input().split()))

for i in n:
    if i % 2 == 0:
        print(i)


# 66.
n = list(map(int, input().split()))

for i in n:
    if i % 2 == 0:
        print('even')
    else:
        print('odd')


# 67.
n = int(input())

if n < 0:
    if n % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if n % 2 == 0:
        print('C')
    else:
        print('D')


# 68.
n = int(input())

if n >= 90:
    print('A')
elif n >= 70:
    print('B')
elif n >= 40:
    print('C')
else:
    print('D')


# 69.
a = input()

if a == 'A':
    print('best!!!')
elif a == 'B':
    print('good!!')
elif a == 'C':
    print('run!')
elif a == 'D':
    print('slowly~')
else:
    print('what?')


# 70.
n = int(input())

dic = {
    12: 'winter',
    1: 'winter',
    2: 'winter',
    3: 'spring',
    4: 'spring',
    5: 'spring',
    6: 'summer',
    7: 'summer',
    8: 'summer',
    9: 'fall',
    10: 'fall',
    11: 'fall',
}

for i in dic:
    if i == n:
        print(dic[i])


# 반복 구조 🐳 --------------------


# 71.
while True:
    n = int(input())

    if n == 0:
        break
    print(n)


# 72.
n = int(input())

while True:
    print(n)
    n -= 1
    if n == 0:
        break


# 73.
n = int(input())

while True:
    n -= 1
    if n < 0:
        break
    print(n)


# 74.
alpha = ord(input())
n = ord('a')

while n <= alpha:
    print(chr(n), end=' ')
    n += 1


# 75.
n = int(input())

cnt = 0
while cnt <= n:
    print(cnt)
    cnt += 1


# 76.
a = int(input())

for i in range(a + 1):
    print(i)


# 기초 종합 🐳 --------------------


# 77.
n = int(input())

result = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        result += i

print(result)


# 78.
while True:
    alpha = input()

    print(alpha)
    if alpha == 'q':
        break


# 79.
n = int(input())

result = 0
for i in range(n):
    result += i
    if result >= n:
        print(i)
        break


# 80.
n, m = map(int, input().split())

for i in range(1, n + 1):
    for j in range(1, m + 1):
        print(i, j)


# 81.
a = int(input(), 16)

for i in range(1, 16):
    print('%X*%X=%X' % (a, i, a*i))


# 82.
n = int(input())

for i in range(1, n + 1):
    if i % 10 == 3 or i % 10 == 6 or i % 10 == 9:
        print('X', end=' ')
    else:
        print(i, end=' ')


# 83.
r, g, b = map(int, input().split())

cnt = 0
for i in range(r):
    for j in range(g):
        for l in range(b):
            cnt += 1
            print(i, j, l)
print(cnt)


# 84.
h, b, c, s = map(int, input().split())

total = h * b * c * s
division = total / 8 / 1024 / 1024
result = round(division, 1)
print(f'{result} MB')


# 85.
w, h, b = map(int, input().split())

total = w * h * b
division = total / 8 / 1024 / 1024

print('%.2f MB' % division)


# 86.
a = int(input())
result = 0
i = 1

while result < a:
    result = result + i
    i = i + 1

print(result)


# 87.
n = int(input())

for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    else:
        print(i, end=' ')


# 88.
a, d, n = map(int, input().split())

for i in range(n - 1):
    a += d

print(a)


# 89.
a, d, n = map(int, input().split())

for i in range(n - 1):
    a *= d

print(a)


# 90.
a, m, d, n = map(int, input().split())

for i in range(n - 1):
    a *= m
    a += d
    # a = a * m + d

print(a)


# 91.
a, b, c = map(int, input().split())

day = 0
while True:
    day += 1
    if day % a == 0 and day % b == 0 and day % c == 0:
        print(day)
        break
