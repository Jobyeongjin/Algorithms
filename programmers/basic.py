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


# 옷가게 할인 받기
def solution(price):
    if 100000 <= price and price < 300000:
        price -= price * 0.05
    elif 300000 <= price and price < 500000:
        price -= price * 0.1
    elif 500000 <= price:
        price -= price * 0.2
    return int(price)


# 아이스 아메리카노
def solution(money):
    if money % 5500 == 0:
        return [money // 5500, 0]
    else:
        return [money // 5500, money - 5500 * (money // 5500)]


# 나이 출력
def solution(age):
    return 2022 - age + 1


# 배열 뒤집기
def solution(num_list):
    answer = []
    for i in range(len(num_list) - 1, -1, -1):
        answer.append(num_list[i])
    return answer


# 문자열 뒤집기
def solution(string):
    return string[::-1]


# 직각삼각형 출력하기
for i in range(1, int(input()) + 1):
    print(i * "*")

# 짝수 홀수 개수
def solution(num_list):
    answer = [0, 0]
    for num in num_list:
        if num % 2 == 0:
            answer[0] += 1
        else:
            answer[1] += 1
    return answer


# 문자 반복 출력하기
def solution(my_string, n):
    answer = ""
    for s in my_string:
        answer += s * n
    return answer


# 특정 문자 제거하기
def solution(my_string, letter):
    return my_string.replace(letter, "")


# 각도기
def solution(angle):
    answer = 0
    if angle == 180:
        answer = 4
    elif angle > 90:
        answer = 3
    elif angle == 90:
        answer = 2
    else:
        answer = 1
    return answer


# 양꼬치
def solution(n, k):
    answer = 0

    service = 0
    if n >= 10:
        service = n // 10
    k -= service

    answer += n * 12000
    answer += k * 2000
    return answer


# 짝수의 합
def solution(n):
    answer = 0
    for num in range(1, n + 1):
        if num % 2 == 0:
            answer += num
    return answer
