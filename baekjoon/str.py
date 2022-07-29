# 1. 아스키코드 🐳
# 문제 : 알파벳 소문자, 대문자, 숫자 0-9중 하나가 주어졌을 때, 주어진 글자의 아스키 코드값을 출력하는 프로그램을 작성하시오.

a = input()

print(ord(a))  # 문자열 => 아스키코드


# 2. 숫자의 합 🐳
# 문제 : N개의 숫자가 공백 없이 쓰여있다. 이 숫자를 모두 합해서 출력하는 프로그램을 작성하시오.

n = int(input())
m = list(input())

sum_ = 0
for i in m:
    sum_ += int(i)

print(sum_)


# 3. 알파벳 찾기 🐳
# 문제 : 알파벳 소문자로만 이루어진 단어 S가 주어진다. 각각의 알파벳에 대해서, 단어에 포함되어 있는 경우에는 처음 등장하는 위치를, 포함되어 있지 않은 경우에는 -1을 출력하는 프로그램을 작성하시오.

s = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'

for i in alpha:  # 문자열 알파를 순회
    if i in s:  # 인풋 값에 알파를 확인하여 해당 위치를 출력
        print(s.index(i), end=' ')
    else:
        print(-1, end=' ')


# 4. 문자열 반복 🐳
# 문제 : 문자열 S를 입력받은 후에, 각 문자를 R번 반복해 새 문자열 P를 만든 후 출력하는 프로그램을 작성하시오. 즉, 첫 번째 문자를 R번 반복하고, 두 번째 문자를 R번 반복하는 식으로 P를 만들면 된다.

t = int(input())

for tc in range(1, t + 1):
    num, word = input().split()

    result = ''
    for i in word:  # 입력받은 문자를 반복
        result += int(num) * i  # 입력받은 숫자를 곱해서 결과값에 저장

    print(result)


# 5. 단어 공부 🐳
# 문제 : 알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.

alpha = input().upper()
alpha_set = list(set(alpha))  # 중복 제거

cnt_ = []
for i in alpha_set:
    cnt = alpha.count(i)  # 입력받은 문자의 개수 세기
    cnt_.append(cnt)

max_ = max(cnt_)  # 가장 큰 값
if cnt_.count(max_) >= 2:  # 가장 큰 값이 2 이상이라면
    print('?')
else:
    print(alpha_set[cnt_.index(max_)])  # 가장 큰 값의 위치를 찾아 출력
