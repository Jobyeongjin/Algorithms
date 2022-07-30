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


# 6. 단어의 개수 🐳
# 문제 : 영어 대소문자와 공백으로 이루어진 문자열이 주어진다. 이 문자열에는 몇 개의 단어가 있을까? 이를 구하는 프로그램을 작성하시오. 단, 한 단어가 여러 번 등장하면 등장한 횟수만큼 모두 세어야 한다.

word = input().split()  # 하나의 문자열을 공백을 기준으로 나누기

print(len(word))  # 리스트 문자열의 길이 구하기


# 7. 상수 🐳
# 문제 : 상수는 수를 다른 사람과 다르게 거꾸로 읽는다. 예를 들어, 734와 893을 칠판에 적었다면, 상수는 이 수를 437과 398로 읽는다. 따라서, 상수는 두 수중 큰 수인 437을 큰 수라고 말할 것이다.
#       두 수가 주어졌을 때, 상수의 대답을 출력하는 프로그램을 작성하시오.

a, b = input().split()  # 문자열을 공백을 기준으로 나눠 입력

A = int(a[::-1])  # 문자열을 뒤집고 숫자형으로 변환
B = int(b[::-1])

if A > B:  # 두 수 비교
    print(A)
else:
    print(B)


# 8. 다이얼 🐳
# 문제 : 숫자 1을 걸려면 총 2초가 필요하다. 1보다 큰 수를 거는데 걸리는 시간은 이보다 더 걸리며, 한 칸 옆에 있는 숫자를 걸기 위해선 1초씩 더 걸린다.
#       상근이의 할머니는 전화 번호를 각 숫자에 해당하는 문자로 외운다. 즉, 어떤 단어를 걸 때, 각 알파벳에 해당하는 숫자를 걸면 된다. 예를 들어, UNUCIC는 868242와 같다.
#       할머니가 외운 단어가 주어졌을 때, 이 전화를 걸기 위해서 필요한 최소 시간을 구하는 프로그램을 작성하시오.

word = list(input())  # 문자열 리스트 입력

alpha = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO',
         'PQRS', 'TUV', 'WXYZ']  # 번호 순으로 정렬한 알파벳 리스트

time = 0
for i in word:  # 입력된 문자열 리스트 순회
    for j in alpha:  # 알파 리스트 순회
        if i in j:  # 두 문자 비교
            time += alpha.index(j) + 3  # 알파 리스트의 해당 인덱스로 접근하고 시간 더하기

print(time)


# 9. 크로아티아 알파벳 🐳
# 문제 : 예를 들어, ljes=njak은 크로아티아 알파벳 6개(lj, e, š, nj, a, k)로 이루어져 있다. 단어가 주어졌을 때, 몇 개의 크로아티아 알파벳으로 이루어져 있는지 출력한다.
#       dž는 무조건 하나의 알파벳으로 쓰이고, d와 ž가 분리된 것으로 보지 않는다. lj와 nj도 마찬가지이다. 위 목록에 없는 알파벳은 한 글자씩 센다.

word = input()

croatia = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatia:  # 크로아티아 문자 순회
    word = word.replace(i, '*')  # replace => 문자열을 변경하는 함수로 i를 '*' 로 변환

print(len(word))  # 총 문자열의 길이를 출력


# 10. 그룹 단어 체커 🐳
# 문제 : 예를 들면, ccazzzzbb는 c, a, z, b가 모두 연속해서 나타나고, kin도 k, i, n이 연속해서 나타나기 때문에 그룹 단어이지만, aabbbccb는 b가 떨어져서 나타나기 때문에 그룹 단어가 아니다.
#       그룹 단어의 개수를 출력하는 프로그램을 작성하시오.

t = int(input())

cnt = t
for tc in range(1, t + 1):
    word = input()

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:  # 앞 글자와 다음 글자가 같다면 넘어가기
            pass
        elif word[i] in word[i + 1:]:  # 앞 글자가 만약 다음 글자 뒤에 더 나온다면 1씩 제거
            cnt -= 1
            break

print(cnt)
