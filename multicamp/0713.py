# 9. 주어진 리스트가 반장 선거 투표 결과일 때 이영희의 총 득표수 구하기
# 입력 : students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
# 출력 : 4
students = ['이영희', '김철수', '이영희', '조민지', '김철수', '조민지', '이영희', '이영희']
a = '이영희'
result = 0

for i in students:  # 학생들을 순차적으로 돌리는 i
    if i == a:  # i 가 a 라면? (a는 '이영희')
        i = result  # i 는 result (0부터 시작)
        result += 1  # 1씩 추가

print(result)


# 10. 주어진 리스트 요소 중 5의 개수 구하기
# 입력 : numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
# 출력 : 3
numbers = [7, 17, 10, 5, 4, 3, 17, 5, 2, 5]
a = 5
result = 0

for i in numbers:  # 숫자들을 순차적으로 돌리는 i
    if i == a:  # i가 a라면? (a는 5로 정의)
        i = result
        result += 1  # 결과에 1씩 추가

print(result)


# 11. 2단부터 9단까지 구구단 출력하기
# 입력 : -
# 출력 : 구구단
for x in range(2, 10):  # 2부터 9까지 돌아가는 x
    for y in range(1, 10):  # 1부터 9까지 돌아가는 y
        print(x * y, end='')  # end = 값 사이 공백을 추가하며, 한 줄로 출력
    print('')


# 12. 문자열 word가 주어질 때, 해당 단어 'a'를 모두 제거한 값
# 입력 : apple
# 출력 : pple
word = 'apple'
result = word

for i in word:
    if i in 'a':  # 만일 i가 문자 'a' 라면
        result = result.replace(i, '')  # result에서 i값을 공백으로 변경

print(result)


# 13. 문자열 word가 주어질 때, 해당 단어를 역순으로 뒤집은 값
# 입력 : apple
# 출력 : elppa
word = 'apple'
result = ''  # 결과는 공백으로 설정

for i in word:  # 문자열 word를 순차적으로 돌리기
    result = i + result  # result에 순차적으로 들어옴 🚨 i + result 순서 확인

print(result)


# 예제 1. 숫자 n을 받아 세제곱한 결과를 반환하는 함수 cube를 정의하고, cube를 호출해 12의 세제곱 결과는?
# 입력 : -
# 출력 : 1728
def cube(n):  # 큐브라는 함수 정의
    a = n ** 3  #
    return a  # a 값을 내보내기


result = cube(12)  # 큐브에 12 입력하고, 나온 결과값은 result에
print(result)  # 출력


# 예제 2. 가로와 세로의 길이를 각각 a, b로 받아 사각형 넑이와 둘레를 함께 반환하는 함수 정의, 사각형의 가로는 20, 세로는 30일 때 결과는?
# 입력 : -
# 출력 : (600, 100)
def rectangle(a, b):
    x = a * b
    y = (a + b) * 2
    return x, y


result = rectangle(20, 30)
print(result)
