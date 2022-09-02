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
