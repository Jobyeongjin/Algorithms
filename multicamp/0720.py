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


# 1986. 지그재그 숫자
# 문제 : 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
#       N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고,
#       그 아래로 각 테스트 케이스가 주어진다. 각 테스트 케이스에는 N이 주어진다.
# 출력 : 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 누적된 값을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 테스트 케이스 t
t = int(input())

# 테스트 케이스만큼 반복
for tc in range(1, t+1):
    # 각 케이스 n
    n = int(input())
    result = 0

    # n만큼 반복
    for i in range(1, n+1):
        # 만일 i가 짝수라면
        if i % 2 == 0:
            # 결과값에서 빼고
            result -= i
        else:
            # 홀수면 더하기
            result += i
    print(f'#{tc} {result}')


# 1284. 수도 요금 경쟁
# 문제 : A사 : 1리터당 P원의 돈을 내야 한다.
#       B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.
#       종민이의 집에서 한 달간 사용하는 수도의 양이 W리터라고 할 때, 요금이 더 저렴한 회사를 골라 그 요금을 출력하는 프로그램을 작성하라.
# 입력 : 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#       각 테스트 케이스마다 첫 번째 줄에 위 본문에서 설명한 대로 P, Q, R, S, W(1 ≤ P, Q, R, S, W ≤ 10000, 자연수)가 순서대로 공백 하나로 구분되어 주어진다.
# 출력 : 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
#       종민이가 내야 하는 수도 요금을 출력한다.

t = int(input())

for i in range(1, t+1):
    # 순서에 맞게 입력을 받기
    P, Q, R, S, W = map(int, input().split())
    # A사 한 달 요금
    a = W * P
    # B사 한 달 요금
    b = Q

    # 만약 월간 사용량이 초과한다면
    if W > R:
        # 초과한 만큼 곱해서 더해주기
        b += (W - R) * S

    # 둘 중 최소값
    result = min(a, b)

    print(f"#{i} {result}")
