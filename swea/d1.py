# 2029. 몫과 나머지 출력하기
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T, 그 아래로 각 테스트 케이스가 주어짐
#       각 테스트 케이스의 첫 번째 줄에는 2개의 수
# 출력 : 출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음 몫을 출력
#       공백을 한 칸 둔 다음 나머지를 출력 (t는 테스트 케이스의 번호를 의미하며 1부터 시작)

t = int(input())

for i in range(1, t + 1):
    a, b = map(int, input().split())

    print('#{} {} {}'.format(i, a // b, a % b))


# 0719 : 거꾸로 출력해 보아요
# 입력 : 주어진 숫자(8)부터 0까지 순서대로 찍기
# 출력 : 8 7 6 5 4 3 2 1 0

t = int(input())

for i in range(0, t + 1):
    print(t - i, end=' ')


# 2071. 평균값 구하기
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어짐
#       각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어짐
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작)

t = int(input())

for i in range(1, t + 1):
    n = list(map(int, input().split()))

    t = 0
    for a in n:
        t += a

    result = round(t / 10)

    print('#{} {}'.format(i, result))


# 2070. 큰 놈, 작은 놈, 같은 놈
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for i in range(1, t + 1):
    a, b = map(int, input().split())

    if a > b:
        print(f'#{i} >')
    elif a < b:
        print(f'#{i} <')
    else:
        print(f'#{i} =')


# 1933. 간단한 N의 약수
# 입력 : 입력으로 정수 N 이 주어진다.
#       N은 1이상 1,000이하의 정수이다. (1 ≤ N ≤ 1,000)
# 출력 : 정수 N 의 모든 약수를 오름차순으로 출력한다.
#       약수란, 수를 어떤 값으로 나눈 나머지가 0이라면 약수

n = int(input())

# 1부터 n까지 반복
for i in range(1, n+1):
    # 만일 n을 i로 나눈 나머지가 0이라면
    if n % i == 0:
        # 한 줄로 공백을 두고 출력
        print(i, end=' ')


# 2019. 더블더블
# 문제 : 1부터 주어진 횟수까지 2를 곱한 값 출력, 주어진 숫자는 30을 넘지 않는다.
# 입력 : 8
# 출력 : 1 2 4 8 16 32 64 128 256

n = int(input())
# 1부터 시작
result = 1

# n만큼 반복
for i in range(n+1):
    print(result, end=' ')
    # 나온 결과에 2를 곱해서 반복
    result *= 2


# 2050. 알파벳을 숫자로 변환
# 문제 : 알파벳으로 이루어진 문자열을 입력 받아 각 알파벳을 1부터 26까지의 숫자로 변환하여 출력하라.
#       문자열의 최대 길이는 200이다.
# 입력 : ABCDEFGHIJKLMNOPQRSTUVWXYZ
# 출력 : 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26

A = input()

for i in A:
    result = ord(i) - 64
    print(result, end=' ')


# 2072. 홀수만 더하기
# 문제 : 10개의 수를 입력 받아, 그 중에서 홀수만 더한 값을 출력
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 숫자로 받은 테스트 케이스
t = int(input())

# 테스트 케이스만큼 반복
for tc in range(1, t+1):
    # 각 케이스의 공백으로 이뤄진 10개의 수를 나눠서 반복문에 입력
    n = map(int, input().split())
    result = 0

    for i in n:
        # 만약 i가 짝수가 아니라면 즉, 홀수라면
        if i % 2 != 0:
            # 결과값에 더하기
            result += i

    print(f'#{tc} {result}')


# 2068. 최대수 구하기
# 문제 : 10개의 수를 입력 받아, 그 중에서 가장 큰 수를 출력하는 프로그램을 작성하라.
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 정수로 받은 케이스
t = int(input())

# 케이스만큼 반복
for tc in range(1, t+1):
    # 각 케이스의 공백으로 이뤄진 수를 나눠서 반복문에 입력
    n = map(int, input().split())
    result = 0

    for i in n:
        # 만약 i가 결과값보다 크다면
        if i > result:
            # 결과값은 i
            result = i

    print(f'#{tc} {result}')


# 2063. 중간값 찾기
# 문제 : 중간값은 통계 집단의 수치를 크기 순으로 배열 했을 때 전체의 중앙에 위치하는 수치를 뜻한다.
#       입력으로 N 개의 점수가 주어졌을 때, 중간값을 출력
#       1. N은 항상 홀수로 주어진다.
#       2. N은 9이상 199 이하의 정수이다. (9 ≤ N ≤ 199)
# 입력 : 입력은 첫 줄에 N 이 주어진다. 둘째 줄에 N 개의 점수가 주어진다
# 출력 : N 개의 점수들 중, 중간값에 해당하는 점수를 정답으로 출력한다.

n = int(input())
# 리스트로 접근
m = list(map(int, input().split()))
# 순차적으로 정렬
m.sort()

for i in range(n):
    # 만약 i가 n을 2로 나눈 몫이라면 즉, 중간이라면
    if i == n//2:
        # 해당 위치의 값 출력
        print(m[i])
        break


# 2058. 자릿수 더하기
# 문제 : 하나의 자연수를 입력 받아 각 자릿수의 합을 계산하는 프로그램을 작성하라.
#       자연수 N은 1부터 9999까지의 자연수이다. (1 ≤ N ≤ 9999)
# 입력 : 입력으로 자연수 N이 주어진다.
# 출력 : 각 자릿수의 합을 출력한다.

# 문자형인 숫자 '6789' 입력
n = input()
result = 0

# 문자열의 길이만큼 반복 (0~3)
for i in range(len(n)):
    # 결과값에 해당 인덱스 위치의 값을 숫자형으로 변환해서 더하기
    result += int(n[i])

print(result)


# 2056. 연월일 달력
# 문제 : 해당 날짜의 유효성을 판단한 후, 날짜가 유효하다면 ”YYYY/MM/DD”형식으로 출력하고,
#       날짜가 유효하지 않을 경우, -1 을 출력하는 프로그램을 작성하라.
#       연월일로 구성된 입력에서 월은 1~12 사이 값을 가져야 하며
#       일은 1일 ~ 각각의 달에 해당하는 날짜까지의 값을 가질 수 있다.
#       ※ 2월의 경우, 28일인 경우만 고려한다. (윤년은 고려하지 않는다.)
# 입력 : 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
#       다음 줄부터 각 테스트 케이스가 주어진다.
# 출력 : 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 숫자형인 케이스 '5'
t = int(input())

# 케이스만큼 반복
for tc in range(1, t+1):
    # 각 케이스는 문자형
    n = input()

    # 연월일에 맞게 쪼개기
    Y = n[:4]
    M = n[4:6]
    D = n[6:8]
    day = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    # 만약 월 값이 1보다 작거나 12보다 큰 경우
    if int(M) < 1 or int(M) > 12:
        print(f'#{tc} -1')
        # 아래 코드 건너뛰고 반복
        continue
    else:
        # 만약 일 값이 1보다 작거나, 딕셔너리에 지정된 값보다 큰 경우
        if int(D) < 1 or day[int(M)] < int(D):
            print(f'#{tc} -1')
            # 아래 코드 건너뛰고 반복
            continue
        else:
            print(f'#{tc} {Y}/{M}/{D}')
