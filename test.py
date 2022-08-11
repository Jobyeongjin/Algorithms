# 파일 불러오기
from audioop import reverse
from collections import deque
from collections import Counter
import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


for _ in range(3):
    num = input()
    cnt = 1  # 기본 값을 1로 설정 같은 값이 나오면 추가 하기 위함
    max_cnt = 0  # 큰 값이 들어오면 바꿔주기 위한 변수
    for i in range(len(num)-1):
        if num[i] == num[i + 1]:
            cnt += 1
        else:
            if max_cnt < cnt:
                max_cnt = cnt
        # cnt 는 다시 1로 초기
                cnt = 1

    if cnt == 8:
        print(cnt)
    elif max_cnt == 1:
        # for문이 끝나고 나서 두 값이 같으면 1출력
        print(1)
    else:
        print(max_cnt)
        # 두 값이 다르면 max_cnt 값을 출력
