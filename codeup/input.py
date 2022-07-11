# 9.
# 입력 : a
# 출력 : a
a = input()  # 사용자가 어떤 값을 입력하게 하고, 그 값을 변수에 문자열(str)로 저장

print(a)

# 10.
# 입력 : 정수 1개
# 출력 : 입력된 수를 정수로 변환
a = input()
b = int(a)

print(b)


# 11.
# 입력 : 실수 1개
# 출력 : 입력된 수를 실수로 변환
a = input()
b = float(a)

print(b)

# 12.
# 입력 : 정수 2개
# 출력 : 입력된 두 정수의 줄을 바꾸기
a = input()
b = input()

print(a)
print(b)

# 13.
# 입력 : 문자 2개
# 출력 : 순서를 바꿔 한 줄에 한 문자씩
a = input()
b = input()

print(b)
print(a)

# 14.
# 입력 : 실수 1개
# 출력 : 입력받은 실수의 줄을 바꾸고 3번
a = input()

print(a)
print(a)
print(a)

# 15.
# 입력 : 공백으로 구분된 정수 2개
# 출력 : 입력된 두 정수의 줄 바꾸기
a, b = input().split()  # 문자열을 공백을 기준으로 나눔

print(a)
print(b)

# 16.
# 입력 : 공백으로 구분된 문자 2개
# 출력 : 2개의 문자의 순서 바꾸기

a, b = input().split()

print(b, a)

# 17.
# 입력 데이터 1개
# 출력 : 공백을 두고 3번 출력
a = input()

print(a, a, a)

# 18.
# 입력 : 시:분
# 출력 : 입력받은 시간 형식과 똑같은 형태
a, b = input().split(':')  # split 안에 특정 값을 넣으면 그것을 기준으로 나눔

print(a, b, sep=':')  # 공백이 아닌 해당 값을 추가

# 19.
# 입력 : 연도, 월, 일이 . 으로 구분
# 출력 : - 구분기호로 사용해서 일-월-연도로 바꾸기
x, y, z = input().split('.')

print(z, y, x, sep='-')

# 20.
# 입력 : 주민번호 앞 6자리와 뒷 7자리가 - 구분
# 출력 : - 를 제외한 주민번호 13자리 모두 붙이기
a, b = input().split('-')

print(a, b, sep='')  # 공백 제거

# 21.
# 입력 : 문자 5개로 이뤄진 단어 1개
# 출력 : 각 문자를 한 줄에 한 문자씩 줄 바꾸기
a = input()

print(a[0])
print(a[1])
print(a[2])
print(a[3])
print(a[4])

# 22.
# 입력 : 6자리 숫자로 이뤄진 연월일(YYMMDD)
# 출력 : 년도 월 일을 공백으로 구분해 한 줄로
a = input()

print(a[0:2], a[2:4], a[4:6])

# 23.
# 입력 : 시:분:초
# 출력 : 분
x, y, z = input().split(':')

print(y)

# 24.
# 입력 : 알파벳과 숫자로 이뤄진 단어 2개가 공백으로 구분
# 출력 : 단어 2개를 순서대로 붙이기
a, b = input().split()

print(a + b)
