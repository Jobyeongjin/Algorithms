"""📝 직사각형 별찍기"""

N, M = map(int, input().split())

for _ in range(M):
    print('*' * N)


"""📝 x만큼 간격이 있는 n개의 숫자"""


def solution(x, n):
    answer = []
    for i in range(1, n + 1):
        answer.append(x * i)

    return answer


"""📝 행렬의 덧셈"""


def solution(arr1, arr2):
    answer = arr1

    for i in range(len(arr1)):
        for j in range(len(arr1[0])):
            arr1[i][j] += arr2[i][j]

    return answer


"""📝 핸드폰 번호 가리기"""


def solution(phone_number):
    answer = ''

    answer = '*' * (len(phone_number) - 4) + phone_number[-4:]

    return answer


"""📝 하샤드 수"""


def solution(x):
    sum_ = 0
    for i in str(x):
        sum_ += int(i)

    if x % sum_ == 0:
        return True
    else:
        return False


"""📝 평균 구하기"""


def solution(arr):
    return sum(arr) / len(arr)


"""📝 콜라츠 추측"""


def solution(n):
    answer = 0

    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = n * 3 + 1

        answer += 1

        if answer == 500:
            answer = -1
            break

    return answer


"""📝 최대공약수와 최소공배수"""


def gcd(n, m):
    while m > 0:
        n, m = m, n % m

    return n


def lcm(n, m):
    return n * m / gcd(n, m)


def solution(n, m):
    answer = []
    answer.append(gcd(n, m))
    answer.append(lcm(n, m))

    return answer


"""📝 짝수와 홀수"""


def solution(num):
    answer = ''

    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'

    return answer


"""📝 제일 작은 수 제거하기"""


def solution(arr):
    if len(arr) > 1:
        arr.remove(min(arr))

        return arr
    else:
        return [-1]


"""📝 정수 제곱근 판별"""


def solution(n):
    answer = 0
    number = n ** 0.5  # 재곱근

    if number % 1 == 0:  # 정수인지 판별
        answer = (number + 1) ** 2
    else:
        answer = -1

    return answer


"""📝 정수 내림차순으로 배치하기"""


def solution(n):
    answer = sorted(list(str(n)), reverse=True)

    return int(''.join(answer))
