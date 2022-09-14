# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math
import heapq

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


s = input()
check = 0
answer = ''
stack = ''

for i in s:
    if check == 0:
        if i == '<':
            check = 1
            stack += i
        elif i == ' ':
            stack += i
            answer += stack
            stack = ''
        else:
            stack = i + stack

    elif check == 1:
        stack += i
        if i == '>':
            check = 0
            answer += stack
            stack = ''

print(answer + stack)
