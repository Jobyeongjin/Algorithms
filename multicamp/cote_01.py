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


"""📝 자연수 뒤집어 배열로 만들기"""


def solution(n):
    answer = []

    for i in str(n)[::-1]:
        answer.append(int(i))

    return answer


"""📝 자릿수 더하기"""


def solution(n):
    answer = 0

    for i in str(n):
        answer += int(i)

    return answer


"""📝 이상한 문자 만들기"""


def solution(s):
    answer = []
    s = s.split(' ')

    for i in range(len(s)):
        result = ''
        for j in range(len(s[i])):
            if j % 2 == 0:
                result += s[i][j].upper()
            else:
                result += s[i][j].lower()

        answer.append(result)

    return ' '.join(answer)


"""📝 약수의 합"""


def solution(n):
    answer = 0

    for i in range(1, n + 1):
        if n % i == 0:
            answer += i

    return answer


"""📝 시저 암호 🚨"""


def solution(s, n):
    s = list(s)

    for i in range(len(s)):
        if s[i].isupper():  # 모든 문자열이 대문자이면 True
            s[i] = chr((ord(s[i]) - ord('A') + n) % 26 + ord('A'))
        elif s[i].islower():  # 모든 문자열이 소문자이면 True
            s[i] = chr((ord(s[i]) - ord('a') + n) % 26 + ord('a'))

    return ''.join(s)

# 아스키코드로 치환 후 거리 계산 후 다시 문자로 반환한다.
# %26은 범위를 벗어나지 않게 한다.(알파벳은 총 25글자)


"""📝 문자열을 정수로 바꾸기"""


def solution(s):
    return int(s)


"""📝 수박수박수?"""


def solution(n):
    answer = ''
    for i in range(1, n + 1):
        if i % 2 == 0:
            answer += '박'
        else:
            answer += '수'
    return answer


"""📝 서울에서 김서방 찾기"""


def solution(seoul):
    answer = ''
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            answer = f'김서방은 {i}에 있다'
    return answer


"""📝 문자열 다루기 기본🚨"""
# isnumeric() -> 숫자로만 구성된 문자열로, 문자열에 숫자만 있다면 True, 아니면 False을 반환


def solution(s):
    answer = True
    s = list(s)

    for i in s:
        if i.isnumeric() and (len(s) == 4 or len(s) == 6):  # 숫자이면서 길이가 4 또는 6인 경우
            pass
        else:   # 그외는 False 후 종료
            answer = False
            break

    return answer


"""📝 문자열 내림차순으로 배치하기"""


def solution(s):
    answer = ''
    answer = s[::-1]
    return answer


"""📝 문자열 내 p와 y의 개수"""


def solution(s):
    p = s.count('P') + s.count('p')
    y = s.count('Y') + s.count('y')

    if p == y:
        return True
    else:
        return False
