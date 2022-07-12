# 65.
# 입력 : 공백을 둔 정수 3개
# 출력 : 짝수만 순서대로 줄 바꿔서
a, b, c = map(int, input().split())

if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

# 66.
# 입력 : 공백을 둔 정수 3개
# 출력 : 입력된 순서대로 짝/홀을 줄 바꿔서
a, b, c = map(int, input().split())

if a % 2 == 0:
    print('even')
else:
    print('odd')
if b % 2 == 0:
    print('even')
else:
    print('odd')
if c % 2 == 0:
    print('even')
else:
    print('odd')

# 67.
# 입력 : 정수 1개
# 출력 : A = 음수+짝수, B = 음수+홀수, C = 양수+짝수, D = 양수+홀수
a = int(input())

if a < 0:
    if a % 2 == 0:
        print('A')
    else:
        print('B')
else:
    if a % 2 == 0:
        print('C')
    else:
        print('D')

# 68.
# 입력 : 정수(0~100) 1개
# 출력 : 평가 점수, A = 90~100, B = 70~89, C = 40~69, D = 0~39
a = int(input())

if a >= 90:
    print('A')
elif a >= 70:
    print('B')
elif a >= 40:
    print('C')
else:
    print('D')

# 69.
# 입력 : 영문자(A, B, C, D, 나머지) 1개
# 출력 : 문자에 따라 다른 내용
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
# 입력 : 월을 의미하는 정수(1 ~ 12) 1개
# 출력 : 계절 이름
a = int(input())

if a == 12 or a == 1 or a == 2:
    print('winter')
elif a == 3 or a == 4 or a == 5:
    print('spring')
elif a == 6
