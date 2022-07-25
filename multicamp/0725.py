# 0. 숫자의개수 💭

# 각 줄의 자연수 입력
A = int(input())
B = int(input())
C = int(input())

# 각 자릿수를 담을 리스트 박스
number = [0] * 9
# 곱한 결과를 리스트, 문자 형태로 변환
result = list(str(A * B * C))

# 각 자릿수를 반복하여 해당 인덱스에 1씩 추가
for i in result:
    number[int(i)] += 1
# 한 줄씩 출력
for i in number:
    print(i)


# 1. 상수 💭

# 문자열 형태로 입력
a, b = input().split()

# 문자열을 뒤집고 숫자형으로 변환
a_reverse = int(a[::-1])
b_reverse = int(b[::-1])

# 두 수를 비교하여 큰 수를 출력
if a_reverse > b_reverse:
    print(a_reverse)
else:
    print(b_reverse)


# 2. 두개뽑아서더하기 💭

# 맨 아래 정의한 수가 numbers로 입력
def solution(numbers):
    # 결과를 담을 리스트 박스
    answer = []

    # 길이만큼 반복
    for i in range(len(numbers)):
        # 길이만큼 반복하는데 i 다음의 수부터 시작
        for j in range(i+1, len(numbers)):
            # 두 수를 더한 값이 answer 안에 없다면
            if numbers[i] + numbers[j] not in answer:
                # 더한 값을 추가
                answer.append(numbers[i] + numbers[j])

    # 오름차순으로 정렬
    answer.sort()

    return answer


# 3. OX퀴즈 💭

# 테스트 케이스
t = int(input())

# 케이스만큼 반복
for i in range(1, t + 1):
    # 문자열 리스트 형태로 입력
    n = list(input())
    # 'O' 가 연속될 때마다 오르는 수
    cnt = 0
    # 총합
    result = 0

    # 리스트 안 문자열을 순차적으로 반복
    for j in n:
        # 'O' 라면
        if j == 'O':
            # 1을 추가하고 총합에 더하기
            cnt += 1
            result += cnt
        # 'O' 가 아니라면
        else:
            # 카운트 리셋
            cnt = 0

    print(result)


# 4. A+B 💡

A, B = map(int, input().split())

print(A + B)


# 5. A+B-2 💡

A = int(input())
B = int(input())

print(A + B)


# 6. A+B-3 💭

t = int(input())

for tc in range(1, t + 1):
    A, B = map(int, input().split())

    print(A + B)


# 7. A+B-6 💭

t = int(input())

for tc in range(1, t + 1):
    A, B = map(int, input().split(','))

    print(A + B)


# 8. 별 찍기 - 1 💭

n = int(input())

for i in range(1, n + 1):
    print('*' * i)


# 9. 별 찍기 - 2 💭

n = int(input())

for i in range(1, n + 1):
    print(' ' * (n - i) + '*' * i)


# 10. 별 찍기 - 20 💭

n = int(input())

for i in range(1, n + 1):
    if i % 2:
        print('* ' * n)
    else:
        print(' *' * n)


# 11. 두 수 비교하기 💭

A, B = map(int, input().split())

if A > B:
    print('>')
elif A < B:
    print('<')
else:
    print('==')


# 12. 시험 성적 💭

n = int(input())

if n >= 90:
    print('A')
elif n >= 80:
    print('B')
elif n >= 70:
    print('C')
elif n >= 60:
    print('D')
else:
    print('F')


# 13. 윤년 💭

n = int(input())

if (n % 4 == 0 and n % 100 != 0) or n % 400 == 0:
    print(1)
else:
    print(0)


# 14. 사분면 고르기 💭

x = int(input())
y = int(input())

if x > 0 and y > 0:
    print(1)
elif x < 0 and y > 0:
    print(2)
elif x < 0 and y < 0:
    print(3)
else:
    print(4)


# 15. 구구단 💭

n = int(input())

for i in range(1, 10):
    print(f'{n} * {i} = {n * i}')


# 16. 합 💭

n = int(input())

result = 0

for i in range(1, n + 1):
    result += i

print(result)


# 17. N 찍기 💭

n = int(input())

for i in range(1, n + 1):
    print(i)


# 18. 기찍 N 💭

n = int(input())

for i in range(n):
    print(n - i)
    print(type(n))


# 19. A+B-7 💭

n = int(input())

for i in range(1, n + 1):
    a, b = map(int, input().split())

    print(f'Case #{i}: {a + b}')


# 20. A+B-8 💭

n = int(input())

for i in range(1, n + 1):
    a, b = map(int, input().split())

    print(f'Case #{i}: {a} + {b} = {a + b}')


# 21. A+B-5 💭

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    else:
        print(a + b)


# 22. X보다 작은 수 💭

n, x = map(int, input().split())
a = list(map(int, input().split()))

for i in a:
    if i < x:
        print(i, end=' ')


# 23. 주사위 세개 💭

a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + a * 1000)
elif a == b or a == c:
    print(1000 + a * 100)
elif b == c:
    print(1000 + b * 100)
else:
    print(max(a, b, c) * 100)


# 24. 한수 💭

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


# 25. 더하기 사이클 💭

n = int(input())
num = n
cnt = 0

while True:
    # 26부터 시작
    a = num // 10  # 몫인 2
    b = num % 10  # 나머지인 6
    c = (a + b) % 10  # 나머지인 8
    num = (b * 10) + C  # 68

    # 사이클 1 추카
    cnt += 1
    # 숫자가 같아지면 멈춤
    if num == n:
        break

print(cnt)


# 26. 최소, 최대 💭

n = int(input())
nums = list(map(int, input().split()))

# min(), max() 함수 사용
print(min(nums), max(nums))
