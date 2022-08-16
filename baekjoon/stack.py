'''괄호 '''
# 스택에 추가하면서 괄호 짝을 만나면 제거한다.

N = int(input())

for _ in range(N):
    BRACKET = input()

    LEFT = '('
    RIGHT = ')'

    L = []
    R = []
    for bk in BRACKET:
        if bk == LEFT:
            L.append(bk)

        if bk == RIGHT:
            if len(L) != 0:
                L.pop()
            else:
                R.append(bk)

    if len(L) == 0 and len(R) == 0:
        print('YES')
    else:
        print('NO')


# 또는


for _ in range(int(input())):
    S = input()

    LEFT = '('
    RIGHT = ')'
    stack = []
    for i in S:
        if i == LEFT:
            stack.append(i)
        elif i == RIGHT:
            if not stack or stack[-1] != LEFT:
                stack.append(RIGHT)
                break

            stack.pop()

    # print('YES' if not stack else 'NO') 한줄코드💡
    if not stack:
        print('YES')
    else:
        print('NO')


# 또는


def solve():
    S = input()

    LEFT = '('
    stack = []
    for i in S:
        if i == LEFT:
            stack.append(i)
        else:
            if len(stack) == 0:
                print('NO')
                return
            else:
                stack.pop()

    if len(stack) == 0:
        print('YES')
    else:
        print('NO')


N = int(input())
for _ in range(N):
    solve()


'''제로'''
# 스택에 추가하면서 0이 나오고 스택에 다른 수가 있을 경우 지워준다.

S = [int(input()) for _ in range(int(input()))]

CHECK = 0
stack = []
for i in S:
    if i != CHECK:
        stack.append(i)
    else:
        if not len(stack):
            stack.append(i)
        else:
            stack.pop()


if not len(stack):
    print(0)
else:
    print(sum(stack))


'''균형잡힌 세상'''
# 여는 괄호를 스텍에 넣으면서 닫는 괄호를 만나면 제거한다. 단, 마지막 요소와 짝이 맞을 경우만 해당하며 아니면 스택에 추가한다.

while True:
    S = input()

    if S == '.':
        break

    stack = []
    for i in S:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) and stack[-1] == '(':
                stack.pop()
            else:
                stack.append(')')
                break
        elif i == ']':
            if len(stack) and stack[-1] == '[':
                stack.pop()
            else:
                stack.append(']')
                break

    print('no' if stack else 'yes')


'''스택'''
# 조건에 맞게 조건문을 작성한다. 이렇게 하면 시간초과가 뜨는데 readline으로 하니 통과했다.

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
