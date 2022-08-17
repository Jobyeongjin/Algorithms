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
