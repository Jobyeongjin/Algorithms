# 20. 각 자릿수의 합 구하기
# 입력 : 정수 number(123)가 주어질 때, 각 자릿수의 합을 구해서 출력
# 출력 : 6

n = input()

# 문자열 그대로 리스트에 추가
a = []

for i in n:
    a += i

# 문자 리스트를 숫자로 바꾸기
result = map(int, a)
# sum 함수 사용
print(sum(result))

# 또는
n = int(input())

result = 0

while n:
    result += n % 10
    n //= 10

print(result)

# 또는
n = int(input())

result = 0

while n:
    n, r = divmod(n, 10)
    result += r

print(result)


# 21. 숫자 뒤집기
# 입력 : 주어진 숫자(1234)를 뒤집은 결과를 출력 / 문자열이 아닌 숫자로 활용
# 출력 : 4321

n = int(input())

result = 0

while n > 0:
    # 10으로 나눈 나머지 즉, 마지막 수
    a = n % 10
    # 결과값 뒤에 10을 곱해서 마지막 수(a) 추가 / 10을 곱해서 마지막 자리를 비워 넣기 위함
    result = result * 10 + a
    # 몫을 구해서 반환
    n = n // 10

print(result)

# 문자열을 쓴다면
n = input()

print(int(str(n)[::-1]))

# 또는
n = int(input())

result = 0

while n:
    # 결과값에 10을 곱한 값을 넣어주면서 마지막 자리 비우기
    result *= 10
    # 10을 나눈 나머지를 더하기
    result += n % 10
    # 몫을 구해서 반환
    n //= 10

print(result)
