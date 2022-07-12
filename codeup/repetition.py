# 71.
# 입력 : 임의의 정수가 계속 줄 바꿔서
# 출력 : 줄 바꿔 하나씩, 0이 되면 종료
from re import I


while True:
    a = int(input())

    if a == 0:
        break

    print(a)

# 72.
# 입력 : 정수(1~100) 1개
# 출력 : 1씩 줄이면서 한 줄씩 카운트다운
a = int(input())

while True:
    print(a)
    a = a - 1
    if a == 0:
        break

# 73.
# 입력 : 정수(1~100) 1개
# 출력 : 1씩 줄이면서 0이 될 때까지
a = int(input())

while True:
    a = a - 1
    print(a)
    if a == 0:
        break

# 74.
# 입력 : 영문자(a~z) 1개
# 출력 : a부터 순서대로 공백을 두고 한 줄로
x = ord(input())  # ord = 입력받은 알파벳을 유니코드 숫자로 변환
a = ord('a')  # a 부터 시작

while a <= x:
    print(chr(a), end=' ')  # chr = 유니코드 숫자를 다시 문자로 변환, end = 한 줄로 출력하기
    a += 1

# 75.
# 입력 : 정수(1~100) 1개
# 출력 : 0부터 줄 바꿔서 한 개씩
a = int(input())

i = 0
while i <= a:
    print(i)
    i += 1

# 76.
# 입력 : 정수(1~100) 1개
# 출력 : 0부터 줄 바꿔서 한 개씩
a = int(input())

for i in range(a + 1):
    print(i)
