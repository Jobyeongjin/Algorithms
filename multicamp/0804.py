# 누울 자리를 찾아라 🐳
# 문제 : 연속해서 2칸 이상의 빈 칸이 누울 자리(반드시 벽이나 짐에 닿음)
# 출력 : 첫째 줄에 가로로 누울 수 있는 자리와 세로로 누울 수 있는 자리의 개수를 출력

n = int(input())

room = [list(input()) for _ in range(n)]

row = 0
for x in range(n):
    cnt = 0
    for y in range(n):
        if room[x][y] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            row += 1

col = 0
for x in range(n):
    cnt = 0
    for y in range(n):
        if room[y][x] == '.':
            cnt += 1
        else:
            cnt = 0
        if cnt == 2:
            col += 1

print(row, col)


# 직사각형 네개의 합집합의 면적 구하기 🐳
# 문제 : 좌표로 입력된 직사각형의 면적 구하기
#       (모든 x좌표와 y좌표는 1이상이고 100이하인 정수)

note = [[0 for _ in range(101)] for _ in range(101)]

for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())

    for x in range(x1, x2):
        for y in range(y1, y2):
            note[x][y] = 1

total = 0
for row in note:
    total += sum(row)

print(total)


# 박스 🚨 🐳
# 문제 : 모든 박스가 이동한 거리 구하기

N = int(input())
answer = []
for _ in range(N):
    ls = list(map(int, input().split()))
    metrix = [list(map(int, input().split())) for _ in range(ls[0])]
    array = [0] * ls[1]
    cnt = 0
    for i in metrix:
        temp = 0
        for k in i:
            if(k == 1):
                array[temp] += 1
            else:
                cnt += array[temp]
            temp += 1
    answer.append(cnt)
for i in answer:
    print(i)


# 지뢰 찾기 🐳

n = int(input())

mines = [list(input().rstrip()) for _ in range(n)]
step = [list(input().rstrip()) for _ in range(n)]
answer = [['.'] * n for _ in range(n)]
dx = [-1, -1, -1, 0, 0, 1, 1, 1]
dy = [-1, 0, 1, -1, 1, -1, 0, 1]
lose = False

for i in range(n):
    for j in range(n):
        cnt = 0
        if step[i][j] == 'x' and mines[i][j] == '.':
            for k in range(8):
                x = i + dx[k]
                y = j + dy[k]
                if x < 0 or y < 0 or x >= n or y >= n:
                    continue

                if mines[x][y] == '*':
                    cnt += 1
            answer[i][j] = cnt

        if step[i][j] == 'x' and mines[i][j] == '*':
            lose = True

if lose:
    for i in range(n):
        for j in range(n):
            if mines[i][j] == '*':
                answer[i][j] = '*'

for i in range(n):
    print(*answer[i], sep='')


# 킹, 퀸, 룩, 비숍, 나이트, 폰 🐳
# 문제 : 부족한 피스가 몇 개인지 구하기

num = list(map(int, input().split()))

piece = [1, 1, 2, 2, 2, 8]

for i in range(6):
    print(piece[i] - num[i], end=' ')


# 뜨거운 붕어빵 🐳
# 문제 : 뒤집힌 모양으로 출력하기

n, m = map(int, input().split())

for _ in range(n):
    fish = input()

    print(fish[::-1], end='\n')


# 공 🐳
# 문제 : 바뀐 컵(공) 위치 찾기

n = int(input())

cup = [1, 2, 3]
for _ in range(n):
    n, m = map(int, input().split())

    a = cup.index(n)
    b = cup.index(m)

    cup[a], cup[b] = cup[b], cup[a]

print(cup[0])


# 대표값 🐳
# 문제 : 평균값과 최빈값 구하기

nums = [int(input()) for _ in range(10)]

mean = sum(nums) // 10  # 평균

print(mean)

a = {}  # 카운팅
for num in nums:
    if num in a:
        a[num] += 1
    else:
        a[num] = 1

max_ = max(a.values())  # 밸류 값 중 가장 큰 값

for i in a:
    if a[i] == max_:
        print(i)


# N번째 큰 수 🐳
# 문제 : 배열에서 n번째 큰 수 구하기

n = int(input())

for i in range(n):
    nums = list(map(int, input().split()))

    nums.sort()
    num = nums[::-1]

    print(num[2])


# 단어 뒤집기 🐳
# 문제 : 문장의 단어를 모두 뒤집어서 출력하기

n = int(input())

for _ in range(n):
    words = list(input().split())

    reverse_ = []
    for word in words:
        reverse_.append(word[::-1])

    print(*reverse_)
