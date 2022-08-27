"""📝 팩토리얼"""
# 0이면 1, 아니라면 -1씩한 값을 곱한다.


def fac(n):
    if n == 0:  # 0이라면 1을 리턴
        return 1

    return n * fac(n - 1)  # 10 * 9(8, 7, 6, ...)


N = int(input())

print(fac(N))


# 또는

N = int(input())

answer = 1
if N > 0:
    for i in range(1, N + 1):
        answer *= i

print(answer)


"""📝 3의 배수"""
# 한 자릿수가 나올 때까지 각 자릿수를 더하는 것을 변환이라고 한다.
# 변환을 몇 번 했는지 카운팅을 하고, 변환의 마지막 값이 3의 배수인지를 확인한다.

N = input().strip()
answer = 0
while len(N) > 1:
    cnt = 0
    for i in range(len(N)):
        cnt += int(N[i])

    N = str(cnt)
    answer += 1
print(answer)

if int(N) % 3 == 0:
    print('YES')
else:
    print('NO')

# 또는


def f(n, answer):
    if len(n) > 1:
        answer += 1
        cnt = 0
        for i in n:
            cnt += int(i)
        f(str(cnt), answer)
    else:
        if int(n) % 3 == 0:
            print(answer)
            print('YES')
        else:
            print(answer)
            print('NO')


N = input()
answer = 0

f(N, answer)


"""📝 피보나치 수"""
# 0, 1부터 시작해 a와 b를 더하고, 나온 결과와 다음 수를 더하기를 n번만큼 반복한다.

N = int(input())

a, b = 0, 1
for _ in range(N):
    a, b = b, a+b

print(a)


"""📝 하노이 탑 🚨"""


def hanoi(a, b, c, n):
    if n == 1:
        print(a, c)
        return

    hanoi(a, c, b, n - 1)  # 원반을 b로 이동
    print(a, c)  # 가장 큰 원반을 c로 이동

    hanoi(b, a, c, n - 1)  # b에 있는 원반을 c로 이동


N = int(input())

print(2**N - 1)  # 하노이 탑 완성 횟수

if N <= 20:  # 20이하일 때만 실행
    hanoi(1, 2, 3, N)
