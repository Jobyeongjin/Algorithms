# 1986. 지그재그 숫자 💡
# 문제 : 1부터 N까지의 숫자에서 홀수는 더하고 짝수는 뺐을 때 최종 누적된 값을 구해보자.
#       N은 1 이상 10 이하의 정수이다. (1 ≤ N ≤ 10)
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고,
#       그 아래로 각 테스트 케이스가 주어진다. 각 테스트 케이스에는 N이 주어진다.
# 출력 : 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 누적된 값을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 테스트 케이스 t
from base64 import b64decode
t = int(input())

# 테스트 케이스만큼 반복
for tc in range(1, t+1):
    # 각 케이스 n
    n = int(input())
    result = 0

    # n만큼 반복
    for i in range(1, n+1):
        # 만일 i가 짝수라면
        if i % 2 == 0:
            # 결과값에서 빼고
            result -= i
        else:
            # 홀수면 더하기
            result += i
    print(f'#{tc} {result}')


# 1284. 수도 요금 경쟁 💡
# 문제 : A사 : 1리터당 P원의 돈을 내야 한다.
#       B사 : 기본 요금이 Q원이고, 월간 사용량이 R리터 이하인 경우 요금은 기본 요금만 청구된다. 하지만 R 리터보다 많은 양을 사용한 경우 초과량에 대해 1리터당 S원의 요금을 더 내야 한다.
#       종민이의 집에서 한 달간 사용하는 수도의 양이 W리터라고 할 때, 요금이 더 저렴한 회사를 골라 그 요금을 출력하는 프로그램을 작성하라.
# 입력 : 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#       각 테스트 케이스마다 첫 번째 줄에 위 본문에서 설명한 대로 P, Q, R, S, W(1 ≤ P, Q, R, S, W ≤ 10000, 자연수)가 순서대로 공백 하나로 구분되어 주어진다.
# 출력 : 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
#       종민이가 내야 하는 수도 요금을 출력한다.

t = int(input())

for i in range(1, t+1):
    # 순서에 맞게 입력을 받기
    P, Q, R, S, W = map(int, input().split())
    # A사 한 달 요금
    a = W * P
    # B사 한 달 요금
    b = Q

    # 만약 월간 사용량이 초과한다면
    if W > R:
        # 초과한 만큼 곱해서 더해주기
        b += (W - R) * S

    # 둘 중 최소값
    result = min(a, b)

    print(f'#{i} {result}')


# 1288. 새로운 불면증 치료법 💡
# 문제 : N의 배수 번호인 양 세기
#       이전에 셌던 번호들의 각 자리수에서 0에서 9까지의 모든 숫자를 보는 것은 최소 몇 번 양을 센 시점일까?
#       5N번 양을 세면 0에서 9까지 모든 숫자를 보게 되므로 민석이는 양 세기를 멈춘다.
# 입력 : 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 N (1 ≤ N ≤ 106)이 주어진다.
# 출력 : 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고,
#       최소 몇 번 양을 세었을 때 이전에 봤던 숫자들의 자릿수에서 0에서 9까지의 모든 숫자를 보게 되는지 출력한다.
#       ( 민석이는 xN번 양을 세고 있다. )

t = int(input())

for tc in range(1, t + 1):
    a = int(input())

    # 0 ~ 9까지 인덱스로 접근
    n = [0] * 10
    # 반복 카운트
    cnt = 0

    # while 문으로 계속 반복
    while True:
        # 만일 n 안에 0이 없다면 멈춤
        if 0 not in n:
            break
        else:
            # 반복 카운트
            cnt += 1
            # 반복 횟수와 배수인 a를 곱해서 총 양을 센 수를 문자열로 결과값에 입력
            result = str(a * cnt)
            # 문자열의 길이만큼 반복
            for i in range(len(result)):
                # 결과값 안에 인덱스의 값을 숫자로 변환하고, 해당 수를 n인덱스의 값을 1로 변경
                n[int(result[i])] = 1

    print(f'#{tc} {result}')


