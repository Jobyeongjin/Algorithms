# 파일 불러오기
from collections import deque
from collections import Counter
import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


N = int(input())

TITLE = 666  # 문자형 타이틀
cnt = 0
while True:
    print(TITLE)
    if '666' in str(TITLE):
        cnt += 1

    if cnt == N:
        print(TITLE)
        break

    TITLE += 1
