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


N = 3
for i in range(N):
    numbers = input()

    answer = 1
    cnt = 1
    for i in range(len(numbers) - 1):
        if numbers[i] == numbers[i + 1]:
            cnt += 1
            if cnt > answer:
                answer = cnt
        else:
            cnt = 1

    if answer == 0:
        print(1)
    else:
        print(answer)
