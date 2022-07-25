# 1. 거꾸로 출력해 보아요 (1545)

n = int(input())

for i in range(n + 1):
    print(n - i, end=' ')


# 2. 간단한 N의 약수 (1933)

n = int(input())

for i in range(1, n + 1):
    # 약수란, 나눴을 때 0이 나오는 수
    if n % i == 0:
        print(i, end=' ')


# 3. 1대1 가위바위보 (1936)

a, b = map(int, input().split())

if a > b:
    print('A')
else:
    print('B')


# 4. 아주 간단한 계산기 (1938)

a, b = map(int, input().split())

print(a+b, a-b, a*b, a/b, end='\n')


# 5. 더블더블 (2019)

n = int(input())

for i in range(n + 1):
    # 2의0제곱(=1) 2 4 8 16 32 64 128 256 💡
    print(2 ** i, end=' ')


# 6. N줄덧셈 (2025)

n = int(input())

result = 0

for i in range(1, n + 1):
    result += i

print(result)


# 7. 대각선 출력하기 (2027)

print('#++++')
print('+#+++')
print('++#++')
print('+++#+')
print('++++#')


# 8. 몫과 나머지 출력하기 (2029)

t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())

    print(f'#{tc} {a // b} {a % b}')


# 9. 서랍의 비밀번호 (2043)

p, k = map(int, input().split())

cnt = 0

for i in range(k, p + 1):
    cnt += 1

print(cnt)


# 10. 스탬프 찍기 (2046)

n = int(input())

for i in range(1, n + 1):
    print('#')
