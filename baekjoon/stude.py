from itertools import permutations, combinations
from collections import deque, Counter
import heapq
import sys

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
answer = ""
stack = ""

for i in s:
    if check == 0:
        if i == "<":
            check = 1
            stack += i
        elif i == " ":
            stack += i
            answer += stack
            stack = ""
        else:
            stack = i + stack

    elif check == 1:
        stack += i
        if i == ">":
            check = 0
            answer += stack
            stack = ""

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

    temp = arr[k + 1 :]
    temp.sort(reverse=True)
    answer = arr[: k + 1] + temp

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

for i in range(n - 1, -1, -1):
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

    delta = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

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

    delta = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

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

    delta = ((0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1), (-1, 0), (-1, -1))

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


"""📝 swea 14413 - 격자판 칠하기"""
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
            if board[x][y] == "#":
                if (x + y) % 2 == 0:
                    arr[0] += 1
                elif (x + y) % 2 == 1:
                    arr[1] += 1
            elif board[x][y] == ".":
                if (x + y) % 2 == 0:
                    arr[2] += 1
                elif (x + y) % 2 == 1:
                    arr[3] += 1

    if (
        (arr[0] and arr[1])
        or (arr[2] and arr[3])
        or (arr[0] and arr[2])
        or (arr[1] and arr[3])
    ):
        print(f"#{tc} impossible")
    else:
        print(f"#{tc} possible")


"""📝 로봇 청소기"""
# 회전할 때마다 좌표 변경
# 4번 회전했다면 후진하는데 만약 후진할 수 없다면 종료
# 방문처리하면서 카운팅


def turn_left():
    global arrow
    arrow -= 1
    if arrow == -1:
        arrow = 3


n, m = map(int, input().split())
r, c, arrow = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]

visited = [[0] * m for _ in range(n)]
visited[r][c] = 1

# 북 동 남 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

clean = 1
turn = 0
while True:
    turn_left()

    nr = r + dr[arrow]
    nc = c + dc[arrow]
    if visited[nr][nc] == 0 and room[nr][nc] == 0:
        visited[nr][nc] = 1
        clean += 1
        r, c = nr, nc
        turn = 0
        continue
    else:
        turn += 1

    if turn == 4:
        nr = r - dr[arrow]
        nc = c - dc[arrow]
        if room[nr][nc] == 0:
            r, c = nr, nc
            turn = 0
        else:
            break

print(clean)


"""📝 요세푸스 문제"""
# deque 활용 문제 -> rotate 함수를 사용하여 왼쪽으로 회전하며, 첫번째 요소 빼기

n, k = map(int, input().split())

arr = [i for i in range(1, n + 1)]
q = deque(arr)
answer = []

while q:
    q.rotate(-(k - 1))
    answer.append(q.popleft())

print("<", end="")
print(*answer, sep=", ", end="")
print(">")


"""📝 돌려막기"""

arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]

# answer.append(sum([x * y for x, y in zip(arr1[0], arr2[0])]))
# answer.append(sum([x * y for x, y in zip(arr1[1], arr2[1])]))
# answer.append(sum([x * y for x, y in zip(arr1[2], arr2[2])]))
# answer.append(sum([x * y for x, y in zip(arr1[3], arr2[3])]))
# answer.append(sum([x * y for x, y in zip(arr1[4], arr2[4])]))

# 1 = arr1[0][0] * arr2[0][0]
# 2 = arr1[0][1] * arr2[1][1]
# 3 = arr1[0][2] * arr2[2][2]
# 4 = arr1[0][3] * arr2[3][3]
# 5 = arr1[0][4] * arr2[4][4]

answer = []
one = []
for i in range(5):
    for j in range(5):
        if i == j:
            one.append(arr2[i][j])

cnt1 = 0
for i in range(5):
    cnt1 += arr1[0][i] * one[i]
answer.append(cnt1)

cnt2 = 0
for i in range(5):
    cnt2 += arr1[1][i] * one[i]
answer.append(cnt2)

cnt3 = 0
for i in range(5):
    cnt3 += arr1[2][i] * one[i]
answer.append(cnt3)

cnt4 = 0
for i in range(5):
    cnt4 += arr1[3][i] * one[i]
answer.append(cnt4)

cnt5 = 0
for i in range(5):
    cnt5 += arr1[4][i] * one[i]
answer.append(cnt5)

print(answer)
min_ = min(answer)
if min_ == answer[4]:
    print("Youngki")
elif min_ == answer[3]:
    print("Jinwoo")
elif min_ == answer[2]:
    print("Jungwoo")
elif min_ == answer[1]:
    print("Junsuk")
elif min_ == answer[0]:
    print("Inseo")


"""📝 덱"""
# 조건에 맞게 출력하는 조건문 작성

n = int(input())
q = deque()

for _ in range(n):
    s = input().split()

    if s[0] == "push_front":
        q.appendleft(s[1])
    elif s[0] == "push_back":
        q.append(s[1])
    elif s[0] == "pop_front":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif s[0] == "pop_back":
        if q:
            print(q.pop())
        else:
            print(-1)
    elif s[0] == "size":
        print(len(q))
    elif s[0] == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif s[0] == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif s[0] == "back":
        if q:
            print(q[len(q) - 1])
        else:
            print(-1)


"""📝 단지번호붙이기"""
# 방문처리하면서 단지 내 건물도 같이 카운팅

n = int(input())

dangi = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))


