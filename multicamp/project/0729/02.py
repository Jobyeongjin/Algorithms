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
