import sys
sys.stdin = open('input.txt', 'r')

t = int(input())

for tc in range(1, t + 1):
    # 문자열로 받기
    n = input()

    # 마디의 최대 길이는 10이니 10까지만 반복
    for i in range(1, 10):

        # 만약 i번째 문자가 i부터 i*2번째 문자가 같다면
        # KOREA로 예를들면 i번째가 5번째인 KOREA까지 왔다면 i*2는 10번째인 KOREAKOREA까지 확인
        # 그래서 슬라이싱은 i부터 i*2
        if n[:i] == n[i:i*2]:
            print(f'#{tc} {i}')
            break
