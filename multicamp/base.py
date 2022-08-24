'''📝 Hello world'''

print('Hello World!')


'''📝 그대로 출력하기'''

while True:
    try:
        print(input())
    except:
        break


'''📝 사칙연산'''

A, B = map(int, input().split())

print(A + B, A - B, A * B, A // B, A % B, sep='\n')


'''📝 꼬마 정민'''

A, B, C = map(int, input().split())

print(A + B + C)


'''📝 몫과 나머지 출력하기'''

for T in range(1, int(input()) + 1):
    a, b = map(int, input().split())

    print(f'#{T} {a // b} {a % b}')


'''📝 단어 길이 재기'''

print(len(input().strip()))


'''📝 최소, 최대'''

N = int(input())
numbers = list(map(int, input().split()))

print(min(numbers), max(numbers))


'''📝 두 수 비교하기'''

A, B = map(int, input().split())

if A < B:
    print('<')
elif A > B:
    print('>')
else:
    print('==')


'''📝 시험 성적'''

S = int(input())

if S >= 90:
    print('A')
elif S >= 80:
    print('B')
elif S >= 70:
    print('C')
elif S >= 60:
    print('D')
else:
    print('F')


'''📝 사분면 고르기'''

X = int(input())
Y = int(input())

if X > 0 and Y > 0:
    print(1)
elif X < 0 and Y > 0:
    print(2)
elif X < 0 and Y < 0:
    print(3)
else:
    print(4)


'''📝 합'''

S = [i for i in range(1, int(input()) + 1)]

print(sum(S))


'''📝 N 찍기'''

print(*[i for i in range(1, int(input()) + 1)], sep='\n')


'''📝 기찍 N'''

print(*sorted([i for i in range(1, int(input()) + 1)], reverse=True), sep='\n')


'''📝 별 찍기 - 1'''

print(*['*' * i for i in range(1, int(input()) + 1)], sep='\n')


'''📝 구구단'''

N = int(input())

for i in range(1, 10):
    print(f'{N} * {i} = {N * i}')


'''📝 더블더블'''

print(*[2 ** i for i in range(int(input()) + 1)])


'''📝 X보다 작은 수'''

N, X = map(int, input().split())
S = list(map(int, input().split()))

RESULT = [i for i in S if i < X]

print(*RESULT)


'''📝 홀수만 더하기'''

for T in range(1, int(input()) + 1):
    N = list(map(int, input().split()))

    S = [i for i in N if i % 2 != 0]

    print(f'#{T} {sum(S)}')


'''📝 간단한 N의 약수'''

T = int(input())

print(*[i for i in range(1, T + 1) if T % i == 0])


'''📝 음계'''

S = list(map(int, input().split()))
CHECK = [1, 2, 3, 4, 5, 6, 7, 8]

if CHECK == S:
    print('ascending')
elif CHECK == S[::-1]:
    print('descending')
else:
    print('mixed')


'''📝 유학 금지'''

S = list(input().strip())

CHECK = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']

print(*[i for i in S if i not in CHECK], sep='')


'''📝 모음이 보이지 않는 사람'''

ALPHA = ['a', 'e', 'i', 'o', 'u']
for T in range(1, int(input()) + 1):
    S = input().strip()

    for i in ALPHA:
        S = S.replace(i, '')

    print(f'#{T} {S}')


"""📝 크로아티아 알파벳"""

CROATIA = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

S = input()

for i in CROATIA:
    S = S.replace(i, '*')

print(len(S))


"""📝 뒤집힌 덧셈"""

X, Y = map(str, input().split())
X, Y = X[::-1], Y[::-1]

print(int(str(int(X) + int(Y))[::-1]))


"""📝 상수"""

X, Y = map(str, input().split())
X, Y = int(X[::-1]), int(Y[::-1])

print(X if X > Y else Y)


"""📝 숫자의 합"""

N = int(input())

print(sum(list(map(int, input()))))


"""📝 분해합"""

N = int(input())

answer = 0
for i in range(1, N + 1):
    LIST = list(map(int, str(i)))
    SUM = i + sum(LIST)

    if SUM == N:
        answer = i
        break

print(answer)


"""📝 숫자의 개수"""

A = int(input())
B = int(input())
C = int(input())

N = list(str(A * B * C))

arr = [0] * 10

for i in N:
    arr[int(i)] += 1

print(*[j for j in arr], sep='\n')


"""📝 새로운 불면증 치료법 🚨"""

for T in range(1, int(input()) + 1):
    N = int(input())

    CHECK = [0] * 10
    cnt = 0
    while True:
        if 0 not in CHECK:
            break
        else:
            cnt += 1
            S = str(N * cnt)
            for i in range(len(S)):
                CHECK[int(S[i])] = True

    print(f'#{T} {S}')


"""📝 초심자의 회문 검사"""

for T in range(1, int(input()) + 1):
    S = input().strip()

    if S == S[::-1]:
        print(f'#{T} 1')
    else:
        print(f'#{T} 0')


"""학📝 점계산"""

SCORE = {
    'A+': 4.3,
    'A0': 4.0,
    'A-': 3.7,
    'B+': 3.3,
    'B0': 3.0,
    'B-': 2.7,
    'C+': 2.3,
    'C0': 2.0,
    'C-': 1.7,
    'D+': 1.3,
    'D0': 1.0,
    'D-': 0.7,
    'F': 0.0
}

print(SCORE[input()])


"""📝 알파벳을 숫자로 변환"""

S = input()

for i in S:
    answer = ord(i) - 64

    print(answer, end=' ')


"""📝 다이얼"""

S = list(input())

ALPHA = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']

time = 0
for i in S:
    for j in ALPHA:
        if i in j:
            time += ALPHA.index(j) + 3

print(time)


"""📝 개수 세기"""

N = int(input())
L = list(map(int, input().split()))
C = int(input())

print(L.count(C))


"""📝 단어 공부"""

WORD = input().upper()
S = list(set(WORD))

CHECK = []
for i in S:
    cnt = WORD.count(i)
    CHECK.append(cnt)

MAX = max(CHECK)
if CHECK.count(MAX) >= 2:
    print('?')
else:
    print(S[CHECK.index(MAX)])


"""📝 숫자 카드 2"""

N = int(input())
CARD = list(map(int, input().split()))
M = int(input())
CHECK = list(map(int, input().split()))

dic = {}
for i in CARD:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1

for i in range(M):
    if CHECK[i] in dic:
        print(dic[CHECK[i]], end=' ')
    else:
        print(0, end=' ')


"""📝 베스트셀러"""

BOOK = {}
for i in range(int(input())):
    S = input().strip()
    if S in BOOK:
        BOOK[S] += 1
    else:
        BOOK[S] = 1

MAX = max(BOOK.values())

TITLE = [i for i in BOOK if MAX == BOOK[i]]
TITLE.sort()

print(TITLE[0])


"""📝 파일 정리"""

dic = {}
for i in range(int(input())):
    _, B = input().strip().split('.')
    if B in dic:
        dic[B] += 1
    else:
        dic[B] = 1

dic = sorted(dic.items())

for i in dic:
    print(*i)


"""📝 최빈수 구하기"""

for T in range(1, int(input()) + 1):
    N = int(input())
    SCORE = list(map(int, input().split()))

    board = [0] * 101
    for i in SCORE:
        board[i] += 1

    MAX = max(board)

    answer = 0
    for i in range(len(board)):
        if board[i] == MAX:
            if i > answer:
                answer = i

    print(f'#{T} {answer}')

# 또는

for T in range(1, int(input()) + 1):
    N = int(input())
    SCORE = list(map(int, input().split()))

    dic = {}
    for i in SCORE:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1

    MAX = max(dic.values())

    for k, v in dic.items():
        if v == MAX:
            print(f'#{T} {k}')


"""📝 회사에 있는 사람"""

dic = {}
for T in range(int(input())):
    P, C = input().split()
    dic[P] = C

names = []
for k, v in dic.items():
    if v == 'enter':
        names.append(k)
    else:
        continue

names.sort(reverse=True)
for i in names:
    print(i)

# 또는

dic = {}
for T in range(int(input())):
    P, C = input().split()

    if C == 'enter':
        dic[P] = C
    else:
        if dic[P]:
            del dic[P]

for i in sorted(dic, reverse=True):
    print(i)


"""📝 차집합"""

a, b = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = set(A - B)

print(len(C))
print(*sorted(C))


"""📝 나머지"""

answer = []
for _ in range(10):
    N = int(input())
    answer.append(N % 42)

print(len(set(answer)))


"""📝 듣보잡"""

N, M = map(int, input().split())
R = set([input().strip() for _ in range(N)])
S = set([input().strip() for _ in range(M)])
C = set(R & S)

print(len(C))
print(*sorted(C), sep='\n')


"""📝 피시방 알바"""

N = int(input())
P = set(map(int, input().split()))

if P == N:
    print(0)
else:
    print(N - len(P))


"""📝 OX퀴즈"""

for _ in range(int(input())):
    S = list(input().strip())

    total = []
    cnt = 0
    for i in S:
        if i == 'O':
            cnt += 1
            total.append(cnt)
        else:
            cnt = 0

    print(sum(total))


"""📝 오르막길"""

N = int(input())
S = list(map(int, input().split()))

start = S[0]
save = 0
high = 0

for i in S:
    if start < i:
        high += i - start
    if start >= i:
        save = max(save, high)
        high = 0

    start = i

print(max(high, save))


"""📝 슈퍼마리오"""

mushroom = [int(input()) for _ in range(10)]

score = 0
for i in range(10):
    prev = score
    score += mushroom[i]
    if score >= 100:
        under = 100 - prev
        over = score - 100
        if over <= under:
            print(score)
            break
        else:
            print(prev)
            break
else:
    print(score)

# 또는

mushroom = [int(input()) for _ in range(10)]

result = 0
score = 0
for i in mushroom:
    score += i
    if abs(score - 100) <= abs(result - 100):
        result = score

print(result)

# 또는

mushroom = [int(input()) for _ in range(10)]

v1 = 0
v2 = 0
score = 0
for i in mushroom:
    score += i
    if score > 100:
        v1 = score - 100
        v2 = 100 - (score - i)
        break

if v1 == v2:
    print(score)
elif v1 > v2:
    print(score - i)
elif v1 < v2:
    print(score)


"""📝 문자열 반복"""

for _ in range(int(input())):
    N, S = input().split()

    answer = [i * int(N) for i in S]

    print(*answer, sep='')


"""📝 카드놀이"""

A = list(map(int, input().split()))
B = list(map(int, input().split()))

a, b = 0, 0
for i in range(10):
    if A[i] > B[i]:
        a += 3
    elif A[i] < B[i]:
        b += 3
    else:
        a += 1
        b += 1

print(a, b)

if a > b:
    print('A')
elif a < b:
    print('B')
elif a == b == 10:
    print('D')
else:
    for i in range(1, 11):
        if A[-i] > B[-i]:
            print('A')
            break
        elif A[-i] < B[-i]:
            print('B')
            break
        else:
            continue


"""📝 세로읽기"""

S = [input().strip() for _ in range(5)]

for i in range(15):
    for j in range(5):
        if i < len(S[j]):
            print(S[j][i], end='')


"""📝 음양더하기"""


def solution(absolutes, signs):
    result = 0

    for i in range(len(signs)):
        if signs[i]:
            result += absolutes[i]
        else:
            result -= absolutes[i]

    return result


"""📝 나는 요리사다"""

SCORE = [sum(list(map(int, input().split()))) for _ in range(5)]
MAX = max(SCORE)

print(SCORE.index(MAX) + 1, MAX)


"""📝 덩치"""

S = [list(map(int, input().split())) for _ in range(int(input()))]

for i in S:
    RANK = 1
    for j in S:
        if i[0] < j[0] and i[1] < j[1]:
            RANK += 1

    print(RANK, end=' ')


"""📝 직사각형 네개의 합집합의 면적 구하기"""

NOTE = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            NOTE[x][y] = 1

answer = 0
for row in NOTE:
    answer += sum(row)

print(answer)


"""📝 2차원 배열의 합 🚨"""

# 시간초과코드

N, M = map(int, input().split())

ARR = [list(map(int, input().split())) for _ in range(N)]

Z = int(input())

for i in range(Z):
    i, j, x, y = map(int, input().split())

    i -= 1
    j -= 1
    x -= 1
    y -= 1

    answer = 0
    for r in range(i, x + 1):
        for c in range(j, y + 1):
            answer += ARR[r][c]

    print(answer)

# 정답코드

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

K = int(input())
dp = [[0] * (M + 1) for _ in range(N + 1)]

for i in range(1, N + 1):
    for j in range(1, M + 1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for _ in range(K):
    i, j, x, y = map(int, input().split())
    print(dp[x][y] - dp[x][j-1] - dp[i-1][y] + dp[i-1][j-1])


"""📝 블랙잭"""

N, M = map(int, input().split())

CARD = list(map(int, input().split()))

answer = 0
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            total = CARD[i] + CARD[j] + CARD[k]

            if answer < total <= M:
                answer = total
            if total == M:
                answer = total

print(answer)


"""📝 문서 검색"""

WORD = input().strip()
C = input().strip()

N = len(C)
i = 0
cnt = 0
while i < len(WORD):
    if WORD[i: i + N] == C:
        cnt += 1
        i += N
    else:
        i += 1

print(cnt)

# 또는

WORD = input().strip()
C = input().strip()

answer = WORD.split(C)

print(len(answer) - 1)

# 또는

WORD = input().strip()
C = input().strip()

answer = WORD.count(C)

print(answer)


"""📝 바이러스"""

N = int(input())
M = int(input())

JOIN = [[] for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0 for _ in range(N + 1)]


def DFS(v):
    stack = [v]
    visited[v] = 1

    while stack:
        cur = stack.pop()

        for d in JOIN[cur]:
            if not visited[d]:
                visited[d] = 1
                stack.append(d)


DFS(1)

answer = -1
for i in visited:
    if i == 1:
        answer += 1

print(answer)


"""📝 연결 요소의 개수"""

n, m = map(int, input().split())

join = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    join[v1].append(v2)
    join[v2].append(v1)

visited = [0] * (n + 1)
stack = []


def DFS(v):
    visited[v] = 1
    stack.append(v)

    while stack:
        cur = stack.pop()

        for d in join[cur]:
            if not visited[d]:
                visited[d] = 1
                stack.append(d)


visited[0] = 1
cnt = 0
for i in range(1, n + 1):
    if not visited[i]:
        DFS(i)
        cnt += 1

print(cnt)


"""📝 촌수계산"""

T = int(input())
N, M = map(int, input().split())
K = int(input())

JOIN = [[] for _ in range(T + 1)]

for _ in range(K):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0] * (T + 1)


def DFS(v):
    for i in JOIN[v]:
        if not visited[i]:
            visited[i] = visited[v] + 1
            DFS(i)


DFS(N)

if visited[M] > 0:
    print(visited[M])
else:
    print(-1)


""""그림"""


N, M = map(int, input().split())
PAINT = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(M)] for _ in range(N)]
delta = ((0, 1), (1, 0), (-1, 0), (0, -1))


def DFS(r, c):
    area = 0
    stack = []
    stack.append((r, c))

    while stack:
        pr, pc = stack.pop()

        if visited[pr][pc] == 0 and PAINT[pr][pc] == 1:
            visited[pr][pc] = 1
            area += 1

        for dr, dc in delta:
            nr = pr + dr
            nc = pc + dc

            if -1 < nr < N and -1 < nc < M:
                if visited[nr][nc] == 0 and PAINT[nr][nc] == 1:
                    stack.append((nr, nc))

    return area


result = []
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0 and PAINT[i][j] == 1:
            result.append(DFS(i, j))

print(len(result))
print(max(result)) if len(result) != 0 else print(0)