def DFS(r, c):
    stack = []
    stack.append((r, c))

    cnt = 0
    while stack:
        r, c = stack.pop()

        if visited[r][c] == 0 and dangi[r][c] == 1:
            visited[r][c] = 1
            cnt += 1

        for dr, dc in delta:
            nr = dr + r
            nc = dc + c
            if -1 < nr < n and -1 < nc < n:
                if visited[nr][nc] == 0 and dangi[nr][nc] == 1:
                    stack.append((nr, nc))

    return cnt


answer = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and dangi[i][j] == 1:
            answer.append(DFS(i, j))

answer.sort()
print(len(answer))
for i in answer:
    print(i)


"""수들의 합 2"""
# 투 포인터
# 끝점을 이동하면서 카운팅
# 카운팅한 값이 k라면 경우의 수 1 추가

n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
e, sum = 0, 0

for s in range(n):
    while sum < k and e < n:
        sum += arr[e]
        e += 1

    if sum == k:
        answer += 1
    sum -= arr[s]

print(answer)

# 또는
n, k = map(int, input().split())
arr = list(map(int, input().split()))

answer = 0
s, e, sum = 0, 1, arr[0]


while s < n:
    if sum == k:
        answer += 1
        sum -= arr[s]
        s += 1
    elif e == n and sum < k:
        break
    elif sum > k:
        sum -= arr[s]
        s += 1
    else:
        sum += arr[e]
        e += 1


print(answer)


"""알람 시계"""
# 45분 이상이면 45분을 빼주고, 45분 이하라면 1시간을 빼고, 15분(60 - 45)을 더하기
# 단, 0시일 경우에만 23시로 지정

h, m = map(int, input().split())

if m < 45:
    if h == 0:
        h = 23
        m += 15
    else:
        h -= 1
        m += 15
else:
    m -= 45

print(h, m)


"""개미"""
# 이동할 개미와 다음 개미의 그룹이 다르다면 위치 변경
# 이동한 개미가 그룹의 첫번째 개미라면 종료

n, m = map(int, input().split())
a = list(input().strip())[::-1]
b = list(input().strip())
t = int(input())
ant = a + b

for _ in range(t):
    for i in range(len(ant) - 1):
        if ant[i] in a and ant[i + 1] in b:
            ant[i], ant[i + 1] = ant[i + 1], ant[i]
            if ant[i + 1] == a[n - 1]:
                break

print(*ant, sep="")


"""트럭"""
# deque 사용 - 해당 길이의 다리 생성
# 시간은 계속 흐르니 while문을 활용해 조건 작성
# 하중 = 다리 위에 있는 트럭의 무게 + 다음 트럭
# 무게가 작거나 같다면 트럭을 다리위에 추가, 아니면 0 추가

n, w, l = map(int, input().split())
truck = deque(list(map(int, input().split())))

bg = deque([0] * w)
cnt = 0

while bg:
    cnt += 1
    bg.popleft()
    if truck:
        if sum(bg) + truck[0] <= l:
            bg.append(truck.popleft())
        else:
            bg.append(0)
    # if len(bg) == 1 and bg[0] != 0:
    #     bg.extend([0] * (w - 1))
    #     if truck:
    #         bg.append(truck.popleft())
    #     bg.popleft()
    #     cnt += 1
    # if not bg:
    #     break

print(cnt)


"""적록색약"""
# BFS 사용 - 방문처리
# 방문 조건에서 다음 좌표가 이전 좌표와 같은지를 확인
# 색약인 사람은 조건에 맞게 rgb를 변형하고,
# 방문처리도 리셋하고 BFS 실행

n = int(input())
rgb = [list(input().strip()) for _ in range(n)]
visited = [[0] * n for _ in range(n)]

delta = ((0, -1), (1, 0), (0, 1), (-1, 0))


def BFS(r, c):
    q = deque()
    q.append((r, c))

    while q:
        r, c = q.popleft()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if (
                -1 < nr < n
                and -1 < nc < n
                and visited[nr][nc] == 0
                and rgb[nr][nc] == rgb[r][c]
            ):
                q.append((nr, nc))
                visited[nr][nc] = 1


one = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            one += 1

for l in rgb:
    for i, v in enumerate(l):
        if v == "G":
            l[i] = "R"

visited = [[0] * n for _ in range(n)]

two = 0
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            BFS(i, j)
            two += 1

print(one, two)


"""신입 사원"""
# 오름차순으로 정렬(서류) 후 가장 작은 수인 첫번째 요소를 기준으로 설정
# 다음 수와 비교(면접)하면서 더 크다면 카운팅

t = int(input())

for tc in range(t):
    n = int(input())
    rank = [list(map(int, input().split())) for _ in range(n)]
    rank.sort()

    one = rank[0][1]
    cnt = 1
    for i in range(1, n):
        if rank[i][1] < one:
            one = rank[i][1]
            cnt += 1

    print(cnt)


"""4와 7"""
K = int(input())
n = 0
while 1:
    i = (2**n) - 1
    j = (2 ** (n + 1)) - 2
    if i <= K and K <= j:
        print(bin((i + 1) + K - i)[3:].replace("0", "4").replace("1", "7"))
        break
    n += 1

# 시간 초과 코드 ⁉
# n = int(input())

# answer = 0
# cnt = 0
# while True:
#     if answer == n:
#         break
#     cnt += 1
#     word = str(cnt)
#     if "4" in word:
#         if word.count("4") + word.count("7") == len(word):
#             answer += 1
#     if "7" in word:
#         if word.count("7") == len(word):
#             answer += 1

# print(cnt)


"""패션왕 신해빈"""
# 입을 것들을 딕셔너리에 담기
# 입을 아이템이 하나라면 값의 개수를 출력
# 여럿이라면 곱한 값을 누적

