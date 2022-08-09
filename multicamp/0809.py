from collections import deque


def pprint(list_):
    for row in list_:
        print(row)

# 모음의 개수 🐳
# 문제 : 모음이 몇 개인지 구하기


while True:
    word = input().strip().upper()
    alpha = ['A', 'E', 'I', 'O', 'U']

    if word == '#':  # '#'은 제외
        break

    cnt = 0
    for i in word:  # 문자열 안에 해당 알파벳이 있으면 카운팅
        if i in alpha:
            cnt += 1

    print(cnt)


# 사분면 🐳
# 문제 : 각 사분면에 점이 몇 개인지 구하기

N = int(input())

Q1, Q2, Q3, Q4, AXIS = 0, 0, 0, 0, 0
for _ in range(N):
    x, y = map(int, input().split())

    if 1 <= x and 1 <= y:  # 4분면의 좌표에 해당하면 카운팅
        Q1 += 1
    elif -1 >= x and 1 <= y:
        Q2 += 1
    elif -1 >= x and -1 >= y:
        Q3 += 1
    elif 1 <= x and -1 >= y:
        Q4 += 1
    else:
        AXIS += 1

print(f'Q1: {Q1}', f'Q2: {Q2}', f'Q3: {Q3}',
      f'Q4: {Q4}', f'AXIS: {AXIS}', sep='\n')


# 대표값2 🐳
# 문제 : 평균과 중앙값 구하기

numbers = [int(input().strip()) for _ in range(5)]
numbers.sort()

avg = sum(numbers) // 5

print(avg)  # 평균
print(numbers[2])  # 중앙값

# 값은 동일하지만 에러
numbers = [int(input().strip()) for _ in range(5)]
numbers.sort()

avg = sum(numbers) // 5

print(avg)

queue = deque(numbers)
while True:
    queue.pop()
    queue.popleft()
    if len(queue) == 1:
        break

print(*queue)


# 가장 많은 글자 🐳 🚨
# 문제 : 문장에서 가장 많이 나오는 글자 찾기

# 값은 동일하지만 실패
alpha = {
    'a': 0,
    'b': 0,
    'c': 0,
    'd': 0,
    'e': 0,
    'f': 0,
    'g': 0,
    'h': 0,
    'i': 0,
    'j': 0,
    'k': 0,
    'l': 0,
    'm': 0,
    'n': 0,
    'o': 0,
    'p': 0,
    'q': 0,
    'r': 0,
    's': 0,
    't': 0,
    'u': 0,
    'v': 0,
    'w': 0,
    'x': 0,
    'y': 0,
    'z': 0
}

for _ in range(14):
    page = input().strip()

    for i in page:  # 입력받은 문자열 하나씩 딕셔너리에 있는지 확인
        if i in alpha:
            alpha[i] += 1  # 있다면 카운팅

answer = max(alpha.values())  # 밸류 값 중 제일 큰 값

for i in alpha:  # 딕셔너리 키 반복
    if alpha[i] == answer:  # 밸류 값이 동일하다면 출력
        print(i, end='')


# 가장 큰 금민수 🐳-
# 문제 : 4와 7로 이루어진 가장 큰 수 구하기

N = int(input())

while True:  # 입력받은 값을 거꾸로 체크하면서 4와 7의 총 개수와 숫자길이 비교
    if len(str(N)) == str(N).count('4') + str(N).count('7'):
        print(N)
        break

    N -= 1


# 무방향 그래프 표현하기 🐳
# 그래프 입력이 주어질 때 무방향 그래프를 인접 행렬과 인접 리스트로 표현하기

N, M = map(int, input().split())

# 인접 행렬
matrix = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = 1
    matrix[y][x] = 1

pprint(matrix)

# 인접 리스트
graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

print(graph)


# 유방향 그래프 표현하기 🐳
# 문제 : 그래프 입력이 주어질 때 유방향 그래프를 인접 행렬과 인접 리스트로 표현하기

N, M = map(int, input().split())

# 인접 행렬
matrix = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    x, y = map(int, input().split())
    matrix[x][y] = 1

pprint(matrix)

# 인접 리스트
graph = [[] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].append(v)

print(graph)


# 몬스터 트럭 🐳
# 문제 : 혜빈이 차의 온전한 주차 공간과 주차 공간을 사용하는데 부숴야 하는 차의 개수 구하기

R, C = map(int, input().split())

parking = [list(input().strip()) for _ in range(R)]

all, one, two, three, four = 0, 0, 0, 0, 0
for i in range(R - 1):  # 인덱스 벗어나지 않게 설정
    for j in range(C - 1):

        arr = []
        for x in range(2):  # 혜빈이의 차 크기
            for y in range(2):
                arr.append(parking[i + x][j + y])

        if '#' in arr:  # '#'은 건너뛰기
            continue

        if arr.count('.') == 4:  # 리스트 안에 주차공간을 확인하해서 카운팅
            all += 1
        elif arr.count('X') == 4:
            four += 1
        elif arr.count('X') == 3:
            three += 1
        elif arr.count('X') == 2:
            two += 1
        elif arr.count('X') == 1:
            one += 1

print(all, one, two, three, four, sep='\n')


# 바이러스 🐳 🚨
# 문제 : 바이러스에 걸린 컴퓨터와 인접한 컴퓨터의 개수 구하기


# 값은 동일하지만 실패
COM = int(input())
N = int(input())

JOIN = [[] for _ in range(COM + 1)]
# 인접 리스트 생성
for _ in range(N):
    a, b = map(int, input().split())
    JOIN[a].append(b)
    JOIN[b].append(a)

virus = []
for i in JOIN:
    if i.count(1):  # 1이 있는 리스트만 추가
        virus.append(i)

cnt = 0
for i in virus:  # 바이러스 넘버를 확인
    for j in i:
        if j == 1:  # 1은 패스
            continue
        else:
            cnt += 1  # 나머지 수만 카운팅

print(cnt)
