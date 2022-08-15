# 소수 찾기 🐳
# 문제 : 주어진 수 N개 중에서 소수가 몇 개인지 찾아서 출력하는 프로그램을 작성하시오.

# 소수란, 1과 자기자신으로 나눌 때만 떨어지는 자연수 💡

n = int(input())
numbers = map(int, input().split())

sosu = 0
for num in numbers:
    if num != 1:  # 1이 아닌 수라면
        for i in range(2, num):  # 자기 자신을 제외한 수로 나눠지는지 확인
            if num % i == 0:
                break
        else:  # 아니면 소수
            sosu += 1

print(sosu)


# 소수 🐳
# 문제 : 예를 들어 M=60, N=100인 경우 60이상 100이하의 자연수 중 소수는 61, 67, 71, 73, 79, 83, 89, 97 총 8개가 있으므로, 이들 소수의 합은 620이고, 최솟값은 61이 된다.
# 출력 : M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다.
#       단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

n = int(input())
m = int(input())

sosu_list = []
for num in range(n, m + 1):  # 60부터 100까지 반복
    if num != 1:
        check = True
        for i in range(2, num):  # 자기 자신을 제외한 수로 나눠지는지 확인
            if num % i == 0:
                check = False
                break
        if check:
            sosu_list.append(num)

if sosu_list:  # 리스트가 참 또는 1 이면 출력
    print(sum(sosu_list), min(sosu_list), sep='\n')
else:
    print(-1)


# 소수 구하기 🐳
# 문제 : 소수 구하기

N, M = map(int, input().split())

for i in range(N, M + 1):
    # 1은 소수가 아니니 넘어가고
    if i == 1:
        continue
    # 에라토스테네스의 체 -> 일정 범위내 수열에서 배수들을 제거해 소수만 걸러내는 체를 말함💡
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            break
    else:
        print(i)
