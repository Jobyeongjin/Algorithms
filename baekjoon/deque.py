from collections import deque

"""📝 큐 2"""
# 덱을 생성하고 조건에 맞게 조건문을 작성합니다.

n = int(input())
q = deque([])

for i in range(n):
    s = input().split()

    if s[0] == 'push':
        q.append(s[1])
    elif s[0] == 'pop':
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if q:
            print(q[-1])
        else:
            print(-1)


"""📝 카드 2"""
# 덱 리스트를 하나가 남을 때까지 반복하면서 조건에 맞게 빼고 넣습니다.

n = int(input())
q = deque([i for i in range(1, n + 1)])

while len(q) > 1:
    q.popleft()
    q.append(q.popleft())

print(q[0])


"""📝 요세푸스 문제 ()"""
# k번째 요소를 빼기 위해 k번째 앞 정수까지 반복문을 사용하여 제외하고, 그 다음은 k번째를 배열에 넣는 작업을 반복합니다.

n, k = map(int, input().split())
q = deque([i for i in range(1, n + 1)])

arr = []
while q:
    for i in range(k - 1):
        q.append(q.popleft())
    arr.append(q.popleft())

print('<', end='')
print(*arr, sep=', ', end='')
print('>')


"""📝 덱"""
# 덱을 생성하고 조건에 맞게 조건문을 작성합니다.

n = int(input())
q = deque([])

for i in range(n):
    s = input().split()

    if s[0] == 'push_front':
        q.appendleft(s[1])
    elif s[0] == 'push_back':
        q.append(s[1])
    elif s[0] == 'pop_front':
        if q:
            print(q[0])
            q.popleft()
        else:
            print(-1)
    elif s[0] == 'pop_back':
        if q:
            print(q[len(q) - 1])
            q.pop()
        else:
            print(-1)
    elif s[0] == 'size':
        print(len(q))
    elif s[0] == 'empty':
        if q:
            print(0)
        else:
            print(1)
    elif s[0] == 'front':
        if q:
            print(q[0])
        else:
            print(-1)
    elif s[0] == 'back':
        if q:
            print(q[len(q) - 1])
        else:
            print(-1)


"""📝 회전하는 큐"""
# rotate() 함수 사용해 이동할 때마다 카운팅을 하고 그 수를 출력합니다.

n, m = map(int, input().split())
check = list(map(int, input().split()))
q = deque([i for i in range(1, n + 1)])

cnt = 0
for i in check:
    while True:
        if q[0] == i:  # 덱 첫번째 요소와 동일하다면 원소 제거
            q.popleft()
            break
        else:
            if q.index(i) < len(q) // 2:  # 덱 총 길이를 반으로 나눠 어느 쪽이 가까운지 비교
                q.rotate(-1)  # 왼쪽으로 이동
                cnt += 1
            else:
                q.rotate(1)  # 오른쪽으로 이동
                cnt += 1

print(cnt)