# 또는

t = int(input())

for tc in range(1, t + 1):
    a = int(input())
    a1 = a
    # set에 계속 추가
    n = set()

    # while 반복 => set 길이가 10이 될 때까지
    while True:
        # for 반복 : 숫자를 문자로
        for i in str(a):
            n.add(i)

        if len(n) == 10:
            break
        a += a1

    print(f'#{tc} {a}')


# 1989. 초심자의 회문 검사 💡
# 문제 : "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
#       단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for tc in range(1, t + 1):
    word = input()

    result = 0
    if word == word[::-1]:
        result = 1

    print(f'#{tc} {result}')


# 1976. 시각 덧셈 💡
# 문제 : 시 분으로 이루어진 시각을 2개 입력 받아, 더한 값을 시 분으로 출력하는 프로그램을 작성하라.
#       (시각은 12시간제로 표시한다. 즉, 시가 가질 수 있는 값은 1시부터 12시이다.)
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 4개의 수가 주어진다.
#       첫 번째 수가 시를 나타내고 두 번째 수가 분을 나타낸다. 그 다음 같은 형식으로 두 번째 시각이 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고 공백을 한 칸 둔 다음, 시를 출력하고 공백을 한 칸 둔 다음 분을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for tc in range(1, t + 1):
    # 시각을 각각 변수에 입력
    h1, m1, h2, m2 = map(int, input().split())

    # 시는 시끼리, 분은 분끼리 더하기
    h = h1 + h2
    m = m1 + m2

    # 만일 시가 12보다 크다면
    if h > 12:
        # 12를 빼주고
        h -= 12

    # 만일 분이 60보다 크거나 같다면
    if m >= 60:
        # 시는 1을 더하고, 분은 60을 빼기
        h += 1
        m -= 60

    print(f'#{tc} {h} {m}')


# 1926. 간단한 369게임 💡
# 문제 : "3" "6" "9"가 들어가 있는 수를 말하지 않는대신, 박수를 친다. 이 때, 박수는 해당 숫자가 들어간 개수만큼 쳐야 한다.
#       예를 들어 숫자 35의 경우 박수 한 번, 숫자 36의 경우 박수를 두번 쳐야 한다.
#       입력으로 정수 N 이 주어졌을 때, 1~N 까지의 숫자를 게임 규칙에 맞게 출력하는 프로그램을 작성하라.
#       박수를 치는 부분은 숫자 대신, 박수 횟수에 맞게 “-“ 를 출력한다.
# 입력 : 입력으로 정수 N 이 주어진다.
# 출력 : 1 ~ N까지의 숫자를 게임 규칙에 맞게 출력한다.

t = int(input())

# 문자형 리스트 369
a = ['3', '6', '9']

for tc in range(1, t + 1):
    # 기본값을 0으로 설정
    cnt = 0

    # 문자형으로 반복하는 i
    for i in str(tc):
        # 만일 a 안에 i가 있다면
        if i in a:
            # 카운트를 1로 변경
            cnt += 1

    # 만일 카운트가 0보다 크다면
    if cnt > 0:
        # '-' 으로 변경
        tc = '-' * cnt

    # 한 줄로 공백을 두고 출력
    print(tc, end=' ')


