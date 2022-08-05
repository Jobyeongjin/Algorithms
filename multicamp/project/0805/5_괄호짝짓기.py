import sys

sys.stdin = open("_괄호짝짓기.txt")

# 괄호 짝짓기

for tc in range(1, 11):
    n = int(input())
    bracket = input()

    stack = []
    left = ['(', '[', '{', '<']
    right = [')', ']', '}', '>']

    answer = 1
    for i in bracket:
        if i in left:
            stack.append(i)
        else:
            if left.index(stack[-1]) == right.index(i):
                stack.pop()
            else:
                answer = 0
                break

    print(f'#{tc} {answer}')