t = int(input())

for tc in range(t):
    n = int(input())
    dic = {}
    for i in range(n):
        item, wear = input().split()
        if wear in dic:
            dic[wear] += [item]
        else:
            dic[wear] = [item]

    if len(dic) == 1:
        print(len(*dic.values()))
    else:
        cnt = 1
        for i in dic.values():
            cnt *= len(i) + 1

        print(cnt - 1)

# 또는

t = int(input())

for tc in range(t):
    n = int(input())

    dic = {}
    for i in range(n):
        item, wear = input().split()
        if wear in dic:
            dic[wear] += 1
        else:
            dic[wear] = 1

    cnt = 1
    for i in dic:
        cnt *= dic[i] + 1
    print(cnt - 1)

# 오답처리 코드 ‼️
# t = int(input())

# for tc in range(t):
#     n = int(input())
#     if n == 0:
#         break
#     dic = {}
#     for i in range(n):
#         item, wear = input().split()
#         if wear in dic:
#             dic[wear] += 1
#         else:
#             dic[wear] = 1

#     if len(dic) == 1:
#         print(n)
#     else:
#         cnt = 1
#         for i in dic:
#             cnt *= dic[i]
#         print(cnt + n)


"""프린터 큐"""
# 주어진 인덱스(m)에 있는 문서가 중요도에 따라 언제 나가는지 확인하는 문제
# 마지막 예제 케이스에 같은 수가 여럿이기 때문에 인덱스로 접근
# -> 인덱스를 표시할 배열을 만들고, 수 배열과 똑같이 돌리고 제거하기를 반복
# 큰 수(중요도)부터 빠져나가니 배열에서 가장 큰 값을 제거하면서 카운팅

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    arr = deque(list(map(int, input().split())))

    idx = []
    for i in range(len(arr)):
        idx.append(i)
    idx = deque(idx)
    idx[m] = "temp"

    cnt = 0
    while True:
        if arr[0] == max(arr):
            cnt += 1
            if idx[0] == "temp":
                print(cnt)
                break
            else:
                arr.popleft()
                idx.popleft()
        else:
            arr.rotate(-1)
            idx.rotate(-1)


"""설탕 배달"""
# 정해진 무게에서 최소한의 봉지를 구하는 문제
# 5로 나눠지면 몫을 구하고, 아니면 3을 빼면서 카운팅
# 5로 나뉘지 않고 3을 빼다가 0보다 작아지면 -1을 출력

n = int(input())

cnt = 0
while n >= 0:
    if n % 5 == 0:
        cnt += n // 5
        print(cnt)
        break
    n -= 3
    cnt += 1

else:
    print(-1)


"""로프"""
# 로프가 버틸 수 있는 최대 중량 구하는 문제
# 버틸 수 있는 최대 중량 = 로프 개수 * 가벼운 중량
# 작은 수가 마지막 인덱스가 되도록 내림차순 정렬

n = int(input())

rope = list(int(input()) for _ in range(n))
rope.sort(reverse=True)

answer = list(rope[i] * (i + 1) for i in range(n))
print(max(answer))


"""DFS와 BFS"""
# DFS, BFS 문제

n, m, v = map(int, input().split())

arr = [[] for _ in range(n + 1)]  # 인접 리스트 생성 = [[], [2,3,4], [1,4], [1,4] [1,2,3]]
for _ in range(m):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

visited = [0] * (n + 1)  # 방문 처리 리스트 = [[], [], [], [], []]

for i in arr:  # 정점 번호 오름차순 정렬
    i.sort()


def DFS(v):
    visited[v] = 1
    print(v, end=" ")

    for i in arr[v]:
        if visited[i] != 1:
            DFS(i)


def BFS(v):
    visited[v] = 1
    q = deque([v])

    while q:
        qp = q.popleft()
        print(qp, end=" ")

        for i in arr[qp]:
            if visited[i] != 1:
                q.append(i)
                visited[i] = 1


DFS(v)
visited = [0] * (n + 1)  # BFS 실행을 위한 방문 처리 초기화
print()
BFS(v)


"""코스튬 파티"""
# 투 포인터 문제
# -> 코스튬을 입는 소의 인덱스 = (0,2), (0,3), (1,3), (2,3)
# pypy3 통과

n, c = map(int, input().split())

cow = [int(input()) for _ in range(n)]

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if cow[i] + cow[j] <= c:
            cnt += 1

print(cnt)


"""ATM"""
# 각 사람이 돈을 뽑는데 필요한 시간이 있고, 그 시간 합의 최소값 구하는 문제
# 최소값을 구하기 위해 오름차순 정렬
# 슬라이싱을 통해 배열의 합을 더하기
# -> 총합 = (0), (0~1), (0~2), (0~3), (0~4) 누적값

n = int(input())
time = list(map(int, input().split()))
time.sort()

answer = 0
for i in range(1, n + 1):
    answer += sum(time[:i])

print(answer)

"""콘센트"""
# 힙 문제
# 오래 걸리는 기기부터 시작하고, 충전자리가 비었다면 기기를 추가
# 다음 충전에 들어갈 기기는 적게 걸리는 기기의 시간을 더해 추가
# -> heap을 사용하는 이유(모듈이 Minheap으로 구현)!!
# -> 오래 걸리는 기기는 어떻게든 시간을 할애하게 됨

n, m = map(int, input().split())
time = list(map(int, input().split()))
time.sort(reverse=True)

heap = []
for i in time:
    if len(heap) < m:
        heapq.heappush(heap, i)
    else:
        out = heapq.heappop(heap)
        heapq.heappush(heap, out + i)

