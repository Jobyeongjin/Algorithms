# 두 수의 합
def solution(num1, num2):
    return num1 + num2


# 두 수의 차
def solution(num1, num2):
    return num1 - num2


# 두 수의 곱
def solution(num1, num2):
    return num1 * num2


# 몫 구하기
def solution(num1, num2):
    return num1 // num2


# 두 수의 나눗셈
def solution(num1, num2):
    return int(num1 / num2 * 1000)


# 숫자 비교하기
def solution(num1, num2):
    return 1 if num1 == num2 else -1


# 분수의 덧셈
def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(numer1, denom1, numer2, denom2):
    topNum = numer2 * denom1 + numer1 * denom2
    botNum = denom1 * denom2

    val = gcd(botNum, topNum)
    ans = [topNum // val, botNum // val]
    return ans


# 배열 두 배 만들기
def solution(numbers):
    return [num * 2 for num in numbers]


# 나머지 구하기
def solution(num1, num2):
    return num1 % num2


# 중앙값 구하기
def solution(array):
    array.sort()
    return array[len(array) // 2]


# 최빈값 구하기
def solution(numbers):
    numCount = {}
    for num in numbers:
        if num in numCount:
            numCount[num] += 1
        else:
            numCount[num] = 1

    numItems = sorted(numCount.items(), key=lambda x: x[-1], reverse=True)
    if len(numItems) <= 1:
        return numItems[0][0]
    else:
        return numItems[0][0] if numItems[0][-1] != numItems[1][-1] else -1


# 짝수는 싫어요
def solution(n):
    answer = []
    for num in range(1, n + 1):
        if num % 2 == 1:
            answer.append(num)
    return answer


# 피자 나눠먹기 1
def solution(n):
    pizza = 0
    if n % 7 == 0:
        pizza = n // 7
    else:
        pizza = n // 7 + 1
    return pizza


# 피자 나눠먹기 2
def solution(n):
    pizza = 1
    while True:
        if (pizza * 6) % n == 0:
            break
        else:
            pizza += 1
    return pizza


# 피자 나눠먹기 3
def solution(slice, n):
    pizza = 0
    if n % slice == 0:
        pizza = n // slice
    else:
        pizza = n // slice + 1
    return pizza


# 평균값 구하기
def solution(numbers):
    return sum(numbers) / len(numbers)
