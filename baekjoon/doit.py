import heapq
import operator

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