print(max(heap))


# 실패 코드
n, m = map(int, input().split())
time = list(map(int, input().split()))
time.sort(reverse=True)

answer = 0
for i in range(n):
    if time[i] >= m:
        if time[i] % m == 0:
            answer += time[i] // m
        else:
            answer += time[i] // m
            time[i + 1] += time[i] % m
    else:
        if time[i] > m:
            if time[i] % m == 0:
                answer += time[i] // m
            else:
                answer += (time[i] // m) + 1
        else:
            answer += 1

print(answer)


"""꿍의 여친 만들기"""
# 만날 수 있는 조합과 걸리는 시간을 딕셔너리에 저장하기
# 조건(단어)들을 반복하면서 딕셔너리에서 값을 찾아 배열에 넣고, 배열 중 가장 큰 값을 또다른 상위 배열에 저장
# 그중 가장 작은 수(최소 시간)를 출력

tc = int(input())

for _ in range(tc):
    a = input().strip().split(",")
    b = input().strip().split("|")

    answer = []

    dic = {}
    for i in a:
        c, t = i.split(":")
        dic[c] = t

    for i in b:
        i = i.split("&")
        box = []
        for j in i:
            box.append(int(dic[j]))
        answer.append(max(box))

    print(min(answer))


"""수리공 항승"""
n, l = map(int, input().split())
position = list(map(int, input().split()))
position.sort()

start = position[0]  # 시작지점
tape = position[0] + l  # 테이프 길이
answer = 1  # 길이가 1일 수도 있으니 1부터 시작

for i in range(n):
    if start <= position[i] < tape:
        continue
    else:
        start = position[i]
        tape = position[i] + l
        answer += 1

print(answer)


# 실패
n, l = map(int, input().split())
position = list(map(int, input().split()))
position.sort()

end = position[-1]
num = 0
answer = 0
while end >= num:
    if position:
        if num == position[0]:
            del position[0]
            answer += 1
            if ((num - 1) + l) in position:
                idx = position.index((num - 1) + l)
                del position[: idx + 1]
                num = (num - 1) + l
                continue
    else:
        break
    num += 1

print(answer)


"""통계학"""
# 평균값 : 리스트의 합 나누기 n
# 중앙값 : 리스트 인덱스가 n으로 나눈 몫
# 최빈수 : Counter().most_common() 사용 - 가장 많이 나온 데이터 순으로 정렬
# 범위 : 최대값 - 최소값
n = int(input())
numbers = [int(input()) for _ in range(n)]
numbers.sort()


def average(nums):
    return round(sum(nums) / n)


print(average(numbers))


def center(nums):
    return nums[n // 2]


print(center(numbers))


def more(nums):
    list = Counter(nums).most_common()
    if len(nums) > 1:
        if list[0][1] == list[1][1]:
            return list[1][0]
        else:
            return list[0][0]
    else:
        return list[0][0]


print(more(numbers))


def scope(nums):
    return max(nums) - min(nums)


print(scope(numbers))


"""좋다"""
# 오름차순 정렬
# 판별할 수를 제외한 나머지 수를 투포인터 범위로 설정
# 더한 값이 좋은 수라면 참, 아니면 거짓을 리턴
n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()


def twopo(i, target):
    scope = numbers[:i] + numbers[i + 1 :]
    start, end = 0, n - 2
    while start < end:
        sum_ = scope[start] + scope[end]
        if target < sum_:
            end -= 1
        elif target > sum_:
            start += 1
        else:
            return True
    return False


good = 0
for i in range(n):
    if twopo(i, numbers[i]):
        good += 1
print(good)


"""보석 도둑"""
# 보석(무게, 가격)과 가방(무게) 모두 오름차순 정렬
# 가방에 넣을 수 있는 보석 찾기
# - HEAP을 사용하고, 내가 찾는 보석은 비싼 보석이기 때문에
# - 기본적으로 구현된 최소힙에서 음수값으로 처리해 최대힙으로 찾기
n, k = map(int, input().split())
gems = [list(map(int, input().split())) for _ in range(n)]
gems.sort()
bags = [int(input()) for _ in range(k)]
bags.sort()

answer = 0
temp = []
for bag in bags:
    while gems and gems[0][0] <= bag:
        heapq.heappush(temp, -heapq.heappop(gems)[1])
    if temp:
        answer -= heapq.heappop(temp)
print(answer)


"""통나무 건너뛰기"""
# 통나무 오름차순 정렬
# 넘을 수 있는 최소 난이도는 인덱스로 볼 때 2차이가 남
# - 정렬된 리스트와 테스트케이스와 비교
for _ in range(int(input())):
    n = int(input())
    nums = sorted(list(map(int, input().split())))
    answer = 0
    for i in range(2, n):
        answer = max(answer, nums[i] - nums[i - 2])
    print(answer)


"""두 수의 합"""
# 투포인터, 오름차순 정렬
# 더한 값이 x값이라면 카운팅
n = int(input())
numbers = sorted(list(map(int, input().split())))
x = int(input())

answer, start, end = 0, 0, n - 1
while start < end:
    sum_ = numbers[start] + numbers[end]
    if x < sum_:
        end -= 1
    elif x > sum_:
        start += 1
    else:
        answer += 1
        start += 1
print(answer)


"""신입 사원"""
# 신입사원의 성적 순위를 오름차순으로 정렬
# - 서류 점수가 1등이라면 절대 떨어지지 않는다.
# - 2등은 1등과 비교했을 때 면접 점수만 비교하게 되고, 당연하게도 순위가 높아야만 통과할 수 있다.
# - 통과했다면 카운팅
for _ in range(int(input())):
    n = int(input())
    ranking = [list(map(int, input().split())) for _ in range(n)]
    ranking.sort()

    target = ranking[0][1]
    answer = 1
    for i in range(1, n):
        if ranking[i][1] < target:
            target = ranking[i][1]
            answer += 1

    print(answer)


"""시간 관리하기"""
# 작업 시간을 내림차순으로 정렬하기
# - 리스트의 두번째 값인 끝내야하는 시간으로 정렬하기 위해 람다 함수 사용
# - 가장 먼저 작업해야 하는 일 == 끝내야 하는 시간이 가장 작은 수
# - 제한 시간 == 끝내야 하는 시간이 가장 큰 수
# 제한 시간부터 작업시 필요한 시간을 빼기 == 일을 할 수 있는 마지막 시간
# - 제한 시간이 일을 끝내는 시간보다 크다면
#   - 제한 시간이 아닌 일을 마치는 시간에서 빼야 한다.
n = int(input())
working = [list(map(int, input().split())) for _ in range(n)]
working.sort(key=lambda x: x[1], reverse=True)

limit = working[0][1]
for i in range(n):
    if working[i][1] <= limit:
        limit = working[i][1] - working[i][0]
    else:
        limit -= working[i][0]

if limit < 0:
    print(-1)
else:
    print(limit)


"""저울"""
# 오름차순 정렬
# 측정할 수 없는 수를 대입 ex) 1이 아닌 2부터 시작이라면 1은 측정 불가
# 마찬가지로 3이 아닌 8을 대입 ex) 4까지는 측정 가능하고, 5는 측정할 수 없음, 6 7 8은 가능
n = int(input())
weights = sorted(list(map(int, input().split())))

answer = 1
for i in range(n):
    if answer < weights[i]:
        break
    answer += weights[i]
print(answer)


"""공주님의 정원"""
n = int(input())
flowers = []
for _ in range(n):
    date = list(map(int, input().split()))
    start = date[0] * 100 + date[1]
    end = date[2] * 100 + date[3]
    flowers.append((start, end))

flowers.sort(key=lambda x: (x[0], x[1]))

target = 301
end = 0
answer = 0
while flowers:
    if target >= 1201 or target < flowers[0][0]:
        break
    for _ in range(len(flowers)):
        if target >= flowers[0][0]:
            if end <= flowers[0][1]:
                end = flowers[0][1]
            flowers.remove(flowers[0])
        else:
            break
    target = end
    answer += 1

if target < 1201:
    print(0)
else:
    print(answer)


"""회의실 배정"""
n = int(input())
times = [tuple(map(int, input().split())) for _ in range(n)]
times.sort(key=lambda x: (x[1], x[0]))

lastEnd = 0
answer = 0
for start, end in times:
    if start >= lastEnd:
        lastEnd = end
        answer += 1

print(answer)


"""전화번호 목록"""
for _ in range(int(input())):
    n = int(input())
    numbers = [list(input().strip()) for _ in range(n)]
    numbers.sort()

    temp = False
    for i in range(n - 1):
        if numbers[i] == numbers[i + 1][: len(numbers[i])]:
            print("NO")
            temp = True
            break
    if temp == False:
        print("YES")


"""강의실"""
n = int(input())
rooms = []
for _ in range(n):
    idx, st, et = map(int, input().split())
    heapq.heappush(rooms, [st, et, idx])

target = []
fs, fe, fi = heapq.heappop(rooms)
heapq.heappush(target, fe)

while rooms:
    st, et, i = heapq.heappop(rooms)
    if target[0] <= st:
        heapq.heappop(target)
    heapq.heappush(target, et)

print(len(target))


"""과제"""
n = int(input())
reports = []
answer = [0] * 1001

for _ in range(n):
    day, value = map(int, input().split())
    reports.append([-value, day, value])

heapq.heapify(reports)

while reports:
    temp = heapq.heappop(reports)
    for i in range(temp[1], 0, -1):
        if answer[i] == 0:
            answer[i] = temp[2]
            break

print(sum(answer))


"""크리스마스 선물"""
n = int(input())

giftbox = []
for _ in range(n):
    area = list(map(int, input().split()))

    if area[0] == 0:
        if len(giftbox) == 0:
            print(-1)
        else:
            answer = -heapq.heappop(giftbox)
            print(answer)
    else:
        for i in range(area[0]):
            heapq.heappush(giftbox, -area[i + 1])


"""순회강연"""
n = int(input())

lectures = []
for _ in range(n):
    pay, day = map(int, input().split())
    lectures.append([day, pay])

lectures.sort()

heap = []
for day, pay in lectures:
    heapq.heappush(heap, pay)
    if day < len(heap):
        heapq.heappop(heap)
print(sum(heap))

# 오답, 해당 일이 아니라 해당 일 안에 강연을 하는 것...!
lectures = {}
for _ in range(int(input())):
    pay, day = map(int, input().split())
    if day in lectures:
        lectures[day].append(pay)
    else:
        lectures[day] = [pay]

lectures = sorted(lectures.items())

answer = 0
for lecture in lectures:
    answer += max(lecture[1])

print(answer)


"""중앙값 구하기"""
for _ in range(int(input())):
    n = int(input())
    nums = []
    for _ in range(n // 10 + 1):
        nums += list(map(int, input().split()))

    print(n // 2 + 1)
    for i in range(n):
        if i % 2 == 0:
            print(sorted(nums[: i + 1])[i // 2], end=" ")


"""한 줄로 서기"""
n = int(input())
leftNums = list(map(int, input().split()))
answer = [0] * n

for i in range(n):
    num = leftNums[i]
    id = i + 1
    left = 0
    for j in range(n):
        if left == num and answer[j] == 0:
            answer[j] = id
            break
        elif answer[j] == 0:
            left += 1
print(*answer)


"""ATM"""
n = int(input())
timers = sorted(list(map(int, input().split())))

sum_ = 0
for i in range(1, n + 1):
    sum_ += sum(timers[:i])

print(sum_)


"""단어 수학"""
n = int(input())
alpha = [input().strip() for _ in range(n)]

dic = {}
for i in range(n):
    for j in range(len(alpha[i])):
        if alpha[i][j] in dic:
            dic[alpha[i][j]] += 10 ** (len(alpha[i]) - j - 1)
        else:
            dic[alpha[i][j]] = 10 ** (len(alpha[i]) - j - 1)

numbers = sorted([val for val in dic.values()], reverse=True)

sum_ = 0
numCount = 9
for num in numbers:
    sum_ += numCount * num
    numCount -= 1

print(sum_)


"""뒤집기"""
coin = input()

cnt = 0
for i in range(len(coin) - 1):
    if coin[i] != coin[i + 1]:
        cnt += 1

print((cnt + 1) // 2)


"""크게 만들기"""
n, k = map(int, input().split())
numbers = input()

arr = []
for number in numbers:
    while arr and 0 < k:
        if arr[-1] < number:
            arr.pop()
            k -= 1
        else:
            break
    arr.append(number)

if k > 0:
    print("".join(arr[:-k]))
else:
    print("".join(arr))


"""센서"""
# index Error... ing...
n = int(input())
k = int(input())
sensor = sorted(list(map(int, input().split())))

gap = []
for i in range(n - 1):
    gap.append(sensor[i + 1] - sensor[i])

gap.sort(reverse=True)

for _ in range(k - 1):
    gap.pop(0)

print(sum(gap))


"""보물"""
n = int(input())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())), reverse=True)
print(sum(x * y for x, y in zip(a, b)))


"""병든 나이트"""
n, m = map(int, input().split())

if n == 1:
    print(1)
elif n == 2:
    print(min(4, (m + 1) // 2))
elif m < 7:
    print(min(4, m))
else:
    print(m - 2)


"""공항"""
gate = int(input())
planes = [int(input()) for _ in range(int(input()))]

parent = [i for i in range(gate + 1)]


def find(a):
    if a == parent[a]:
        return a
    parent[a] = find(parent[a])
    return parent[a]


def union(a, b):
    pa = find(a)
    pb = find(b)
    parent[pa] = pb


answer = 0
for plane in planes:
    temp = find(plane)
    if temp == 0:
        break
    union(temp, temp - 1)
    answer += 1

print(answer)


"""동전 0"""
n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)][::-1]

answer = 0
for i in coins:
    if k == 0:
        break
    if i > k:
        continue
    answer += k // i
    k %= i

print(answer)


"""DFS와 BFS"""
n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in graph:
    i.sort()

bfsVisited = [False] * (n + 1)
dfsVisited = [False] * (n + 1)


def DFS(v):
    dfsVisited[v] = True
    print(v, end=" ")
    for i in graph[v]:
        if not dfsVisited[i]:
            DFS(i)


def BFS(v):
    bfsVisited[v] = True
    queue = deque([v])

    while queue:
        v = queue.popleft()
        print(v, end=" ")
        for i in graph[v]:
            if not bfsVisited[i]:
                queue.append(i)
                bfsVisited[i] = True


DFS(v)
print()
BFS(v)


"""팔"""
l, r = input().split()
L, R = len(l), len(r)

if L != R:
    print(0)
else:
    answer = 0
    for i in range(L):
        if l[i] != r[i]:
            break
        else:
            if l[i] == "8":
                answer += 1

    print(answer)


"""촌수계산"""
n = int(input())
s, e = map(int, input().split())
m = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (n + 1)


def DFS(s):
    for i in graph[s]:
        if visited[i] == 0:
            visited[i] = visited[s] + 1
            DFS(i)


DFS(s)
print(visited[e]) if visited[e] > 0 else print(-1)


"""알파벳"""
R, C = map(int, input().split())

alpha = [list(map(lambda x: ord(x) - 65, input().strip())) for _ in range(R)]
delta = ((-1, 0), (0, -1), (1, 0), (0, 1))
visited = [False] * 26

visited[alpha[0][0]] = True
answer = 1


def DFS(r, c, cnt):
    global answer
    answer = max(answer, cnt)

    for dr, dc in delta:
        nr = dr + r
        nc = dc + c

        if -1 < nr < R and -1 < nc < C and not visited[alpha[nr][nc]]:
            visited[alpha[nr][nc]] = True
            DFS(nr, nc, cnt + 1)
            visited[alpha[nr][nc]] = False


DFS(0, 0, answer)
print(answer)


"""정수 a를 k로 만들기"""
a, k = map(int, input().split())
cnt = 0

while True:
    if k == a:
        print(cnt)
        break
    else:
        if k % 2 == 0 and k >= a * 2:
            k = k // 2
            cnt += 1
        else:
            k -= 1
            cnt += 1


"""토마토"""
m, n = map(int, input().split())
tomatoBox = [list(map(int, input().split())) for _ in range(n)]

delta = ((0, -1), (1, 0), (0, 1), (-1, 0))


def BFS():
    while queue:
        r, c = queue.popleft()

        for dr, dc in delta:
            nr = dr + r
            nc = dc + c

            if -1 < nr < n and -1 < nc < m and not tomatoBox[nr][nc]:
                tomatoBox[nr][nc] = tomatoBox[r][c] + 1
                queue.append((nr, nc))


queue = deque([])
for i in range(n):
    for j in range(m):
        if tomatoBox[i][j] == 1:
            queue.append((i, j))

BFS()

answer = 0
for days in tomatoBox:
    for day in days:
        if day == 0:
            print(-1)
            exit()
        answer = max(answer, day)

print(answer - 1)


"""토마토 - 3차원 탐색"""
M, N, H = map(int, input().split())
tomatoBox = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]

delta = ((0, -1, 0), (0, 0, 1), (0, 1, 0), (0, 0, -1), (-1, 0, 0), (1, 0, 0))


def BFS():
    while queue:
        h, r, c = queue.popleft()
        for dh, dr, dc in delta:
            nh = dh + h
            nr = dr + r
            nc = dc + c

            if (
                -1 < nh < H
                and -1 < nr < N
                and -1 < nc < M
                and not tomatoBox[nh][nr][nc]
            ):
                tomatoBox[nh][nr][nc] = tomatoBox[h][r][c] + 1
                queue.append((nh, nr, nc))


queue = deque()
for h in range(H):
    for i in range(N):
        for j in range(M):
            if tomatoBox[h][i][j] == 1:
                queue.append((h, i, j))


BFS()

answer = 0
for boxFloors in tomatoBox:
    for days in boxFloors:
        for day in days:
            if day == 0:
                print(-1)
                exit()
            answer = max(answer, day)

print(answer - 1)


"""깊이 우선 탐색 3"""
sys.setrecursionlimit(100_000)

n, m, s = map(int, input().split())

graph = [[] for _ in range(n + 1)]
# 그래프 배열을 입력을 받을 때 간선의 수를 반복해야 하는데 정점의 수를 반복하는 실수를 했다.
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

for i in graph:
    i.sort()

answer = [-1] * (n + 1)


def DFS(s, cnt):
    answer[s] = cnt

    for i in graph[s]:
        if answer[i] == -1:
            DFS(i, cnt + 1)


DFS(s, 0)

for i in range(1, n + 1):
    print(answer[i])


"""트리의 지름"""
n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    v1, v2, weight = map(int, input().split())
    graph[v1].append((v2, weight))
    graph[v2].append((v1, weight))

visited = [-1] * (n + 1)
visited[1] = 0


def DFS(s, wei):
    for v, w in graph[s]:
        if visited[v] == -1:
            visited[v] = w + wei
            DFS(v, w + wei)


DFS(1, 0)


maxNode = visited.index(max(visited))

visited = [-1] * (n + 1)
visited[maxNode] = 0

DFS(maxNode, 0)

print(max(visited))


"""트리의 지름"""
n = int(input())

graph = [[] for _ in range(n + 1)]
for _ in range(n):
    arr = list(map(int, input().split()))
    nodeNum = arr[0]
    idx = 1
    while arr[idx] != -1:
        v, w = arr[idx], arr[idx + 1]
        graph[nodeNum].append((v, w))
        idx += 2

visited = [-1] * (n + 1)
visited[1] = 0


def DFS(s, wei):
    for v, w in graph[s]:
        if visited[v] == -1:
            visited[v] = w + wei
            DFS(v, w + wei)


DFS(1, 0)

maxNode = visited.index(max(visited))
visited = [-1] * (n + 1)
visited[maxNode] = 0

DFS(maxNode, 0)

print(max(visited))


"""예산"""
n = int(input())
areaMoneys = list(map(int, input().split()))
money = int(input())

start, end = 0, max(areaMoneys)

answer = 0
temp = 0
while start <= end:
    limit = (start + end) // 2

    for areaMoney in areaMoneys:
        if areaMoney < limit:
            temp += areaMoney
        else:
            temp += limit

    if temp <= money:
        start = limit + 1
        answer = limit
    else:
        end = limit - 1

    temp = 0

print(answer)


"""용엑"""
n = int(input())
solution = list(map(int, input().split()))

left, right = 0, n - 1
temp = 2000000000
a, b = 0, 0

while left < right:
    check = solution[left] + solution[right]

    if abs(check) < temp:
        a, b = solution[left], solution[right]
        temp = abs(check)

    if check < 0:
        left += 1
    else:
        right -= 1

print(a, b)

# 시간초과 코드
temp = abs(solution[0] + solution[n - 1])
a, b = solution[0], solution[n - 1]

for i in range(n):
    for j in range(i + 1, n):
        if abs(solution[i] + solution[j]) <= temp:
            temp = abs(solution[i] + solution[j])
            a, b = solution[i], solution[j]
print(a, b)


"""두 수의 합"""


def binarySearch(nums, target):
    cnt, temp = 0, 200000000
    for i in range(n):
        left, right = i + 1, n - 1

        while left <= right:
            mid = (left + right) // 2
            sumNums = nums[i] + nums[mid]

            if sumNums < target:
                left = mid + 1
            else:
                right = mid - 1

            if abs(target - sumNums) < temp:
                cnt = 1
                temp = abs(target - sumNums)
            elif abs(target - sumNums) == temp:
                cnt += 1

    return cnt


for _ in range(int(input())):
    n, k = map(int, input().split())
    numbers = sorted(list(map(int, input().split())))
    print(binarySearch(numbers, k))


"""기타 레슨"""


def blurayCount(bluraySize):
    cnt = 0
    sumLesson = 0

    for i in range(n):
        if sumLesson + lessons[i] > bluraySize:
            cnt += 1
            sumLesson = 0
        sumLesson += lessons[i]

    return cnt + 1


def binarySearch(lessons, target):
    left, right = max(lessons), sum(lessons)

    while left <= right:
        mid = (left + right) // 2
        cnt = blurayCount(mid)

        if cnt > target:
            left = mid + 1
        elif cnt <= target:
            right = mid - 1

    return left


n, m = map(int, input().split())
lessons = list(map(int, input().split()))
print(binarySearch(lessons, m))


"""K번째 수"""
n = int(input())
k = int(input())

start, end = 1, k
while start <= end:
    mid = (start + end) // 2

    temp = 0
    for i in range(1, n + 1):
        temp += min(mid // i, n)

    if temp >= k:
        end = mid - 1
    else:
        start = mid + 1

print(start)

"""용돈관리"""
n, m = map(int, input().split())
todays = [int(input()) for _ in range(n)]

left, right = min(todays), sum(todays)
ans = 0

while left <= right:
    mid = (left + right) // 2

    total = mid
    cnt = 1

    for today in todays:
        if total < today:
            total = mid
            cnt += 1
        total -= today

    if cnt > m or mid < max(todays):
        left = mid + 1
    else:
        right = mid - 1
        ans = mid

print(ans)


"""연구소"""
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
answer = 0

safeZoneCnt = 0
for i in range(n):
    for j in range(m):
        if maps[i][j] == 0:
            safeZoneCnt += 1


def virus():
    global answer

    virusCnt = 0
    visited = [[0] * m for _ in range(n)]

    q = deque()
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 2:
                visited[i][j] = 1
                q.append((i, j))

    while q:
        r, c = q.popleft()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc

            if -1 < nr < n and -1 < nc < m:
                if visited[nr][nc] == 0 and maps[nr][nc] == 0:
                    visited[nr][nc] = 1
                    virusCnt += 1
                    q.append((nr, nc))

    answer = max(answer, safeZoneCnt - virusCnt - 3)


def makeWall(cnt):
    if cnt == 3:
        virus()
        return

    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                makeWall(cnt + 1)
                maps[i][j] = 0


makeWall(0)
print(answer)


"""치킨 배달"""
n, m = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(n)]

house, chickens = [], []
for i in range(n):
    for j in range(n):
        if maps[i][j] == 1:
            house.append((i + 1, j + 1))
        elif maps[i][j] == 2:
            chickens.append((i + 1, j + 1))

answer = 10e9

for chicken in combinations(chickens, m):
    totalRoad = 0
    for hr, hc in house:
        road = 10e9
        for cr, cc in chicken:
            road = min(road, (abs(hr - cr) + abs(hc - cc)))
        totalRoad += road
    answer = min(answer, totalRoad)

print(answer)


"""빗물"""
h, w = map(int, input().split())
walls = list(map(int, input().split()))

rain = 0

for i in range(1, len(walls) - 1):
    left = max(walls[:i])
    right = max(walls[i + 1 :])
    minHeight = min(left, right)

    if walls[i] < minHeight:
        rain += minHeight - walls[i]

print(rain)


"""달팽이"""


def makeSnail():
    r = c = n // 2
    step = num = 2
    board[r][c] = 1
    r -= 1
    c -= 1

    delta = ((0, 1), (1, 0), (0, -1), (-1, 0))
    direction = 0

    while True:
        for _ in range(4):
            dr, dc = delta[direction]

            for _ in range(step):
                r += dr
                c += dc
                board[r][c] = num

                if num == find:
                    ans[0], ans[1] = r + 1, c + 1
                if num == n**2:
                    return

                num += 1
            direction = (direction + 1) % 4

        step += 2
        r -= 1
        c -= 1


n = int(input())
find = int(input())
board = [[0] * n for _ in range(n)]
ans = [n // 2 + 1, n // 2 + 1]

makeSnail()

for i in board:
    print(*i)
print(*ans)


"""로봇 청소기"""
N, M = map(int, input().split())
R, C, D = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]

delta = ((-1, 0), (0, 1), (1, 0), (0, -1))
cnt = 0


def cleaningRobot(r, c, d):
    global cnt
    if not room[r][c]:
        room[r][c] = 2
        cnt += 1

    for _ in range(4):
        nd = (d + 3) % 4
        nr = r + delta[nd][0]
        nc = c + delta[nd][1]
        if room[nr][nc] == 0:
            cleaningRobot(nr, nc, nd)
            return
        d = nd

    nd = (d + 2) % 4
    nr = r + delta[nd][0]
    nc = c + delta[nd][1]
    if room[nr][nc] == 1:
        return
    cleaningRobot(nr, nc, d)


cleaningRobot(R, C, D)
print(cnt)


"""IPv6"""
ip = list(input().split(":"))

if ip.count(""):
    while len(ip) > 8:
        del ip[ip.index("")]
    while len(ip) < 8:
        ip.insert(ip.index(""), "")

for i in range(8):
    if len(ip[i]) < 4:
        ip[i] = "0" * (4 - len(ip[i])) + ip[i]

print(*ip, sep=":")


"""카드 정렬하기"""
n = int(input())
cards = []

for _ in range(n):
    heapq.heappush(cards, int(input()))

if len(cards) == 1:
    print(0)
else:
    answer = 0
    while len(cards) > 1:
        a = heapq.heappop(cards)
        b = heapq.heappop(cards)
        answer += a + b
        heapq.heappush(cards, a + b)

    print(answer)
