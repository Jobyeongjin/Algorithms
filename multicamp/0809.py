from collections import deque
from collections import Counter


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

S = input().replace('\n', '').replace(' ', '')
list_ = Counter(S).most_common()
char = []
freq = []

for c, f in list_:
    freq.append(f)

for i in range(freq.count(freq[0])):
    char.append(list_[i][0])

char.sort()

print(*char, sep='')

# 또는
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
    page = input().replace('\n', '').replace(' ', '')  # 🚨 입력에서 문제가 있었음

    for i in page:  # 입력받은 문자열 하나씩 딕셔너리에 있는지 확인
        if i in alpha:
            alpha[i] += 1  # 있다면 카운팅

answer = max(alpha.values())  # 밸류 값 중 제일 큰 값

for i in alpha:  # 딕셔너리 키 반복
    if alpha[i] == answer:  # 밸류 값이 동일하다면 출력
        print(i, end='')

# 또는

dict_ = {}  # 문자를 카운팅하는 로직
while True:
    try:
        input_ = input()
        input_ = input_.replace(' ', '')

        for char in input_:  # 문자 개수 카운팅
            if char not in dict_:
                dict_[char] = 1
            else:
                dict_[char] += 1

    except:
        break
# 딕셔너리 정렬
sorted_dict = sorted(dict_.items(), key=lambda x: (-x[1], x[0]))

max_ = sorted_dict[0][1]
for char, count in sorted_dict:
    if max_ == count:
        print(char)


# 가장 큰 금민수 🐳-
# 문제 : 4와 7로 이루어진 가장 큰 수 구하기

N = int(input())

while True:  # 입력받은 값을 거꾸로 체크하면서 4와 7의 총 개수와 숫자길이 비교
    if len(str(N)) == str(N).count('4') + str(N).count('7'):
        print(N)
        break

    N -= 1

# 또는

N = int(input())

max_ = 4  # 초기값 설정
for number in range(N + 1):
    string_number = str(number)

    for char_number in string_number:
        # 각 자릿수가 4 또는 7이 아니면 반복하지 않는다
        if not (char_number == '4' or char_number == '7'):
            break
    # for문이 정상적으로 다 완료되면 else를 실행
    # break를 만나지 않으면 실행
    else:
        max_ = int(string_number)  # 최대값 갱신

print(max_)


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

# 또는
R, C = map(int, input().split())

parking = [list(input()) for _ in range(R)]
delta = ((0, 0), (1, 0), (0, 1), (1, 1))
truck = []
crush = [0, 0, 0, 0, 0]

for r in range(R - 1):
    for c in range(C - 1):
        for x, y in delta:
            truck.append(parking[r + x][c + y])

        if truck.count('#') == 0:
            crush[truck.count('X')] += 1

        truck.clear()

print(*crush, sep='\n')

# 또는

# 우 우하 하
dr = [0, 1, 1]
dc = [1, 1, 0]
BUILDING = '#'
CAR = 'X'
VOID = '.'

R, C = list(map(int, input().split()))
parking = [list(input()) for _ in range(R)]

break_count = [0] * 5
for r in range(R):
    for c in range(C):
        cnt = 0
        # 조건 1. 기준 좌표가 빌딩이면 안된다.
        if parking[r][c] == BUILDING:
            continue
        # 조건 2. 기준 좌표가 차라면 부순 횟수 + 1
        if parking[r][c] == CAR:
            cnt += 1
        # 델타탐색
        for d in range(3):
            nr = r + dr[d]
            nc = c + dc[d]
            # 조건 1. 범위를 벗어나지 않는다.
            if not (-1 < nr < R and -1 < nc < C):
                break
            # 조건 2. 탐색 좌표에 빌딩이 있으면 안된다.
            if parking[nr][nc] == BUILDING:
                break
            # 조건 3. 탐색 좌표에 차가 있다면 키운팅
            if parking[nr][nc] == CAR:
                cnt += 1
        # break를 만나지 않고 반복문이 끝났다면
        # 혜빈이가 정상적으로 주차를 했다는 뜻
        else:
            break_count[cnt] += 1

for count in break_count:
    print(count)


# 바이러스 🐳 🚨
# 문제 : 바이러스에 걸린 컴퓨터와 인접한 컴퓨터의 개수 구하기

V = int(input())
E = int(input())

JOIN = [[] for _ in range(V + 1)]
visited = []
for _ in range(E):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)


def DFS(v):
    # 깊이우선탐색
    visited.append(v)
    for i in range(len(JOIN[v])):
        if JOIN[v][i] not in visited:
            DFS(JOIN[v][i])

    return


def BFS(v):
    # 너비우선탐색
    queue = deque()
    queue.append(v)
    visited.append(v)
    while queue:
        p = queue.popleft()
        for i in range(len(JOIN[p])):
            if JOIN[p][i] not in visited:
                queue.append(JOIN[p][i])
                visited.append(JOIN[p][i])


BFS(1)
print(visited)


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
