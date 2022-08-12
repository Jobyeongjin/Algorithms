# 모음이 보이지 않는 사람

T = int(input())

for tc in range(1, T + 1):
    word = input()

    a = word.replace('a', '')  # 문자열에서 모음을 하나씩 삭제 (변환)
    e = a.replace('e', '')
    i = e.replace('i', '')
    o = i.replace('o', '')
    u = o.replace('u', '')

    print(f'#{tc} {u}')


# 또는


T = int(input())
ALPHA = ['a', 'e', 'i', 'o', 'u']

for tc in range(1, T + 1):
    word = input()

    for i in word:
        if i in ALPHA:
            word = word.replace(i, '')

    print(f'#{tc} {word}')


# 또는


ALPHA = ['a', 'e', 'i', 'o', 'u']
for tc in range(1, int(input()) + 1):
    S = input()

    result = ''
    for i in S:  # 입력 문자 순회
        if i in ALPHA:  # i가 알파라면 건너뛰기
            continue

        result += i  # 나머지는 결과값에 추가

    print(f'#{tc} {result}')


# 또는


T = int(input())

for tc in range(1, T + 1):
    S = input()

    S = S.replace('a', '')
    S = S.replace('e', '')
    S = S.replace('i', '')
    S = S.replace('o', '')
    S = S.replace('u', '')

    print(f'#{tc} {S}')
