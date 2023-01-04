import heapq
import operator
from collections import deque

"""구간 합 구하기 4"""
# 더한 값을 누적하는 리스트를 만들고, 구하고자 한 구간과 구하지 않을 구간을 뺀다.

n, m = map(int, input().split())
numbers = list(map(int, input().split()))

sum_ = [0]
cnt = 0
for i in numbers:
    cnt += i
    sum_.append(cnt)

for _ in range(m):
    a, b = map(int, input().split())
    print(sum_[b] - sum_[a - 1])


"""구간 합 구하기 5"""
n, m = map(int, input().split())

a = [[0] * (n + 1)]
b = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    a_row = [0] + [int(i) for i in input().split()]
    a.append(a_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        b[i][j] = b[i][j - 1] + b[i - 1][j] - b[i - 1][j - 1] + a[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = b[x2][y2] - b[x1 - 1][y2] - b[x2][y1 - 1] + b[x1 - 1][y1 - 1]
    print(answer)


"""주몽"""
# 인덱스 정렬 후 양쪽에서 하나씩 비교하기
# 재료값보다 작으면 작은 수를 하나 올리고, 값이 크면 큰 인덱스를 내려가는 방식
# 재료값과 같다면 카운팅 후 인덱스 이동

n = int(input())
m = int(input())
arr = list(map(int, input().split()))

arr.sort()
cnt = 0
i = 0
j = n - 1

while i < j:
    if arr[i] + arr[j] < m:
        i += 1
    elif arr[i] + arr[j] > m:
        j -= 1
    else:
        cnt += 1
        i += 1
        j -= 1

print(cnt)


"""DNA 비밀번호"""
check = [0] * 4
arr = [0] * 4
secret = 0


def add(s):
    global check, arr, secret
    if s == "A":
        arr[0] += 1
        if arr[0] == check[0]:
            secret += 1
    elif s == "C":
        arr[1] += 1
        if arr[1] == check[1]:
            secret += 1
    elif s == "G":
        arr[2] += 1
        if arr[2] == check[2]:
            secret += 1
    elif s == "T":
        arr[3] += 1
        if arr[3] == check[3]:
            secret += 1


def remove(s):
    global check, arr, secret
    if s == "A":
        if arr[0] == check[0]:
            secret -= 1
        arr[0] -= 1
    elif s == "C":
        if arr[1] == check[1]:
            secret -= 1
        arr[1] -= 1
    elif s == "G":
        if arr[2] == check[2]:
            secret -= 1
        arr[2] -= 1
    elif s == "T":
        if arr[3] == check[3]:
            secret -= 1
        arr[3] -= 1


s, p = map(int, input().split())
word = list(input())
check = list(map(int, input().split()))
result = 0

for i in range(4):
    if check[i] == 0:
        secret += 1

for i in range(p):
    add(word[i])

if secret == 4:
    result += 1

for i in range(p, s):
    j = i - p
    add(word[i])
    remove(word[j])
    if secret == 4:
        result += 1

print(result)


"""스택 수열"""
# 스택에 순서대로 넣으면서 배열의 수와 같은지 확인하며 +,- 입력

n = int(input())
arr = [int(input()) for _ in range(n)]
stack = []
cnt = 1
check = True
answer = ""

for i in range(n):
    s = arr[i]
    if s >= cnt:  # 배열의 번호가 오름차순 수보다 작다면
        while s >= cnt:
            stack.append(cnt)  # 스택에 순차적으로 번호 입력하면서 + 입력
            cnt += 1
            answer += "+\n"
        stack.pop()  # 번호보다 커졌다면 - 입력
        answer += "-\n"
    else:  # 배열의 번호보다 크다면
        p = stack.pop()  # 스택에서 제거한 오름차순 수와 배열의 수를 비교
        if p > s:
            print("NO")
            check = False
            break
        else:
            answer += "-\n"

if result:
    print(answer)


"""절대값 힙"""
# 힙은 최소값 또는 최대값을 빠르게 찾을 수 있다. 느슨한 정렬 상태를 유지하고 있다.
# 파이썬의 heapq 모듈은 최소값이 우선으로 적용한다.

n = int(input())
heap = []

for _ in range(n):
    num = int(input())

    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])


"""수 정렬하기 1"""
# 두 수를 비교하면서 앞의 수가 더 크다면 템프를 이용하여 위치 변경

n = int(input())
arr = [0] * n

for i in range(n):
    arr[i] = int(input())