# 1859. 백만장자 프로젝트 💡🚨
# 문제 : 다음과 같은 조건 하에서 사재기를 하여 최대한의 이득을 얻도록 도와주자.
#       1. 원재는 연속된 N일 동안의 물건의 매매가를 예측하여 알고 있다.
#       2. 당국의 감시망에 걸리지 않기 위해 하루에 최대 1만큼 구입할 수 있다.
#       3. 판매는 얼마든지 할 수 있다.
#       예를 들어 3일 동안의 매매가가 1, 2, 3 이라면 처음 두 날에 원료를 구매하여 마지막 날에 팔면 3의 이익을 얻을 수 있다.
# 입력 : 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#       각 테스트 케이스 별로 첫 줄에는 자연수 N(2 ≤ N ≤ 1,000,000)이 주어지고,
#       둘째 줄에는 각 날의 매매가를 나타내는 N개의 자연수들이 공백으로 구분되어 순서대로 주어진다.
#       각 날의 매매가는 10,000이하이다.
# 출력 : 각 테스트 케이스마다 ‘#x’(x는 테스트케이스 번호를 의미하며 1부터 시작한다)를 출력하고, 최대 이익을 출력한다.

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    # 매매가를 리스트로 받기
    price = list(map(int, input().split()))

    # 뒤로 접근
    price = price[::-1]
    max = price[0]
    result = 0

    # 들어온 케이스만큼 반복
    for i in range(1, n):
        # 만일 최고가보다 작다면
        if max > price[i]:
            # 최고가에서 매매가를 빼서 이득을 결과 값에 넣기
            result += max - price[i]
        else:
            # 최고가 업데이트
            max = price[i]

    print(f'#{tc} {result}')


# 2007. 패턴 마디의 길이 💡
# 문제 : 패턴에서 반복되는 부분을 마디라고 부른다. 문자열을 입력 받아 마디의 길이를 출력하는 프로그램을 작성하라.
#       각 문자열의 길이는 30이다. 마디의 최대 길이는 10이다.
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 길이가 30인 문자열이 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for tc in range(1, t + 1):
    # 문자열로 받기
    n = input()

    # 마디의 최대 길이는 10이니 10까지만 반복
    for i in range(1, 10):

        # 만약 i번째 문자가 i부터 i*2번째 문자가 같다면
        # KOREA로 예를들면 i번째가 5번째인 KOREA까지 왔다면 i*2는 10번째인 KOREAKOREA까지 확인
        # 그래서 슬라이싱은 i부터 i*2
        if n[:i] == n[i:i*2]:
            print(f'#{tc} {i}')
            break


# 2005. 파스칼의 삼각형 💡
# 문제 : 파스칼의 삼각형이란 아래와 같은 규칙을 따른다.
#       1. 첫 번째 줄은 항상 숫자 1이다.
#       2. 두 번째 줄부터 각 숫자들은 자신의 왼쪽과 오른쪽 위의 숫자의 합으로 구성된다.
#       N이 4일 경우, N을 입력 받아 크기 N인 파스칼의 삼각형을 출력하는 프로그램을 작성하시오.
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다. 각 테스트 케이스에는 N이 주어진다.
# 출력 : 각 줄은 '#t'로 시작하고, 다음 줄부터 파스칼의 삼각형을 출력한다.
#       삼각형 각 줄의 처음 숫자가 나오기 전까지의 빈 칸은 생략하고 숫자들 사이에는 한 칸의 빈칸을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

# 첫번째 정수 입력
n = int(input())

# 첫번째 정수만큼 반복
for tc in range(1, n + 1):
    # 두번째 정수 입력
    n = int(input())
    # temp에서 나온 값을 담을 박스
    result = []
    # 두번째 정수만큼 반복
    for i in range(n):
        # 반복할 때마다 새로운 temp 생성
        temp = []

        for j in range(i + 1):
            # 0이거나 i라면
            if j == 0 or j == i:
                # temp에 1을 추가
                temp.append(1)
            else:
                # 이전의 temp 리스트에서 구한 값을 temp에 추가 🚨
                # result[i-1]은 이전의 temp
                # [j] + [j-1]은 해당 인덱스 위치와 그 전에 위치를 더하기
                temp.append(result[i-1][j] + result[i-1][j-1])
        # 반복문에서 나온 값 temp를 result에 저장
        result.append(temp)

    print(f'#{tc}')
    # result 값을 순차적으로 출력하기 🚨
    for i in result:
        # 리스트의 모든 값들을 unpacking
        print(*i)


