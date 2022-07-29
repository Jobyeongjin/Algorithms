# 1. 정수 N개의 합
# 문제 : 정수 n개가 주어졌을 때, n개의 합을 구하는 함수를 작성하시오.
#       def solve(a: list) -> int
#       a: 합을 구해야 하는 정수 n개가 저장되어 있는 리스트
#       리턴값: a에 포함되어 있는 정수 n개의 합 (정수)

def solve(a):
    return sum(a)


# 2. 셀프 넘버

def func(n):
    num = list(str(n))
    asw = n
    for i in range(len(num)):
        asw += int(num[i])
    return asw


set_ = list(range(1, 10001))
for n in range(1, 10001):
    if func(n) in set_:
        set_.remove(func(n))

for i in range(len(set_)):
    print(set_[i])


# 3. 한수
# 문제 : 어떤 양의 정수 X의 각 자리가 등차수열을 이룬다면, 그 수를 한수라고 한다.
#       등차수열은 연속된 두 개의 수의 차이가 일정한 수열을 말한다. N이 주어졌을 때, 1보다 크거나 같고, N보다 작거나 같은 한수의 개수를 출력하는 프로그램을 작성하시오.

n = int(input())

hansu = 0
for i in range(1, n + 1):

    if i < 100:
        hansu += 1
    else:
        ns = list(map(int, str(i)))
        if ns[0] - ns[1] == ns[1] - ns[2]:
            hansu += 1

print(hansu)
