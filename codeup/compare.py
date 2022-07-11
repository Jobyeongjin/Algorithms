# 48.
# 입력 : 공백을 둔 정수 2개
# 출력 : a가 b보다 작은 경우 참, 아니면 거짓
a, b = map(int, input().split())

if (a < b):
    print('True')
else:
    print('False')

# 49.
# 입력 : 공백을 둔 정수 2개
# 출력 : a와 b가 같을 경우 참, 아니면 거짓
a, b = map(int, input().split())

if (a == b):
    print('True')
else:
    print('False')

# 50.
# 입력 : 공백을 둔 정수 2개
# 출력 : b가 a보다 크거나 같은 경우 참, 아니면 거짓
a, b = map(int, input().split())

if (a <= b):
    print('True')
else:
    print('False')

# 51.
# 입력 : 공백을 둔 정수 2개
# 출력 : a와 b가 다른 경우 참, 아니면 거짓
a, b = map(int, input().split())

if (a != b):
    print('True')
else:
    print('False')
