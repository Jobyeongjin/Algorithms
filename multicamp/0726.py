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