# 1984. 중간 평균값 구하기 💡
# 문제 : 10개의 수를 입력 받아, 최대 수와 최소 수를 제외한 나머지의 평균값을 출력하는 프로그램을 작성하라.
#       (소수점 첫째 자리에서 반올림한 정수를 출력한다.)
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에는 10개의 수가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for tc in range(1, t + 1):
    # 리스트로 접근
    n = list(map(int, input().split()))

    n.sort()
    min_ = n[0]
    max_ = n[-1]

    n.remove(min_)
    n.remove(max_)
    result = sum(n) / len(n)

    print(f'#{tc} {round(result)}')

# 또는
t = int(input())

for tc in range(1, t + 1):
    numbers = list(map(int, input().split()))

    max_, min_ = max(numbers), min(numbers)

    arr = []
    for i in numbers:
        if i == max_ or i == min_:
            i = 0
        else:
            arr.append(i)

    result = round(sum(arr) / len(arr))

    print(f'#{tc} {result}')


# 1983. 조교 성적 매기기 💡
# 문제 : 학점은 상대평가로 주어지는데, 총 10개의 평점이 있다. 학점은 학생들이 응시한 중간/기말고사 점수 결과 및 과제 점수가 반영한다.
#       10 개의 평점을 총점이 높은 순서대로 부여하는데, 각각의 평점은 같은 비율로 부여할 수 있다.
#       예를 들어, N 명의 학생이 있을 경우 N/10 명의 학생들에게 동일한 평점을 부여할 수 있다.
#       입력으로 각각의 학생들의 중간, 기말, 과제 점수가 주어지고, 학점을 알고싶은 K 번째 학생의 번호가 주어졌을 때,
#       K 번째 학생의 학점을 출력하는 프로그램을 작성하라.
# 입력 : 입력은 첫 줄에 총 테스트 케이스의 개수 T가 온다. 다음 줄부터 각 테스트 케이스가 주어진다.
#       테스트 케이스의 첫 번째 줄은 학생수 N 과, 학점을 알고싶은 학생의 번호 K 가 주어진다.
#       테스트 케이스 두 번째 줄 부터 각각의 학생이 받은 시험 및 과제 점수가 주어진다.
# 출력 : 테스트 케이스 t에 대한 결과는 “#t”을 찍고, 한 칸 띄고, 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for tc in range(1, t + 1):
    # 학생 수 n, 학점이 궁금한 학생 번호 k
    n, k = map(int, input().split())

    RANK = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    total_score = []  # 학생들의 총점 리스트
    for i in range(n):
        a, b, c = map(int, input().split())
        sum = (a * 0.35) + (b * 0.45) + (c * 0.20)
        total_score.append(sum)

    student = total_score[k - 1]
    total_score.sort(reverse=True)
    # 구하고자 하는 학생의 점수를 인덱스로 접근
    # 동일한 평점을 부여받은 10명의 학생들은 나누기
    result = total_score.index(student) // (n // 10)

    print(f'#{tc} {RANK[result]}')


# 1204. 최빈수 구하기 💡
# 문제 : 다음과 같은 수 분포가 있으면, 10, 8, 7, 2, 2, 4, 8, 8, 8, 9, 5, 5, 3
#       최빈수는 8이 된다. 최빈수를 출력하는 프로그램을 작성하여라
#       (단, 최빈수가 여러 개 일 때에는 가장 큰 점수를 출력하라).
# 입력 : 첫 번째 줄에 테스트 케이스의 수 T가 주어진다.
#       각 테스트 케이스의 첫 줄에는 테스트 케이스의 번호가 주어지고 그 다음 줄부터는 점수가 주어진다.
# 출력 : #부호와 함께 테스트 케이스의 번호를 출력하고, 공백 문자 후 테스트 케이스에 대한 답을 출력한다.

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    li = list(map(int, input().split()))
    # 1부터 100까지 점수를 체크할 리스트
    a = [0] * 101
    result = 0
    # 점수에 맞게 인덱스 추가
    for i in li:
        a[i] += 1

    # 가장 큰 수
    max_cnt = max(a)
    # 기장 많이 나온 수 찾기
    for j in range(len(a)):
        # 만일 a의 인덱스에 해당하는 값이 가장 큰 수와 같다면
        if a[j] == max_cnt:
            # 만일 결과값보다 크다면 교체
            if j > result:
                result = j

    print(f'#{tc} {result}')


