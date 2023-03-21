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


# 배열 자르기
def solution(numbers, num1, num2):
    return numbers[num1 : num2 + 1]


# 외계행성의 나이
def solution(age):
    answer = ""
    alpha = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
    for i in str(age):
        answer += alpha[int(i)]
    return answer


# 진료순서 정하기
def solution(emergency):
    answer = []
    temp = sorted(emergency, reverse=True)
    for i in emergency:
        answer.append(temp.index(i) + 1)
    return answer


# 순서쌍의 개수
def solution(n):
    answer = []
    for i in range(1, n + 1):
        if n % i == 0:
            answer.append((i, n // i))
    return len(answer)


# 개미군단
def solution(hp):
    answer = 0

    answer += hp // 5
    hp %= 5
    answer += hp // 3
    hp %= 3
    answer += hp // 1
    hp %= 1

    return answer


# 모스부호
def solution(letter):
    answer = ""
    morse = {
        ".-": "a",
        "-...": "b",
        "-.-.": "c",
        "-..": "d",
        ".": "e",
        "..-.": "f",
        "--.": "g",
        "....": "h",
        "..": "i",
        ".---": "j",
        "-.-": "k",
        ".-..": "l",
        "--": "m",
        "-.": "n",
        "---": "o",
        ".--.": "p",
        "--.-": "q",
        ".-.": "r",
        "...": "s",
        "-": "t",
        "..-": "u",
        "...-": "v",
        ".--": "w",
        "-..-": "x",
        "-.--": "y",
        "--..": "z",
    }

    for i in letter.split():
        answer += morse[i]

    return answer


# 가위바위보
def solution(rsp):
    answer = ""

    for i in rsp:
        if i == "2":
            answer += "0"
        elif i == "0":
            answer += "5"
        elif i == "5":
            answer += "2"

    return answer


# 구슬을 나누는 경우의 수
# 1차 실패 - 시간 초과
from itertools import combinations


def solution(balls, share):
    answer = []
    ballNums = [ballNum for ballNum in range(balls)]

    for i in combinations(ballNums, share):
        answer.append(i)

    return len(answer)


# 2차 실패 - 틀린 답안
def solution(balls, share):
    answer = 0

    for i in range(balls):
        for j in range(i + 1, balls):
            print(i, j)

    return answer


# 3차 성공 - 1차에서 리스트가 필요없어지니 훨씬 간결해짐
import math


def solution(balls, share):
    return math.comb(balls, share)


# 4차 성공 - 알고보니 팩토리얼
def solution(balls, share):
    def fact(n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    answer = fact(balls) / (fact(balls - share) * fact(share))

    return answer


# 점의 위치 구하기
def solution(dot):
    x, y = dot
    if 0 < x and 0 < y:
        return 1
    elif 0 > x and 0 < y:
        return 2
    elif 0 > x and 0 > y:
        return 3
    else:
        return 4


# 2차원으로 만들기
def solution(num_list, n):
    return [num_list[i - n : i] for i in range(n, len(num_list) + 1, n)]


# 공 던지기
def solution(numbers, k):
    return numbers[(k - 1) * 2 % len(numbers)]


# 배열 회전시키기
from collections import deque


def solution(numbers, direction):
    numbers = deque(numbers)
    numbers.rotate(1 if direction == "right" else -1)
    return list(numbers)


# 주사위의 개수
def solution(box, n):
    r, c, h = box
    return (r // n) * (c // n) * (h // n)


# 합성수 찾기
def solution(n):
    answer = 0
    for num in range(4, n + 1):
        cnt = 0
        for i in range(1, num + 1):
            if num % i == 0:
                cnt += 1
        if cnt >= 3:
            answer += 1
    return answer


# 최댓값 만들기
def solution(numbers):
    numbers.sort(reverse=True)
    return numbers[0] * numbers[1]


# 팩토리얼
def solution(n):
    i = 0
    fact = 1
    while fact <= n:
        i += 1
        fact *= i
    answer = i - 1
    return answer


# 모음 제거
def solution(my_string):
    string = "aeiou"
    for i in string:
        my_string = my_string.replace(i, "")
    return my_string


# 문자열 정렬하기
def solution(my_string):
    answer = []
    nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
    for i in my_string:
        for num in nums:
            if i == num:
                answer.append(int(i))
    answer.sort()
    return answer


# 숨어있는 숫자의 덧셈
def solution(my_string):
    answer = 0
    nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in my_string:
        for num in nums:
            if i == str(num):
                answer += int(i)
    return answer


# 소인수분해
def solution(n):
    answer = []
    i = 2
    while i <= n:
        if n % i == 0:
            n = n // i
            answer.append(i)
        else:
            i += 1
    return sorted(list(set(answer)))


# 컨트롤 제트
def solution(s):
    answer = 0
    for i in range(len(s.split())):
        if s[i] == "Z":
            answer -= int(s[i - 1])
        else:
            answer += int(s[i])
    return answer


# 배열 원소의 길이
def solution(strlist):
    return [len(s) for s in strlist]


# 중복된 문자 제거
def solution(my_string):
    answer = ""
    arr = []
    for i in my_string:
        if i in arr:
            continue
        arr.append(i)
    for i in arr:
        answer += i
    return answer


# 삼각형의 완성조건(1)
def solution(sides):
    sides = sorted(sides, reverse=True)
    maxNum = sides[0]
    for i in range(1, len(sides)):
        maxNum -= sides[i]
    if maxNum > -1:
        return 2
    else:
        return 1


# 가까운 수
def solution(array, n):
    answer = 0
    gap = 10e9
    for i in sorted(array):
        if abs(i - n) < gap:
            gap = abs(i - n)
            answer = i
    return answer


# 369게임
def solution(order):
    answer = 0
    for i in str(order):
        if i == "3" or i == "6" or i == "9":
            answer += 1
    return answer


# 암호 해독
def solution(cipher, code):
    answer = ""
    i = 0
    cnt = code - 1
    while i < len(cipher):
        if cnt == 0:
            answer += cipher[i]
            cnt = code
        cnt -= 1
        i += 1
    return answer


# 대문자와 소문자
def solution(my_string):
    answer = ""
    for i in my_string:
        if i.isupper():
            answer += i.lower()
        else:
            answer += i.upper()
    return answer


# 영어가 싫어요
def solution(numbers):
    nums = [
        "zero",
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
    ]
    for i, s in enumerate(nums):
        numbers = numbers.replace(s, str(i))
    return int(numbers)


# 인덱스 바꾸기
def solution(my_string, num1, num2):
    answer = ""
    for i in range(len(my_string)):
        if i == num1:
            answer += my_string[num2]
        elif i == num2:
            answer += my_string[num1]
        else:
            answer += my_string[i]
    return answer


# 한 번만 등장한 문자
def solution(s):
    answer = ""
    s = sorted(s)
    for i in s:
        if s.count(i) > 1:
            continue
        answer += i
    return answer


# 약수 구하기
def solution(n):
    answer = []
    i = 1
    while i <= n:
        if n % i == 0:
            answer.append(i)
        i += 1
    return answer


# 편지
def solution(message):
    return len(message) * 2


# 가장 큰 수 찾기
def solution(array):
    maxNum = max(array)
    return [maxNum, array.index(maxNum)]


# 문자열 계산하기
def solution(my_string):
    answer = 0
    flag = True
    for i in my_string.split():
        if i == "-":
            flag = False
            continue
        elif i == "+":
            flag = True
            continue

        if flag:
            answer += int(i)
        else:
            answer -= int(i)
    return answer


# 배열의 유사도
def solution(s1, s2):
    answer = 0
    for i in s1:
        if i in s2:
            answer += 1
    return answer


# 숫자 찾기
def solution(num, k):
    num = str(num)
    answer = []
    for i in range(1, len(num) + 1):
        if num[i - 1] == str(k):
            answer.append(i)
    if answer:
        return answer[0]
    else:
        return -1


# N의 배수 고르기
def solution(n, numlist):
    answer = []
    for num in numlist:
        if num % n == 0:
            answer.append(num)
    return answer


# 자릿수 더하기
def solution(n):
    answer = 0
    for i in str(n):
        answer += int(i)
    return answer


# OX 퀴즈
def solution(quiz):
    answer = []
    for i in quiz:
        cnt = 0
        check = True
        result = False
        temp = ""
        for j in i.split():
            if result:
                if temp == j:
                    answer.append("O")
                else:
                    answer.append("X")

            if j == "-":
                check = False
                continue
            elif j == "+":
                check: True
                continue

            if j == "=":
                temp += str(cnt)
                result = True
                continue

            if check:
                cnt += int(j)
            else:
                cnt -= int(j)
    return answer


# 문자열 안에 문자열
def solution(str1, str2):
    return 1 if str2 in str1 else 2


# 제곱수 판별하기
def solution(n):
    answer = 2
    cnt = 0
    while cnt < n:
        if cnt * cnt == n:
            answer = 1
        cnt += 1
    return answer


# 세균 증식
def solution(n, t):
    for _ in range(t):
        n = n * 2
    return n


# 문자열 정렬하기(2)
def solution(my_string):
    return "".join(sorted(list(my_string.lower())))


# 7의 개수
def solution(nums):
    answer = 0
    for num in nums:
        answer += str(num).count("7")
    return answer


# 잘라서 배열로 저장하기
def solution(my_str, n):
    answer = []
    for i in range(0, len(my_str), n):
        answer.append(my_str[i : i + n])
    return answer


# 중복된 숫자 개수
def solution(array, n):
    return array.count(n)


# 머쓱이보다 키 큰 사람
def solution(array, n):
    return array.count(n)


# 직사각형 넓이 구하기
def solution(dots):
    x = [dot[0] for dot in dots]
    y = [dot[1] for dot in dots]
    r = max(x) - min(x)
    c = max(y) - min(y)
    return r * c


# 캐릭터의 좌표
def solution(keyinput, board):
    answer = [0, 0]
    mid = [board[0] // 2, board[1] // 2]
    for key in keyinput:
        print(key)
        if key == "up":
            if answer[1] >= mid[1]:
                answer[1] = mid[1]
            else:
                answer[1] += 1
        elif key == "down":
            if answer[1] <= -mid[1]:
                answer[1] = -mid[1]
            else:
                answer[1] -= 1
        elif key == "left":
            if answer[0] <= -mid[0]:
                answer[0] = -mid[0]
            else:
                answer[0] -= 1
        else:
            if answer[0] >= mid[0]:
                answer[0] = mid[0]
            else:
                answer[0] += 1
    return answer


# 최댓값 구하기(2)
def solution(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[-1] * numbers[-2])


# 다항식 구하기
def solution(polynomial):
    x, num = 0, 0
    for i in polynomial.split(" + "):
        if "x" in i:
            if len(i) == 1:
                x += 1
            else:
                x += int(i[:-1])
        else:
            num += int(i)
    if x == 1:
        x = ""
    if num == 0:
        return f"{x}x"
    if x == 0:
        return f"{num}"
    if num == 0 and x == 0:
        return "0"
    return f"{x}x + {num}"
