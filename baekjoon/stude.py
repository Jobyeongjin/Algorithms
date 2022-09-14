"""10870 - 피보나치 수 5"""
# 인덱스 접근
# 앞에 두자리를 더해서 리스트에 추가
# 마지막 값 출력

n = int(input())

answer = [0, 1]
for i in range(2, n + 1):
    plus = answer[i - 1] + answer[i - 2]
    answer.append(plus)

print(answer[n])


"""10250 - """


"""17413 - 단어 뒤집기 2"""
# 조건문, 반복문
# 문자열을 반복하면서 <> 구간에서는 스위칭하면서 그대로 스택에 입력
# 공백을 제외한 나머지는 반대로 입력

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


"""10973 - """


"""16935 - """
