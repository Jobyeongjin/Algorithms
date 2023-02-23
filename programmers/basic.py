def solution(num1, num2):
    """두 수의 합"""
    return num1 + num2


def solution(num1, num2):
    """두 수의 차"""
    return num1 - num2


def solution(num1, num2):
    """두 수의 곱"""
    return num1 * num2


def solution(num1, num2):
    """몫 구하기"""
    return num1 // num2


def solution(num1, num2):
    """두 수의 나눗셈"""
    return int(num1 / num2 * 1000)


def solution(num1, num2):
    """숫자 비교하기"""
    return 1 if num1 == num2 else -1


def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a


def solution(numer1, denom1, numer2, denom2):
    """분수의 덧셈"""
    topNum = numer2 * denom1 + numer1 * denom2
    botNum = denom1 * denom2

    val = gcd(botNum, topNum)
    ans = [topNum // val, botNum // val]
    return ans


def solution(numbers):
    """배열 두 배 만들기"""
    return [num * 2 for num in numbers]


def solution(num1, num2):
    """나머지 구하기"""
    return num1 % num2


def solution(array):
    """중앙값 구하기"""
    array.sort()
    return array[len(array) // 2]


def solution(numbers):
    """최빈값 구하기"""
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


def solution(n):
    """짝수는 싫어요"""
    answer = []
    for num in range(1, n + 1):
        if num % 2 == 1:
            answer.append(num)
    return answer
