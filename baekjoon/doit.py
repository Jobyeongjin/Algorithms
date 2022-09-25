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
    print(sum_[b] - sum_[a-1])


"""구간 합 구하기 5"""
n, m = map(int, input().split())

a = [[0] * (n + 1)]
b = [[0] * (n + 1) for _ in range(n + 1)]

for _ in range(n):
    a_row = [0] + [int(i) for i in input().split()]
    a.append(a_row)

for i in range(1, n + 1):
    for j in range(1, n + 1):
        b[i][j] = b[i][j-1] + b[i-1][j] - b[i-1][j-1] + a[i][j]

for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    answer = b[x2][y2] - b[x1 - 1][y2] - b[x2][y1 - 1] + b[x1 - 1][y1 - 1]
    print(answer)
