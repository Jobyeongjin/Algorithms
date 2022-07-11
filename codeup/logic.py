# 52.
# 입력 : 정수 1개
# 출력 : 값이 0이면 거짓, 아니면 참

a = int(input())

if (a == 0):
    print('False')
else:
    print('True')

# 53.
# 입력 : 정수 1개
# 출력 : 불 값이 거짓이면 참, 참이면 거짓
a = bool(int(input()))

if (a == True):
    print('False')
else:
    print('True')

# 54.
# 입력 : 공백을 둔 정수 2개
# 출력 : 둘 다 참이어야 참, 아니면 거짓
a, b = map(int, input().split())

if (a and b == True):
    print('True')
else:
    print('False')

# 55.
# 입력 : 공백을 둔 정수 2개
# 출력 : 하나라도 참이면 참, 아니면 거짓
a, b = map(int, input().split())

if (a or b == True):
    print('True')
else:
    print('False')

# 56.
# 입력 : 공백을 둔 정수 2개
# 출력 : 참/거짓 값이 서로 다른 경우만 참, 아니면 거짓
a, b = map(int, input().split())

if (a ^ b == True):
    print('True')
else:
    print('False')

# 57.
# 입력 : 공백을 둔 정수 2개
# 출력 : 참/거짓 값이 서로 같은 경우만 참, 아니면 거짓
a, b = map(int, input().split())

if (bool(a) ^ bool(b) == True):
    print('False')
else:
    print('True')

# 58.
# 입력 : 공백을 둔 정수 2개
# 출력 : 참/거짓 값이 모두 거짓일 때만 참, 아니면 거짓
a, b = map(int, input().split())

if (a == False and b == False):
    print('True')
else:
    print('False')

# 59.
# 입력 : 비트단위 정수 1개
# 출력 : 비트 단위로 1 > 0, 0 > 1 로 바꾼 후 10진수로
a = int(input())

print(~a)

# 60.
# 입력 : 공백을 둔 정수 2개
# 출력 : 비트단위로 and 계산을 한 두 정수 값을 10진수로
a, b = map(int, input().split())

print(a & b)

# 61.
# 입력 : 공백을 둔 정수 2개
# 출력 : 비트단위로 or 계산을 한 두 정수 값을 10진수로
a, b = map(int, input().split())

print(a | b)

# 62.
# 입력 : 공백을 둔 정수 2개
# 출력 : 비트단위로 xor 계산을 한 두 정수 값을 10진수로
a, b = map(int, input().split())

print(a ^ b)

# 63.
# 입력 : 공백을 둔 정수 2개
# 출력 : 두 정수 중 큰 값을 10진수로
a, b = map(int, input().split())

if (a > b):
    print(a)
else:
    print(b)

# 64.
# 입력 : 공백을 둔 정수 3개
# 출력 : 가장 작은 값
a, b, c = map(int, input().split())

print(min(a, b, c))
