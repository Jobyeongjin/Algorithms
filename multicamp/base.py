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
