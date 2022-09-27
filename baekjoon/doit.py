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
