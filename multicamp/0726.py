# 문제 : 두 수의 최대공약수, 최소공배수 구하기
# 공약수란, 두 수 사이의 공통으로 존재하는 약수 💡
# 공배수란, 두 수의 공통적인 배수 💡

import math

a, b = map(int, input().split())

print(math.gcd(a, b))  # 최대공약수
print(math.lcm(a, b))  # 최소공배수


# 문제 : 자연수 n(분해합)의 가장 작은 생성자 구하기
# 입력 : 216
# 출력 : 198
# 분해합이란, N과 N의 각 자릿수의 합 💡

# 접근 : 입력값 = 분해합이고 생성자보다 작기 때문에 반복문을 입력값만큼 사용
#       문자열로 쪼개서 리스트에 담는데 sum 함수 사용을 위해 숫자형으로 변환
#       분해합을 구하고, 그 분해합이 적용되는 수를 찾아 결과값에 저장

n = int(input())
result = 0

for i in range(1, n + 1):
    a = list(map(int, str(i)))
    sum_ = i + sum(a)

    if(sum_ == n):
        result = i
        break

print(result)


# 문제 : 최대 오르막길 구하기
# 입력 : 5
#       1 2 1 4 6
# 출력 : 5

# 접근 : 지속해서 증가해야 오르막길이니 리스트의 숫자를 반복하면서 더 큰 수 비교
#       크다면 두 수의 차 = 오르막길, 아니면 리셋, 리셋하기 전에 변수에 저장

n = int(input())
num = list(map(int, input().split()))

way = num[0]
high = 0
save = 0


for i in num:
    if way < i:
        high += i - way
    if way >= i:
        save = max(save, high)
        high = 0
    way = i

print(max(high, save))


# 문제 : 5명이 서로 다른 사람에게 평가점수를 주고, 우승자와 그의 점수를 구하기
# 입력 : 5 4 4 5
#       5 4 4 4
#       5 5 4 4
#       5 5 5 4
#       4 4 4 5
# 출력 : 4 19

# 접근 : 4개의 수를 더하고, 더한 값을 리스트에 저장
#       리스트에서 가장 큰 수를 구하고, 그 인덱스 값 찾기

sum_score = []

for i in range(5):
    sum_ = sum(map(int, input().split()))
    sum_score.append(sum_)

print(sum_score.index(max(sum_score)) + 1, max(sum_score))


# 문제 : 신문 헤드라인
# 입력 : 입력으로 80 bytes 이하의 길이를 가진 문자열이 주어진다.
# 출력 : 문자열의 소문자를 모두 대문자로 변경한 결과를 출력한다.

# 접근 : 대문자 변환 함수 사용

char = input()

print(char.upper())


# 문제 : 알파벳을 숫자로 변환
# 입력 : 알파벳으로 이루어진 문자열이 주어진다.
# 출력 : 각 알파벳을 숫자로 변환한 결과값을 빈 칸을 두고 출력한다.

# 접근 : 아스키 코드로 변환하기 (알파벳 A = 65)

char = input()

for i in char:
    result = ord(i) - 64
    print(result, end=' ')


# 문제 : 연월일 달력
# 입력 : 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다.
#       다음 줄부터 각 테스트 케이스가 주어진다.
# 출력 : 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 접근 : 연월일을 나누고 주어진 날짜가 정상인지 아닌지 비교하기

t = int(input())

for tc in range(1, t + 1):
    n = input()

    Y = n[:4]
    M = n[4:6]
    D = n[6:8]

    day = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
           7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    if int(M) < 1 or int(M) > 12:
        print(f'#{tc} -1')
        continue
    else:
        if int(D) < 1 or day[int(M)] < int(D):
            print(f'#{tc} -1')
            continue
        else:
            print(f'#{tc} {Y}/{M}/{D}')


# 문제 : 자릿수 더하기
# 입력 : 6789
# 출력 : 30

# 접근 : 문자열의 인덱스인 각 자릿수를 결과값에 더하기

n = input()
result = 0

for i in range(len(n)):
    result += int(n[i])

print(result)


# 중간값 찾기
# 입력 : 입력은 첫 줄에 N 이 주어진다. 둘째 줄에 N 개의 점수가 주어진다.
# 출력 : N 개의 점수들 중, 중간값에 해당하는 점수를 정답으로 출력한다.

# 접근 : 리스트를 정렬한 뒤 가운데 값을 찾아 인덱스로 접근

n = int(input())
m = list(map(int, input().split()))
m.sort()

for i in range(n):
    if i == n//2:
        print(m[i])
        break


# 최대수 구하기
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.

t = int(input())

for tc in range(1, t + 1):
    n = list(map(int, input().split()))
    print(f'#{tc} {max(n)}')


# 큰 놈, 작은 놈, 같은 놈
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 2개의 수가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for tc in range(1, t + 1):
    a, b = map(int, input().split())

    if a < b:
        print(f'#{tc} <')
    elif a > b:
        print(f'#{tc} >')
    else:
        print(f'#{tc} =')


# 평균값 구하기
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for tc in range(1, t + 1):
    n = list(map(int, input().split()))

    cnt = 0
    for i in n:
        cnt += i

    result = round(cnt / 10)

    print(f'#{tc} {result}')


# 홀수만 더하기
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for tc in range(1, t + 1):
    n = list(map(int, input().split()))

    result = 0
    for i in n:
        if i % 2 != 0:
            result += i

    print(f'#{tc} {result}')


# 최빈수 구하기
# 입력 : 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#       각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.
# 출력 : #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    score = list(map(int, input().split()))
    score_board = [0] * (max(score) + 1)
    result = 0

    for i in score:
        score_board[i] += 1

    cnt_max = max(score_board)
    for j in range(len(score_board)):
        if score_board[j] == cnt_max:
            if j > result:
                result = j

    print(f'#{tc} {result}')
