"""📝 수 찾기"""

n = int(input())
card = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

dic = {}
for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if arr[i] in dic:
        print(1)
    else:
        print(0)


"""📝 숫자 카드 2"""

n = int(input())
card = list(map(int, input().split()))
m = int(input())
arr = list(map(int, input().split()))

dic = {}
for i in card:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(m):
    if arr[i] in dic:
        print(dic[arr[i]], end=' ')
    else:
        print(0, end=' ')


"""📝 랜선 자르기"""

k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2  # 중간 위치
    cnt = 0  # 랜선 수
    for i in arr:
        cnt += i // mid  # 분할된 랜선 수
    if cnt >= n:
        start = mid + 1  # 랜선 수가 목표치보다 크다면 절반에서 1을 더한 값을 시작점으로 두고 다시 시작
    else:
        end = mid - 1  # 아니라면 절반에서 1을 뺀 값을 끝점으로 정해 다시 시작

print(end)


"""📝 공유기 설치"""


n, c = map(int, input().split())

arr = [int(input()) for _ in range(n)]
arr.sort()

start = 1
end = arr[-1] - arr[0]
answer = 0

while start <= end:
    mid = (start + end) // 2
    old = arr[0]
    cnt = 1

    for i in range(1, len(arr)):
        if arr[i] >= old + mid:
            cnt += 1
            old = arr[i]

    if cnt >= c:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1

print(answer)
