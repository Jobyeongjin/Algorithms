# 1. 최소, 최대 💭
# 문제 : N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 정수의 개수 N (1 ≤ N ≤ 1,000,000)이 주어진다.
#       둘째 줄에는 N개의 정수를 공백으로 구분해서 주어진다. 모든 정수는 -1,000,000보다 크거나 같고, 1,000,000보다 작거나 같은 정수이다.
# 출력 : 첫째 줄에 주어진 정수 N개의 최솟값과 최댓값을 공백으로 구분해 출력한다.

n = int(input())
num = list(map(int, input().split()))

print(min(num), max(num))


# 2. 최댓값 💭
# 문제 : 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄부터 아홉 번째 줄까지 한 줄에 하나의 자연수가 주어진다. 주어지는 자연수는 100 보다 작다.
# 출력 : 첫째 줄에 최댓값을 출력하고, 둘째 줄에 최댓값이 몇 번째 수인지를 출력한다.

n = []

for i in range(9):
    n.append(int(input()))

print(max(n))
print(n.index(max(n)) + 1)


# 3. 숫자의 개수 💭
# 문제 : 세 개의 자연수 A, B, C가 주어질 때 A × B × C를 계산한 결과에 0부터 9까지 각각의 숫자가 몇 번씩 쓰였는지를 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 A, 둘째 줄에 B, 셋째 줄에 C가 주어진다. A, B, C는 모두 100보다 크거나 같고, 1,000보다 작은 자연수이다.
# 출력 : 첫째 줄에는 A × B × C의 결과에 0 이 몇 번 쓰였는지 출력한다.
#       마찬가지로 둘째 줄부터 열 번째 줄까지 A × B × C의 결과에 1부터 9까지의 숫자가 각각 몇 번 쓰였는지 차례로 한 줄에 하나씩 출력한다.

a = int(input())
b = int(input())
c = int(input())

num_x = list(str(a * b * c))

arr = [0] * 10

for i in num_x:
    arr[int(i)] += 1

# for j in arr:
#   print(j)
# 한 줄로!!
# print(j for j in arr) => Error🚨
# 리스트로 감싸고, 리스트를 없애고, 구분자로 개행 입력...
print(*[j for j in arr], sep='\n')


# 4. 나머지 💭
# 문제 : 수 10개를 입력받은 뒤, 이를 42로 나눈 나머지를 구한다. 그 다음 서로 다른 값이 몇 개 있는지 출력하는 프로그램을 작성하시오.
# 입력 : 첫째 줄부터 열번째 줄 까지 숫자가 한 줄에 하나씩 주어진다. 이 숫자는 1,000보다 작거나 같고, 음이 아닌 정수이다.
# 출력 : 첫째 줄에, 42로 나누었을 때, 서로 다른 나머지가 몇 개 있는지 출력한다.

arr = []

for i in range(10):
    n = int(input())
    n_rest = n % 42
    arr.append(n_rest)

print(len(set(arr)))


# 5. OX퀴즈 💭
# 문제 : "OOXXOXXOOO"의 점수는 1+2+0+0+1+0+0+1+2+3 = 10점이다.
#       OX퀴즈의 결과가 주어졌을 때, 점수를 구하는 프로그램을 작성하시오.
# 입력 : 첫째 줄에 테스트 케이스의 개수가 주어진다.
#       각 테스트 케이스는 한 줄로 이루어져 있고, 길이가 0보다 크고 80보다 작은 문자열이 주어진다.
#       문자열은 O와 X만으로 이루어져 있다.
# 출력 : 각 테스트 케이스마다 점수를 출력한다.

t = int(input())

for i in range(1, t + 1):
    n = list(input())
    cnt = 0
    result = 0

    for j in n:
        if j == 'O':
            cnt += 1
            result += cnt
        else:
            cnt = 0

    print(result)


# 6. 평균은 넘겠지 💭
# 문제 : 대학생 새내기들의 90%는 자신이 반에서 평균은 넘는다고 생각한다. 당신은 그들에게 슬픈 진실을 알려줘야 한다.
# 입력 : 첫째 줄에는 테스트 케이스의 개수 C가 주어진다.
#       둘째 줄부터 각 테스트 케이스마다 학생의 수 N(1 ≤ N ≤ 1000, N은 정수)이 첫 수로 주어지고, 이어서 N명의 점수가 주어진다.
#       점수는 0보다 크거나 같고, 100보다 작거나 같은 정수이다.
# 출력 : 각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.

n = int(input())

for _ in range(n):
    score = list(map(int, input().split()))
    average = sum(score[1:]) / score[0]

    cnt = 0
    for i in score[1:]:
        if i > average:
            cnt += 1

    per = (cnt / score[0]) * 100

    # round 함수는 사용불가, 40.0%는 소숫점 표기가 안됨 🚨
    print('{:.3f}%'.format(per))
