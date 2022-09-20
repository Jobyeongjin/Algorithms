from collections import deque

"""📝 10870 - 피보나치 수 5"""
# 인덱스 접근
# 앞에 두자리를 더해서 리스트에 추가
# 마지막 값 출력

n = int(input())

answer = [0, 1]
for i in range(2, n + 1):
    plus = answer[i - 1] + answer[i - 2]
    answer.append(plus)

print(answer[n])


"""📝 10250 - ACM 호텔"""
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


"""📝 17413 - 단어 뒤집기 2"""
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


"""📝 10973 - 이전 순열 """

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


"""📝 16935 - 배열 돌리기 3"""
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


"""📝 1138 - 한 줄로 서기"""
# 거꾸로 접근해 리스트에 추가 -> 입력의 수는 점점 작아지기 때문에 원하는 인덱스에 추가 가능

n = int(input())
arr = list(map(int, input().split()))
answer = []

for i in range(len(arr)-1, -1, -1):
    answer.insert(arr[i], i + 1)

print(*answer)


"""📝 3986 - 좋은 단어"""
# 단어를 하나씩 스택에 추가하면서 마지막 요소와 동일하다면 스택에서 제거
# 스택에 비었다면 카운팅

n = int(input())

cnt = 0
for _ in range(n):
    s = input().strip()
    stack = []

    for i in range(len(s)):
        if stack and s[i] == stack[-1]:
            stack.pop()
        else:
            stack.append(s[i])

    if not stack:
        cnt += 1

print(cnt)


"""📝 2+1 세일"""
# 비싼 제품을 무료로 받아야 최소비용이 가능하니 오름차순으로 정렬
# 3번째 요소는 무료이니 패스

n = int(input())
price = [int(input()) for _ in range(n)]
price.sort(reverse=True)

answer = 0
cnt = 0
for i in range(n):
    cnt += 1
    if cnt == 3:
        cnt = 0
        continue
    answer += price[i]

print(answer)


"""📝 섬의 개수"""
# 입력 마지막은 제외
# 완전 탐색으로 1을 만나면 DFS, BFS 실행

while True:
    w, h = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(h)]

    if w == 0 and h == 0:
        break

    delta = ((0, -1), (1, -1), (1, 0), (1, 1),
             (0, 1), (-1, 1), (-1, 0), (-1, -1))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                stack = []
                stack.append((i, j))

                while stack:
                    (c, r) = stack.pop()
                    if maps[c][r] == 1:
                        maps[c][r] = 0

                        for dr, dc in delta:
                            nr = dr + r
                            nc = dc + c

                            if -1 < nc < h and -1 < nr < w:
                                if maps[nc][nr] == 1:
                                    stack.append((nc, nr))
                cnt += 1

    print(cnt)


#
while True:
    w, h = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(h)]

    delta = ((0, -1), (1, -1), (1, 0), (1, 1),
             (0, 1), (-1, 1), (-1, 0), (-1, -1))

    if w == 0 and h == 0:
        break

    def DFS(c, r):
        stack = []
        stack.append((c, r))

        while stack:
            (c, r) = stack.pop()
            maps[c][r] = 0
            for dr, dc in delta:
                nr = dr + r
                nc = dc + c

                if -1 < nc < h and -1 < nr < w and maps[nc][nr] == 1:
                    stack.append((nc, nr))

    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                DFS(i, j)
                cnt += 1

    print(cnt)


#
while True:
    w, h = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(h)]

    delta = ((0, -1), (1, -1), (1, 0), (1, 1),
             (0, 1), (-1, 1), (-1, 0), (-1, -1))

    if w == 0 and h == 0:
        break

    def BFS(c, r):
        queue = deque()
        queue.append([c, r])

        while queue:
            c, r = queue.popleft()
            for dr, dc in delta:
                nr = dr + r
                nc = dc + c

                if -1 < nc < h and -1 < nr < w and maps[nc][nr] == 1:
                    maps[nc][nr] = 0
                    queue.append([nc, nr])

    cnt = 0
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 1:
                maps[i][j] = 0
                BFS(i, j)
                cnt += 1

    print(cnt)


"""swea 14413 - 격자판 칠하기"""
# 좌표 값을 각각(짝수, 홀수별로) 누적해 비교
# ex)
# - # 짝수에 값이 있으면 # 홀수에는 값이 없어야 한다.
# - . 짝수에 값이 있으면 . 홀수에는 값이 없어야 한다.
# - # 짝수에 값이 있으면 . 짝수에는 값이 없어야 한다.


t = int(input())

for tc in range(1, t + 1):
    r, c = map(int, input().split())
    board = [list(input().strip()) for _ in range(r)]
    arr = [0, 0, 0, 0]

    for x in range(r):
        for y in range(c):
            if board[x][y] == '#':
                if (x + y) % 2 == 0:
                    arr[0] += 1
                elif (x + y) % 2 == 1:
                    arr[1] += 1
            elif board[x][y] == '.':
                if (x + y) % 2 == 0:
                    arr[2] += 1
                elif (x + y) % 2 == 1:
                    arr[3] += 1

    if (arr[0] and arr[1]) or (arr[2] and arr[3]) or (arr[0] and arr[2]) or (arr[1] and arr[3]):
        print(f'#{tc} impossible')
    else:
        print(f'#{tc} possible')
