# 1. 구구단
# 입력 : 첫째 줄에 N, N은 1보다 크거나 같고, 9보다 작거나 같음
# 출력 : 출력형식과 같게 N*1부터 N*9까지 출력

import sys  # 4번 문제

n = int(input())

# range를 활용하여 1부터 9까지 숫자 생성
for i in range(1, 10):
    # print(f'{n} * {i} = {n * i}')와 동일
    print(n, '*', i, '=', n*i)


# 2. A+B-3
# 입력 : 각 테스트 케이스는 한 줄, 각 줄에 A와 B가 주어짐 (0 < A, B < 10)
# 출력 : 각 테스트 케이스마다 A+B를 출력

t = int(input())

# 한 줄로 받은 t를 반복문을 돌려서
for i in range(t):
    # 각 줄의 a, b 생성
    # a, b는 따로 인자를 받아 더할 것이기 때문에 map()과 split() 함수 사용
    a, b = map(int, input().split())
    print(a + b)


# 3. 합
# 입력 : 첫째 줄에 n (1 ≤ n ≤ 10,000)
# 출력 : 1부터 n까지 합

n = int(input())
result = 0

# 1부터 시작하는 n
for i in range(1 + n):
    # 결과 값에 i를 더하기
    # result = result + i와 동일
    result += i

print(result)


# 4. 빠른 A+B
# 입력 : 첫 줄에 테스트케이스의 개수 T (최대 1,000,000), 다음 T줄에는 각각 두 정수 A와 B (A와 B는 1 이상, 1,000 이하)
# 출력 : 각 테스트케이스마다 A+B를 한 줄에 하나씩 순서대로 출력


t = int(input())

for i in range(t):
    # input() 대신 sys.stdin.readline() 함수 사용
    # sys 모듈을 불러온 것은 맨 상단에 위치
    a, b = map(int, sys.stdin.readline().split())
    print(a + b)


# 5. N 찍기
# 입력 : 첫째 줄에 100,000보다 작거나 같은 자연수 N
# 출력 : 첫째 줄부터 N번째 줄 까지 차례대로 출력

n = int(input())

# n만큼 반복, 1씩 추가하면서 출력
for i in range(n):
    print(i + 1)


# 6. 기찍 N
# 입력 : 첫째 줄에 100,000보다 작거나 같은 자연수 N
# 출력 : 첫째 줄부터 N번째 줄 까지 차례대로 출력

n = int(input())

# n만큼 반복, 1씩 줄이면서 출력
for i in range(n):
    print(n - i)


# 7. A+B-7
# 입력 : 첫째 줄에 테스트 케이스의 개수 T, 각 테스트 케이스는 한 줄
#       각 줄에 A와 B가 주어짐 (0 < A, B < 10)
# 출력 : 각 테스트 케이스마다 "Case #x: "를 출력한 다음, A+B를 출력, 테스트 케이스 번호는 1부터 시작

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(f'Case #{i + 1}: {a + b}')


# 8. A+B - 8
# 입력 : 첫째 줄에 테스트 케이스의 개수 T, 각 테스트 케이스는 한 줄
#       각 줄에 A와 B가 주어짐 (0 < A, B < 10)
# 출력 : 각 테스트 케이스마다 "Case #x: A + B = C" 형식으로 출력
#       x는 테스트 케이스 번호이고 1부터 시작하며, C는 A+B

t = int(input())

for i in range(t):
    a, b = map(int, input().split())
    print(f'Case #{i + 1}: {a} + {b} = {a + b}')


# 9. 별 찍기 - 1
# 입력 : 첫째 줄에 N(1 ≤ N ≤ 100)
# 출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력

n = int(input())

for i in range(n):
    print('*' * (i + 1))


# 10. 별 찍기 - 2
# 입력 : 첫째 줄에 N(1 ≤ N ≤ 100)
# 출력 : 첫째 줄부터 N번째 줄까지 차례대로 별을 출력

n = int(input())

for i in range(n):
    print(' ' * (n - i - 1) + '*' * (i + 1))


# 11. X보다 작은 수
# 입력 : 첫째 줄에 N과 X (1 ≤ N, X ≤ 10,000)
#       둘째 줄에 수열 A를 이루는 정수 N, 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수
# 출력 : X보다 작은 수를 입력받은 순서대로 공백으로 구분 (X보다 작은 수는 적어도 하나 존재)

n, x = map(int, input().split())
N = list(map(int, input().split()))

for i in range(n):
    if N[i] < x:
        print(N[i], end=' ')


# 12. A+B-5
# 입력 : 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#       각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#       입력의 마지막에는 0 두 개가 들어온다.
# 출력 : 각 테스트 케이스마다 A+B를 출력

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    print(a + b)


# 13. A+B-4
# 입력 : 입력은 여러 개의 테스트 케이스로 이루어져 있다.
#       각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
# 출력 : 각 테스트 케이스마다 A+B를 출력

while True:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break


# 14. 더하기 사이클
# 입력 : 첫째 줄에 N이 주어진다. N은 0보다 크거나 같고, 99보다 작거나 같은 정수
# 출력 : 첫째 줄에 N의 사이클 길이를 출력

n = int(input())
x = n
result = 0

while True:
    a = x // 10
    b = x % 10
    c = (a + b) % 10
    x = (b * 10) + c

    result += 1
    if(x == n):
        break

print(result)
