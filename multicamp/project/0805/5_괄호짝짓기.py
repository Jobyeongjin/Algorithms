import sys

sys.stdin = open("_괄호짝짓기.txt")

# 괄호 짝짓기

for tc in range(1, 11):
    n = int(input())
    bracket = input()

    stack = []
    left = ['(', '[', '{', '<']  # 여는 괄호
    right = [')', ']', '}', '>']  # 닫는 괄호

    answer = 1
    for i in bracket:
        if i in left:  # 여는 괄호라면 스택에 추가
            stack.append(i)
        else:
            # 스택 안에 있는 여는 괄호와 닫는 괄호의 인덱스가 동일하면 스택에서 제거
            if left.index(stack[-1]) == right.index(i):
                stack.pop()
            else:
                answer = 0
                break

    print(f'#{tc} {answer}')


# 또는
open_b = ['(', '[', '{', '<']
close_b = [')', ']', '}', '>']

for i in range(1, 11):
    len_ = int(input())
    bracket = list(input())  # 입력받은 괄호 리스트

    stack = []
    check = True

    for j in bracket:
        if j in open_b:  # 여는 괄호라면 스택에 저장
            stack.append(j)
        elif j in close_b:
            # 몇 번째 인덱스의 닫는 괄호인지 확인해 여는 괄호를 찾아 스택에서 pop한 값과 같은지 확인
            if stack.pop() != open_b[close_b.index(j)]:
                # 닫는 괄호와 짝이 아니면 결과를 False로 변경하고 종료
                check = False
                break

    if check == True:
        print(f'#{i} 1')
    else:
        print(f'#{i} 0')
