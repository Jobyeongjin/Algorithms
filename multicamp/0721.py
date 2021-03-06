# 1288. 새로운 불면증 치료법
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


# 1989. 초심자의 회문 검사
# 문제 : "level" 과 같이 거꾸로 읽어도 제대로 읽은 것과 같은 문장이나 낱말을 회문(回文, palindrome)이라 한다.
#       단어를 입력 받아 회문이면 1을 출력하고, 아니라면 0을 출력하는 프로그램을 작성하라.
# 입력 : 가장 첫 줄에는 테스트 케이스의 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어진다.
#       각 테스트 케이스의 첫 번째 줄에 하나의 단어가 주어진다.
# 출력 : 출력의 각 줄은 '#t'로 시작하고, 공백을 한 칸 둔 다음 정답을 출력한다.
#       (t는 테스트 케이스의 번호를 의미하며 1부터 시작한다.)

t = int(input())

for tc in range(1, t + 1):
    # 문자열인 a
    a = input()

    # 만일 a랑 거꾸로 한 a가 같다면
    if a == a[::-1]:
        # 결과는 1
        result = 1
    # else를 안쓰고 결과값을 애초에 0으로 설정할 수도 있다!
    else:
        # 그게 아니라면 0
        result = 0

    print(f'#{tc} {result}')


# 1976. 시각 덧셈
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


# 1926. 간단한 369게임
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
