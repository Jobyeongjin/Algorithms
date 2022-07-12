# 1.
# 입력 : n 이 3의 배수이면서 짝수인 경우 참, 아니면 거짓
# 출력 : 거짓
n = 267

if n % 3 == 0 and n % 2 == 0:  # % 나누고 나머지, == 0 >> 배수 찾기
    print('참')
else:
    print('거짓')

# 2.
# 입력 : 문자열 word('happy!') 의 길이
# 출력 : 6
word = 'happy!'
a = 0

for i in word:
    a += 1  # a 는 +1

print(a)

# 3.
# 입력 : 1부터 n(10)까지의 합, while문, for문 각각 활용
# 출력 : 55
a = 0
result = 0
n = 10

while a < n:
    a += 1
    result += a

print(result)

# 또는
for a in range(n):  # 0부터 9까지 숫자 생성
    a += 1  # a는 1을 더한 값
    result += a  # result 값에 a 를 더하기

print(result)


# 4.
# 입력 : 1부터 n(5)까지의 곱
# 출력 : 120
a = 0
result = 1  # 결과는 1부터 곱하기
n = 5

while a < n:
    a += 1
    result *= a

print(result)
# 또는
for i in range(n):
    a += 1
    result *= a

print(result)

# 5.
# 입력 : 평균 구하기
# 출력 : 11
numbers = [3, 10, 20]
a = 0
result = 0

for i in numbers:
    result += i
    a += 1

print(int(result / a))

# 6.
# 입력 : 최대값 구하기
# 출력 : 100
numbers = [0, 20, 100]
a = numbers[0]  # 리스트 안에 값으로 0번째 값으로 시작

for i in numbers:
    if i > a:
        a = i

print(a)

# 7.
# 입력 : 최소값 구하기
# 출력 : 0
numbers = [0, 20, 100]
a = numbers[0]

for i in numbers:
    if i < a:
        a = i

print(a)

# 8.
# 입력 : 두 번째로 큰 값 구하기
# 출력 : 20
numbers = [0, 20, 100]
a = numbers[0]

for i in numbers:
    if i > a:
        a = i

numbers.remove(a)  # 구한 값 삭제

for i in numbers:  # 삭제한 상태에서 다시 반복
    if i > a:
        a = i

print(a)

# 또는
numbers = [0, 20, 100]
numbers.sort()  # 오름차순으로 정렬

print(numbers[-2])  # 끝에서 두 번째 값 가져오기

# 또는
numbers = [0, 20, 100, 40]
a = numbers[0]
result = numbers[0]

for i in numbers:
    if i > a:  # 만약 값이 a보다 크다면 i 값은 a 로 (최대값)
        a = i
    elif result < i < a:  # 최대값이 아닌 값들 중에서 a보다 작고 결과값보다는 크다면
        result = i  # 그 값을 다시 결과값으로

print(result)