for i in range(n - 1):
    for j in range(n - 1 - i):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp


for i in range(n):
    print(arr[i])


"""ATM"""
n = int(input())
time = list(map(int, input().split()))
arr = [0] * n

for i in range(1, n):
    point = i
    value = time[i]

    for j in range(i - 1, -1, -1):
        if time[j] < time[i]:
            point = j + 1
            break
        if j == 0:
            point = 0
    for j in range(i, point, -1):
        time[j] = time[j - 1]
    time[point] = value

arr[0] = time[0]

for i in range(1, n):
    arr[i] = arr[i - 1] + time[i]

print(sum(arr))

# 또는
n = int(input())
time = list(map(int, input().split()))
time.sort()

answer = 0
for i in range(1, n + 1):
    answer += sum(time[0:i])

print(answer)


"""K번째 수 구하기"""
n, m = map(int, input().split())
numbers = list(map(int, input().split()))

print(sorted(numbers)[m - 1])


"""수 정렬하기 3"""
n = int(input())
m = 10001
arr = [0] * m

for i in range(n):
    arr[int(input())] += 1

for i in range(m):
    if arr[i] != 0:
        for _ in range(arr[i]):
            print(i)
print(arr)


"""연결 요소의 개수"""

n, m = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    arr[u].append(v)
    arr[v].append(u)

visited = [0] * (n + 1)


def DFS(v):
    visited[v] = 1
    for i in arr[v]:
        if not visited[i]:
            DFS(i)


cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        cnt += 1
        DFS(i)

print(cnt)


"""수강신청"""
# 딕셔너리에 값을 인덱스 기준으로 넣으면서 중복된 목록 삭제
# 값을 기준으로 정렬하기
# operator() -> 연산처리를 빠르게 처리
# itemgetter() -> 튜플 리스트 생성 (인덱스 1번을 기준으로 정렬한다)

k, l = map(int, input().split())

dic = {}
for i in range(l):
    s = input().strip()
    dic[s] = i

dics = sorted(dic.items(), key=operator.itemgetter(1))

cnt = 0
for i in dics:
    print(i[0])
    cnt += 1
    if cnt == k:
        break


"""숫자 카드"""
# 시간초과로 인해 pypy3로 진행

n = int(input())
cards = set(map(int, input().split()))
m = int(input())
check = list(map(int, input().split()))

for i in check:
    if i in cards:
        print(1, end=" ")
    else:
        print(0, end=" ")


"""동전 0"""
# 동전 리스트를 거꾸로 뒤집어서 값이 크다면 넘어간다.
# 값이 작으면 나눈 몫을 구하고, k는 나눈 나머지를 저장한다.
# k가 0이라면 종료

n, k = map(int, input().split())
coin = [int(input()) for _ in range(n)][::-1]

cnt = 0
for i in coin:
    if k == 0:
        break
    if i > k:
        continue
    cnt += k // i
    k %= i

print(cnt)


"""저울"""
# 저울을 이용하는데 무거운 것부터 올릴 수는 없으니 오름차순으로 정렬하고 누적합으로 풀이

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

cnt = 1
for i in range(n):
    if cnt < arr[i]:
        break
    cnt += arr[i]

print(cnt)


"""회의실 배정"""
# 시간을 오름차순으로 정렬 / 람다를 사용하여 우선순위 지정
# 입실이 퇴실보다 크다면 퇴실 업데이트 후 카운팅

n = int(input())
time = [list(map(int, input().split())) for _ in range(n)]
time = sorted(time, key=lambda x: (x[1], x[0]))

end = 0
cnt = 0
for s, e in time:
    if s >= end:
        end = e
        cnt += 1

print(cnt)


"""보물"""
# 최소값은 가장 큰 수와 가장 작은 수를 곱해야 함
# 정렬 후 zip() 함수를 사용하여 같은 인덱스끼리 묶어준 후 반복해서 곱하고 그 값들을 더하기

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort(reverse=True)

print(sum(x * y for x, y in zip(a, b)))


"""잃어버린 괄호"""
# 최소값이 나오게 괄호를 만드는 건 - 기호가 기준이 되고, +값은 값을 누적하기

s = input().split("-")

answer = 0
for i in s[0].split("+"):
    answer += int(i)

for i in s[1:]:
    for j in i.split("+"):
        answer -= int(j)

print(answer)


