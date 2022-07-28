# 나머지
# 문제 : 42로 나눴을 때, 서로 다른 나머지가 몇 개인지 출력
# 접근 : 42로 나눈 나머지를 구하고, 중복 값을 제거해 남은 개수를 구함

arr = []
for i in range(10):
    n = int(input())
    n_ = n % 42
    arr.append(n_)

print(len(set(arr)))


# SASA 모형을 만들어보자
# 문제 : SASA 모형 개수의 최댓값을 출력하기
#       모형 1개는 S, A가 각각 2개씩 필요
# 접근 : 더 작은 수를 찾아서 모형에 필요한 개수인 2로 나누기

S, A = map(int, input().split())

result = min(S, A)

print(result // 2)


# 쉽게 푸는 문제 🚨
# 문제 : 수열(12233344445...)을 만들고 해당 구간에 속하는 숫자의 합 구하기
# 접근 : d

a, b = map(int, input().split())

data = [0]
sum = 0
# 수열 만들기
for i in range(1, b + 1):
    for j in range(i):
        data.append(i)

for i in range(a, b + 1):
    sum += data[i]

print(sum)


# 뒤집힌 덧셈
# 문제 : 두 양의 정수 X와 Y가 주어졌을 때,
#       Rev(Rev(X) + Rev(Y))를 구하는 프로그램을 작성하시오
# 접근 : 문자열로 입력받아 뒤집어서 더하고, 다시 뒤집기

x, y = input().split()

x_rev = x[::-1]
y_rev = y[::-1]

sum_ = str(int(x_rev) + int(y_rev))
print(int(sum_[::-1]))


# 다이얼
# 문제 : 첫째 줄에 다이얼을 걸기 위해 필요한 최소 시간을 출력
# 접근 : 입력받은 문자를 리스트 안에서 찾고, 해당 인덱스 값으로 더해가기

number = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

alpha = list(input())

time = 0

for i in alpha:
    for j in number:
        if i in j:
            time += number.index(j) + 3  # 인덱스는 0부터, 알파벳은 3부터

print(time)
