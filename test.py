# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


N = int(input())

stack = []
for _ in range(N):
    S = input().split()

    if S[0] == 'push':
        stack.append(S[1])

    elif S[0] == 'pop':
        if not stack:
            print(-1)
        else:
            print(stack.pop())

    elif S[0] == 'size':
        print(len(stack))

    elif S[0] == 'empty':
        if stack:
            print(0)
        else:
            print(1)

    elif S[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)