"""거스름돈 """
# 2, 5원 동전으로 최소 거스름돈 구하는 문제
# 5로 나눠지면 나눈 몫을 카운팅, 아니면 2를 빼주고 카운팅, 0보다 작으면 종료
# 나눌 수 없다면 -1을 출력하기

n = int(input())

answer = 0
while True:
    if n % 5 == 0:
        answer += n // 5
        break
    else:
        n -= 2
        answer += 1

    if n < 0:
        break

if n < 0:
    print(-1)
else:
    print(answer)


"""DFS와 BFS"""
n, m, s = map(int, input().split())

arr = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    arr[v1].append(v2)
    arr[v2].append(v1)

for i in range(n + 1):
    arr[i].sort()


def DFS(v):
    print(v, end=" ")
    visited[v] = 1

    for i in arr[v]:
        if visited[i] != 1:
            DFS(i)


visited = [0] * (n + 1)
DFS(s)


def BFS(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        p = q.popleft()
        print(p, end=" ")

        for i in arr[p]:
            if visited[i] != 1:
                visited[i] = 1
                q.append(i)


print()
visited = [0] * (n + 1)
BFS(s)


"""미로 탐색"""
n, m = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(n)]

delta = ((0, -1), (1, 0), (0, 1), (-1, 0))


def BFS(i, j):
    q = deque()
    q.append((i, j))

    while q:
        r, c = q.popleft()

        for dr, dc in delta:
            nr = r + dr
            nc = c + dc
            print(nr, nc)
            if -1 < nr < n and -1 < nc < m and arr[nr][nc] == 1:
                arr[nr][nc] = arr[r][c] + 1
                q.append((nr, nc))

    return arr[n - 1][m - 1]


print(BFS(0, 0))


"""강의실 배정"""
# 끝나는 시간과 시작 시간을 비교해서 강의실 추가
# -> 다음 강의 시작 시간이 현재 강의의 끝나는 시간보다 빠르면 동시 강의 진행
# -> 그게 아니라면 새로운 강의 시간으로 배정

n = int(input())

lecture = []
for _ in range(n):
    s, t = map(int, input().split())
    lecture.append([s, t])

lecture.sort()

