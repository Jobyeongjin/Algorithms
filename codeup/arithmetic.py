# 32.
# 입력 : 정수 1개
# 출력 : 부호 바꾸기(-)
a = int(input())

print(-a)

# 33.
# 입력 : 문자 1개
# 출력 : 그 다음 문자
x = input()
y = ord(x) + 1
z = chr(y)

print(z)

# 34.
# 입력 : 공백으로 구분된 정수 2개
# 출력 : 정수 2개 빼기
x, y = input().split()
z = int(x) - int(y)

print(z)

# 35.
# 입력 : 공백으로 구분된 실수 2개
# 출력 : 실수 2개 곱하기
x, y = input().split()
z = float(x) * float(y)

print(z)

# 36.
# 입력 : 공백으로 구분된 단어와 반복 횟수(3)
# 출력 : 횟수만큼 단어를 반복
a, b = input().split()

print(a * int(b))

# 37.
# 입력 : 반복 횟수와 문장을 줄 바꿔서
# 출력 : 문장을 횟수만큼
a = input()
b = input()

print(int(a) * b)

# 38.
# 입력 : 공백으로 구분된 정수 2개
# 출력 : 거듭제곱한 값
x, y = input().split()
z = int(x)**int(y)

print(z)

# 39.
# 입력 : 공백으로 구분된 실수 2개
# 출력 : 거듭제곱한 값
x, y = input().split()
z = float(x)**float(y)

print(z)

# 40.
# 입력 : 공백으로 구분된 정수 2개
# 출력 : 나눈 몫
x, y = input().split()
z = int(x)//int(y)

print(z)

# 41.
# 입력 : 공백으로 구분된 정수 2개
# 출력 : 나눈 나머지
x, y = input().split()
z = int(x) % int(y)

print(z)

# 42.
# 입력 : 실수 1개
# 출력 : 소수점 세 번째에서 반올림한 값
a = float(input())

print(round(a, 2))

# 43.
# 입력 : 공백으로 구분된 실수 2개
# 출력 : 나눈 결과를 소수점 네 번째에서 반올림한 값
a, b = input().split()
x = float(a)
y = float(b)

z = x / y

print('%.3f' % z)

# 44.
# 입력 : 공백으로 둔 정수 2개
# 출력 : 첫 줄에 +, 둘째 줄은 -, 셋째는 *, 넷째는 몫, 다섯째는 나머지, 여섯째는 나눈 값을 순서대로(실수는 소수점 둘째까지)
a, b = map(int, input().split())

print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(round(a / b, 2))

# 45.
# 입력 : 공백을 둔 정수 3개
# 출력 : 공백을 둔 합과 평균, 평균은 소수점 둘째까지
x, y, z = map(int, input().split())
a = x + y + z
b = (a) / 3

print(a, '%0.2f' % b)

# 46.
# 입력 : 정수 1개
# 출력 : 2배 곱한 정수
a = int(input())

print(a * 2)

# 47.
# 입력 : 공백을 둔 정수 2개(0 <= a, b <= 10)
# 출력 : a를 2b(제곱)배 만큼 곱한 값
x, y = map(int, input().split())
z = 2 ** y

print(x * z)