# 1940. 가랏! RC카! 💡

t = int(input())

for i in range(1, t + 1):
    n = int(input())
    # 속도와 거리
    speed = 0
    distance = 0
    # i 사용하지 않기 때문에 _ 로 설정
    for _ in range(n):
        # 리스트로 접근
        command = list(map(int, input().split()))
        # 가속하면
        if command[0] == 1:
            # 가속한만큼 속도에 누적
            speed += command[1]
        # 감속하면
        elif command[0] == 2:
            # 감속한만큼 속도 감소
            if speed > command[1]:
                speed -= command[1]
            # 현재 속도가 다음 요소보다 값이 작으면 속도는 0
            else:
                speed = 0
        # 속도 값을 거리에 누적
        distance += speed

    print(f'{i} {distance}')


# 1970. 쉬운 거스름돈 💡

# 돈 리스트
coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    result = []
    # coins 를 순차적으로 비교하기
    for coin in coins:
        # 손님 돈(n)을 각 금액에 맞춰 나눈 몫(a)은 결과 값에 저장
        a = n // coin
        result.append(a)
        # 뺀 값으로 다시 반복하기
        n -= a * coin

    print(f'#{tc}')
    # 리스트를 문자열로 변환하는 join 함수 사용
    print(' '.join(list(map(str, result))))


# 1945. 간단한 소인수분해 💡
# 문제 : N=2a x 3b x 5c x 7d x 11e
#       N이 주어질 때 a, b, c, d, e 를 출력하라.

# 소인수분해 💭
# - 자연수를 소인수들의 곱으로 표현하는 것
# - 나누기를 거꾸로, 수와 몫을 소수로 나눔, 계속 반복해서 나온 소인수들을 곱하기

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    while n != 1:
        if n % 2 == 0:
            a += 1
            n = n / 2
        elif n % 3 == 0:
            b += 1
            n = n / 3
        elif n % 5 == 0:
            c += 1
            n = n / 5
        elif n % 7 == 0:
            d += 1
            n = n / 7
        elif n % 11 == 0:
            e += 1
            n = n / 11

    print(f'#{tc} {a} {b} {c} {d} {e}')


# 간단한 압축 풀기 💡
# 문제 : 원본 문서는 너비가 10인 여러 줄의 문자열로 이루어져 있다. 문자열은 마지막 줄을 제외하고 빈 공간 없이 알파벳으로 채워져 있고 마지막 줄은 왼쪽부터 채워져 있다.
#       이 문서를 압축한 문서는 알파벳과 그 알파벳의 연속된 개수로 이루어진 쌍들이 나열되어 있다. (예 : A 5    AAAAA)
#       압축된 문서를 입력 받아 원본 문서를 만드는 프로그램을 작성하시오.

t = int(input())

for tc in range(1, t + 1):
    n = int(input())

    word = ''
    for i in range(1, n + 1):
        n, m = input().split()
        word += n * int(m)

    print(f'#{tc}')

    for i in range(0, len(word), 10):  # 0부터 문자길이까지, 10칸씩 (0, 10, 20)
        print(word[i:i + 10])


# 1948. 날짜 계산기 💡
# 문제 : 월 일로 이루어진 날짜를 2개 입력 받아, 두 번째 날짜가 첫 번째 날짜의 며칠째인지 출력하는 프로그램을 작성하라.

