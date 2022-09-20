from collections import deque

"""📝 팩토리얼"""
# 0이면 1, 아니라면 -1씩한 값을 곱한다.


def fac(n):
    if n == 0:  # 0이라면 1을 리턴
        return 1

    return n * fac(n - 1)  # 10 * 9(8, 7, 6, ...)


N = int(input())

print(fac(N))


# 또는

N = int(input())

answer = 1
if N > 0:
    for i in range(1, N + 1):
        answer *= i

print(answer)


"""📝 3의 배수"""
# 한 자릿수가 나올 때까지 각 자릿수를 더하는 것을 변환이라고 한다.
# 변환을 몇 번 했는지 카운팅을 하고, 변환의 마지막 값이 3의 배수인지를 확인한다.

N = input().strip()
answer = 0
while len(N) > 1:
    cnt = 0
    for i in range(len(N)):
        cnt += int(N[i])

    N = str(cnt)
    answer += 1
print(answer)

if int(N) % 3 == 0:
    print('YES')
else:
    print('NO')

# 또는


def f(n, answer):
    if len(n) > 1:
        answer += 1
        cnt = 0
        for i in n:
            cnt += int(i)
        f(str(cnt), answer)
    else:
        if int(n) % 3 == 0:
            print(answer)
            print('YES')
        else:
            print(answer)
            print('NO')


N = input()
answer = 0

f(N, answer)


"""📝 피보나치 수"""
# 0, 1부터 시작해 a와 b를 더하고, 나온 결과와 다음 수를 더하기를 n번만큼 반복한다.

N = int(input())

a, b = 0, 1
for _ in range(N):
    a, b = b, a+b

print(a)


"""📝 하노이 탑 🚨"""


def hanoi(a, b, c, n):
    if n == 1:
        print(a, c)
        return

    hanoi(a, c, b, n - 1)  # 원반을 b로 이동
    print(a, c)  # 가장 큰 원반을 c로 이동

    hanoi(b, a, c, n - 1)  # b에 있는 원반을 c로 이동


N = int(input())

print(2**N - 1)  # 하노이 탑 완성 횟수

if N <= 20:  # 20이하일 때만 실행
    hanoi(1, 2, 3, N)


"""📝 토마토"""
# 시작좌표 1을 찾아 BFS를 실행한다.
# 4방위로 다음 좌표를 탐색하면서 익지 않은 토마토라면 기준 좌표에 + 1을 더하면서 익히고, 좌표는 리스트에 저장한다.
# 그렇게 완성된 토마토 밭에 0이 있다면 -1을 출력하고, 아니라면 최대값에서 -1한 값을 출력한다.

m, n = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(n)]

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))

queue = deque([])
for i in range(n):
    for j in range(m):
        if tomato[i][j] == 1:
            queue.append([i, j])


def BFS():
    while queue:
        r, c = queue.popleft()

        for dr, dc in delta:
            nr, nc = r + dr, c + dc

            if -1 < nr < n and -1 < nc < m:
                if tomato[nr][nc] == 0:
                    tomato[nr][nc] = tomato[r][c] + 1
                    queue.append([nr, nc])


BFS()
answer = 0
for i in tomato:
    for j in i:
        if j == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(i))

print(answer - 1)


"""📝 직사각형 네개의 합집합의 면적 구하기"""
# 노트에다가 직사각형의 크기만큼 순회하면서 값을 추가하고 총합(면적) 구하기

note = [[0] * 101 for _ in range(101)]
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            note[i][j] = 1

answer = 0
for i in note:
    answer += sum(i)

print(answer)


"""📝 수 이어가기"""
# 조건에 맞는 수를 리스트에 저장하고, 최대 길이를 가진 결과 출력

n = int(input())

answer = []  # 최대 길이를 가진 변수 리스트
for i in range(1, n + 1):
    arr = [n]
    arr.append(i)  # 두번째 수 입력
    idx = 1

    while True:
        next_n = arr[idx - 1] - arr[idx]
        if next_n < 0:  # 다음 수가 음수라면 종료
            break
        arr.append(next_n)
        idx += 1

    if len(answer) < len(arr):  # 최대 길이를 가진 리스트 비교하기
        answer = arr

print(len(answer))
print(*answer)
