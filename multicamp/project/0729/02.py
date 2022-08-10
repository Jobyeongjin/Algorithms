# 문자열의 거울상

t = int(input())

for tc in range(1, t + 1):
    alpha = list(input())  # 문자열 리스트

    list_ = ''
    reverse_ = alpha[::-1]  # 순서 뒤집기

    for i in reverse_:  # 반복문, 조건문을 활용하여 문자 변경
        if i == 'b':
            list_ += 'd'
        elif i == 'd':
            list_ += 'b'
        elif i == 'p':
            list_ += 'q'
        else:
            list_ += 'p'

    print(f'#{tc} {list_}')

# 또는

t = int(input())

for tc in range(1, t + 1):
    alpha = list(input())

    arr = ''
    reverse_ = alpha[::-1]
    # 딕셔너리를 선언하고 arr에 해당 값 추가
    d = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    for i in reverse_:
        arr += d.get(i)

    print(f'#{tc} {arr}')