heap = []
heapq.heappush(heap, lecture[0][1])
for i in range(1, n):
    if lecture[i][0] < heap[0]:
        heapq.heappush(heap, lecture[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, lecture[i][1])

print(len(heap))


# 답은 맞지만 실패 코드
n = int(input())

lecture = []
for _ in range(n):
    s, t = map(int, input().split())
    lecture.append([s, t])

lecture.sort()

e = lecture[0][1]
s = lecture[0][0]
answer = 1
for i in range(n):
    if lecture[i][1] >= s and lecture[i][0] >= e:
        s = lecture[i][0]
        e = lecture[i][1]
        answer += 1

print(answer)


"""스네이크버드"""
n, l = map(int, input().split())
apple = list(map(int, input().split()))
apple.sort()

for i in range(n):
    if l >= apple[i]:
        l += 1

print(l)


"""등수 매기기"""
n = int(input())

rank = [int(input()) for _ in range(n)]
rank.sort()

answer = 0
for i in range(1, n + 1):
    answer += abs(i - rank[i - 1])

print(answer)


"""사과 담기 게임"""
n, m = map(int, input().split())
j = int(input())

s = 1
next = m
cnt = 0

for _ in range(j):
    position = int(input())

    if s <= position and next >= position:
        continue
    elif s < position:
        cnt += position - next
        s += position - next
        next = position
    else:
        cnt += s - position
        next -= s - position
        s = position

print(cnt)


"""컵홀더"""
n = int(input())
arr = list(input())

s = 0
l = 0
for i in arr:
    if i == "S":
        s += 1
    else:
        l += 1

answer = s
if l > 0:
    answer += int(l // 2) + 1

print(answer)


"""안테나"""
n = int(input())
house = list(map(int, input().split()))
house.sort()

print(house[(n - 1) // 2])


"""캠핑"""
i = 1
while True:
    l, p, v = map(int, input().split())
    if l + p + v == 0:
        break

    answer = (v // p) * l
    answer += min((v % p), l)

    print(f"Case {i}: {answer}")
    i += 1


"""박 터뜨리기"""
n, k = map(int, input().split())

if k * (k + 1) > 2 * n:
    print(-1)
elif (n - k * (k + 1) / 2) % k == 0:
    print(k - 1)
else:
    print(k)


"""방 번호"""
s = input()

answer = [0] * 10
for i in range(len(s)):
    num = int(s[i])
    if num == 6 or num == 9:
        if answer[6] <= answer[9]:
            answer[6] += 1
        else:
            answer[9] += 1
    else:
        answer[num] += 1

print(max(answer))


"""홀수"""
numbers = [int(input()) for _ in range(7)]

arr = []
for i in numbers:
    if i % 2 != 0:
        arr.append(i)

if arr:
    print(sum(arr))
    print(min(arr))
else:
    print(-1)


"""색종이"""
n = int(input())

board = [[0] * 100 for _ in range(100)]

for _ in range(n):
    x, y = map(int, input().split())

    for i in range(y, y + 10):
        for j in range(x, x + 10):
            board[i][j] = 1

cnt = 0
for i in range(100):
    for j in range(100):
        if board[i][j]:
            cnt += 1

print(cnt)


"""점수 집계"""
n = int(input())

for _ in range(n):
    score = list(map(int, input().split()))
    score.sort()
    score.pop(0)
    score.pop(-1)
    if score[2] - score[0] >= 4:
        print("KIN")
    else:
        print(sum(score))


"""행렬 덧셈"""
# EOFE Error 발생!
# -> 리스트 안에 반복문에서 행의 수 n이 아닌 열인 m으로 제출...

n, m = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for i, j in zip(a, b):
    print(*list(x + y for x, y in zip(i, j)))


"""윷놀이"""
for _ in range(3):
    arr = list(map(int, input().split()))
    yut = arr.count(0)
    if yut == 1:
        print("A")
    elif yut == 2:
        print("B")
    elif yut == 3:
        print("C")
    elif yut == 4:
        print("D")
    else:
        print("E")


"""10부제"""
n = input().strip()
cars = list(map(str, input().split()))

cnt = 0
for i in cars:
    if i in n:
        cnt += 1

print(cnt)


"""크냐?"""
while True:
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break
    else:
        if n > m:
            print("Yes")
        elif n == m:
            print("No")
        else:
            print("No")


"""막대기"""
n = int(input())

sticks = list()
for _ in range(n):
    stick = int(input())
    sticks.append(stick)

start = sticks[-1]

cnt = 0
for i in range(len(sticks) - 1, -1, -1):
    if sticks[i] > start:
        cnt += 1
        start = sticks[i]

print(cnt + 1)


"""바닥 장식"""
n, m = map(int, input().split())
floor = [list(input().strip()) for _ in range(n)]

answer = 0
cnt = 0
for r in range(n):
    for c in range(m):
        if floor[r][c] == "-":
            cnt += 1
        elif floor[r][c] != "-" and cnt > 0:
            answer += 1
            cnt = 0
    if cnt > 0:
        answer += 1
        cnt = 0

for c in range(m):
    for r in range(n):
        if floor[r][c] == "|":
            cnt += 1
        elif floor[r][c] != "|" and cnt > 0:
            answer += 1
            cnt = 0
    if cnt > 0:
        answer += 1
        cnt = 0

print(answer)


"""괄호의 값"""
text = list(input())

stack = []
answer = 0
temp = 1

for i in range(len(text)):

    if text[i] == "(":
        stack.append(text[i])
        temp *= 2

    elif text[i] == "[":
        stack.append(text[i])
        temp *= 3

    elif text[i] == ")":
        if not stack or stack[-1] == "[":
            answer = 0
            break
        if text[i - 1] == "(":
            answer += temp
        stack.pop()
        temp //= 2

    else:
        if not stack or stack[-1] == "(":
            answer = 0
            break
        if text[i - 1] == "[":
            answer += temp
        stack.pop()
        temp //= 3

if stack:
    print(0)
else:
    print(answer)


"""숫자 정사각형"""
# 모든 좌표를 확인하면서 같은 축에 같은 수가 있다면
# 정사각형를 만들어 꼭지좌표의 수가 같은 수인지 확인
# 나머지 두 좌표가 같은 수라면 길이의 제곱값을 저장
n, m = map(int, input().split())
arr = [list(input().strip()) for _ in range(n)]

answer = []
for i in range(n):
    for j in range(m):
        spot = arr[i][j]
        for k in range(j, m):
            if arr[i][k] == spot and i + k - j < n and k < m:
                if arr[i + k - j][j] == spot and arr[i + k - j][k] == spot:
                    answer.append((k - j + 1) ** 2)

print(max(answer))
