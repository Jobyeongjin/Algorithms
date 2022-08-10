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


t = int(input())

for tc in range(1, t + 1):
    alpha = list(input())

    arr = ''
    reverse_ = alpha[::-1]

    d = {'b': 'd', 'd': 'b', 'p': 'q', 'q': 'p'}
    for i in reverse_:
        arr += d.get(i)

    print(f'#{tc} {arr}')