t = int(input())

for tc in range(1, t + 1):
    m1, d1, m2, d2 = map(int, input().split())

    days = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
            7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}

    result = 0
    for i in range(m1, m2):
        if i == m1:
            result += days[i] - d1 + 1
        else:
            result += days[i]

    result += d2

    print(f'#{tc} {result}')


# 1959. 두 개의 숫자열 🚨 💡
# 문제 : 서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())
    a = list(input().split())
    b = list(input().split())

    max_value = 0
    for i in range(abs(n - m) + 1):

        value = 0
        for j in range(min(n, m)):
            if len(a) > len(b):
                value += int(a[j + i]) * int(b[j])
            elif len(a) < len(b):
                value += int(a[j]) * int(b[j + i])
            else:
                value += int(a[j]) * int(b[j])

        if value > max_value:
            max_value = value

    print(f'#{tc} {max_value}')


# 1966. 숫자를 정렬하자 💡
# 문제 : 숫자열을 오름차순으로 정렬

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    numbers = list(map(int, input().split()))

    numbers.sort()
    print(f'#{tc}', end=' ')
    print(*numbers)


# 2001. 파리 퇴치 💡
# 문제 : 해당 영역에 존재하는 파리를 촤대한 많이 잡기

t = int(input())

for tc in range(1, t + 1):
    n, m = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(n)]

    fly = []
    for i in range(n - 1):
        for j in range(n - 1):

            total = 0
            # 파리 잡기
            for x in range(m):
                for y in range(m):
                    if i + x in range(n) and j + y in range(n):
                        total += arr[i + x][j + y]

            fly.append(total)

    # 최대값 구하기
    max_ = fly[0]
    for i in fly:
        if i > max_:
            max_ = i

    print(f'#{tc} {max_}')


# 1285. 아름이의 돌 던지기 💡
# - C문제지만 파이썬으로 구현해보기
# 문제 : 최대한 0에 가까운 위치에 돌을 던지고, 0과 돌의 거리 차이와 몇 명인지를 구하기

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    stone = map(int, input().split())

    value = [abs(i) for i in stone]  # 절대값 리스트 생성
    min_ = min(value)  # 0이랑 제일 가까운 건 결국 최소값

    cnt = 0
    for i in value:  # 같은 수가 있는지 확인
        if i == min_:
            cnt += 1

    print(f'#{tc} {min_} {cnt}')


# 1928. Base64 Decoder
# 문제 : 입력으로 Base64 Encoding 된 String 이 주어졌을 때, 해당 String 을 Decoding 하여, 원문을 출력하는 프로그램을 작성

# from base64 import b64decode

t = int(input())

for tc in range(1, t + 1):
    word = input()
    answer = b64decode(word).decode('UTF-8')

    print(f'#{tc} {answer}')


# 1954. 달팽이 숫자 🚨
# 문제 : 시계방향으로 달팽이 숫자 만들기

t = int(input())
# 우 하 좌 상
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for tc in range(1, t + 1):
    n = int(input())

    snail = [[0] * n for _ in range(n)]
    # 초기 좌표 및 회전 방향 0
    x, y = 0, 0
    rotate = 0

    for i in range(1, n * n + 1):
        snail[x][y] = i  # 순차적으로 좌표 입력
        x += dx[rotate]
        y += dy[rotate]
        # 좌표가 리스트 범위 밖이거나 이미 값이 부여된 경우
        if not 0 <= x < n or not 0 <= y < n or snail[x][y] != 0:
            x -= dx[rotate]
            y -= dy[rotate]
            rotate = (rotate + 1) % 4
            x += dx[rotate]
            y += dy[rotate]

    print(f'#{tc}')

    for i in range(n):
        for j in range(n):
            print(snail[i][j], end=' ')
        print()
