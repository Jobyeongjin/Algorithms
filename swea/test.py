import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(1, t + 1):
    # 문자열로 받기
    n = input()

    # 마디의 최대 길이는 10이니 10까지만 반복
    for i in range(1, 10):

        if n[:i] == n[i: i*2]:
            print(f'#{tc} {i}')
            break
