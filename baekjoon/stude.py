"""10870 - 피보나치 수 5"""
# 인덱스 접근
# 앞에 두자리를 더해서 리스트에 추가
# 마지막 값 출력

n = int(input())

answer = [0, 1]
for i in range(2, n + 1):
    plus = answer[i - 1] + answer[i - 2]
    answer.append(plus)

print(answer[n])


"""10250 - ACM 호텔"""
# 층수와 룸 번호를 구해서 더하기 -> 층수 = 나눈 나머지, 룸 번호 = 나눈 몫 +1
# 예외는 찾을 방과 층 높이가 같은 경우 -> 층수 = 높이, 룸 번호 = -1

t = int(input())

for _ in range(1, t + 1):
    h, w, n = map(int, input().split())  # 6 12 10

    floor = n % h
    room = n // h + 1
    if floor == 0:
        floor = h
        room -= 1

    print(floor * 100 + room)


"""17413 - 단어 뒤집기 2"""
# 문자열을 반복하면서 <> 구간에서는 스위칭하면서 그대로 스택에 입력
# 공백을 제외한 나머지는 반대로 입력

s = input()
check = 0
answer = ''
stack = ''

for i in s:
    if check == 0:
        if i == '<':
            check = 1
            stack += i
        elif i == ' ':
            stack += i
            answer += stack
            stack = ''
        else:
            stack = i + stack

    elif check == 1:
        stack += i
        if i == '>':
            check = 0
            answer += stack
            stack = ''

print(answer + stack)


"""10973 - 이전 순열 """

n = int(input())
arr = list(map(int, input().split()))

k = -1
for i in range(len(arr) - 1):
    if arr[i] > arr[i + 1]:
        k = i

if k == -1:
    print(-1)
else:
    for i in range(k + 1, len(arr)):
        if arr[i] < arr[k]:
            m = i

    arr[k], arr[m] = arr[m], arr[k]

    temp = arr[k + 1:]
    temp.sort(reverse=True)
    answer = arr[:k + 1] + temp

    print(*answer)


"""16935 - 배열 돌리기 3"""
# zip() -> 길이가 같은(순회가능한) 객체의 인자를 받아서 인덱스끼리 묶어준다


def one():
    global arr
    arr = arr[::-1]


def two():
    global arr
    for i in range(n):
        arr[i] = arr[i][::-1]


def three():
    global arr
    arr = list(map(list, zip(*arr[::-1])))


def four():
    global arr
    arr = list(map(list, zip(*arr)))[::-1]


def five():
    global arr, n, m
    temp = [[0] * m for _ in range(n)]
    N, M = n // 2, m // 2
    for r in range(N):
        for c in range(M):
            temp[r][c + M] = arr[r][c]
            temp[r + N][c + M] = arr[r][c + M]
            temp[r + N][c] = arr[r + N][c + M]
            temp[r][c] = arr[r + N][c]
    arr = temp


def six():
    global arr, n, m
    temp = [[0] * m for _ in range(n)]
    N, M = n // 2, m // 2
    for r in range(N):
        for c in range(M):
            temp[r + N][c] = arr[r][c]
            temp[r][c] = arr[r][c + M]
            temp[r][c + M] = arr[r + N][c + M]
            temp[r + N][c + M] = arr[r + N][c]
    arr = temp


n, m, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
ope = list(map(int, input().split()))

for i in ope:
    if i == 1:
        one()
    elif i == 2:
        two()
    elif i == 3:
        three()
    elif i == 4:
        four()
    elif i == 5:
        five()
    else:
        six()

for i in arr:
    print(*i)
