from collections import deque

# 등산로 조성 🚨


def BFS(i, j, n, maps):
    queue = deque()
    visited = [[1] * n for _ in range(n)]  # 방문처리할 이중 리스트 생성
    graph = maps  # 기존 등산로

    dy = [0, -1, 0, 1]  # 4방위 델타 좌표
    dx = [1, 0, -1, 0]

    queue.append((i, j))  # 큐에 추가

    while queue:
        y, x = queue.popleft()  # 큐에서 제거

        if visited[y][x]:
            for k in range(4):  # 델타 탐색
                ny = y + dy[k]  # 다음 좌표 = 기존 좌표 + 델타 좌표
                nx = x + dx[k]

                if -1 < ny < n and -1 < nx < n:  # 범위를 벗어나지 않으면서
                    if graph[y][x] > graph[ny][nx]:  # 다음 좌표가 지형이 낮다면
                        # 다음 좌표 값 = 기존 좌표 값 + 1
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))

    return max(map(max, visited))  # 가장 긴 등산로를 리턴


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]  # 등산지도 리스트 생성

    HIGH = 0
    for i in range(N):  # 가장 높은 봉우리 구하기
        for j in range(N):
            if HIGH < MAP[i][j]:
                HIGH = MAP[i][j]

    LEN = []
    for a in range(N):  # 완전 탐색
        for b in range(N):
            for c in range(1, K + 1):  # 공사로 지형 낮추기
                MAP[a][b] -= c

                for d in range(N):  # 완전 탐색
                    for e in range(N):
                        if MAP[d][e] == HIGH:  # 가장 높은 봉우리를 만났다면
                            # BFS 실행하고 리턴값을 리스트에 저장
                            LEN.append(BFS(d, e, N, MAP))

                MAP[a][b] += c  # 낮춘 지형을 다시 원상복구

    print(f'#{tc} {max(LEN)}')


# 또는


def BFS(i, j, n, maps):
    queue = deque()
    # 높이가 1인 지도에서 다음 좌표에 1씩 추가하면서 가장 긴 등산로를 구한다
    visited = [[1] * (n) for _ in range(n)]
    graph = maps  # 기존 등산 지도

    dy = [0, -1, 0, 1]  # 4방위 델타 좌표
    dx = [1, 0, -1, 0]

    queue.append((i, j))  # 큐에 초기 좌표 입력

    while queue:  # 큐가 빌 때까지 반복
        y, x = queue.popleft()  # 큐에서 좌표 삭제 및 변수에 저장

        if visited[y][x]:  # 방문한 좌표라면
            for k in range(4):  # 4방위 델타 탐색
                ny = y + dy[k]  # 다음 좌표 = 기존 좌표 + 델타 좌표
                nx = x + dx[k]

                if -1 < ny < n and -1 < nx < n:  # 범위를 벗어나지 않으면서
                    if graph[y][x] > graph[ny][nx]:  # 다음 좌표가 더 낮다면
                        # 다음 좌표 = 기존 좌표 + 1
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))

    return max(map(max, visited))  # 가장 긴 등산로를 리턴


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())  # 지도의 한 변의 길이 N, 최대 공사 가능 깊이 K

    maps = []
    for _ in range(N):  # 등산로 지도인 이차원 리스트 생성
        M = list(map(int, input().split()))
        maps.append(M)

    MAX_H = max(map(max, maps))  # 가장 높은 봉우리 구하기

    LEN = []
    for a in range(N):  # 완전 탐색
        for b in range(N):
            for c in range(1, K + 1):  # 지형 공사로 높이 K만큼 낮추기
                maps[a][b] -= c

                for d in range(N):  # 완전 탐색
                    for e in range(N):
                        if maps[d][e] == MAX_H:  # 가장 높은 봉우리를 만났다면
                            # BFS 실행하고 리턴박은 결과를 리스트에 추가
                            LEN.append(BFS(d, e, N, maps))

                maps[a][b] += c  # 깎은 지형 높이를 원상복구 / 다음 BFS를 실행하기 위함

    print(f'#{tc} {max(LEN)}')


# 또는


dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def BFS(a, b):
    global answer

    q = deque()
    q.append((a, b, 1))  # 큐에 좌표와 카운팅할 숫자 추가 / 초기값

    while q:
        x, y, cnt = q.popleft()

        for i in range(4):  # 4방위 델타 탐색
            nx = x + dx[i]  # 다음 좌표 = 기존 좌표 + 델타 좌표
            ny = y + dy[i]

            if 0 <= nx < N and 0 <= ny < N:  # 범위를 벗어나지 않으면서
                if MAPS[nx][ny] < MAPS[x][y]:  # 다음 봉우리가 지형이 낮다면
                    q.append((nx, ny, cnt + 1))  # 큐에 카운팅 + 1한 좌표를 추가

        answer = max(answer, cnt)


def FIND(n, mx):
    for i in range(n):
        for j in range(n):
            if MAPS[i][j] == mx:  # 가장 높은 봉우리를 만났다면
                START.append((i, j))  # 스타트에 추가


def FIX(n, k):
    for i in range(n):  # 완전 탐색
        for j in range(n):
            for FIX in range(k + 1):  # 공사는 한번씩 진행
                MAPS[i][j] -= FIX

                for a, b in START:  # 스타트 지점을 기준으로 BFS 실행
                    BFS(a, b)

                # 지형 원상복구 -> 다음 좌표의 BFS 실행할 때는 원상복구한 지형으로 실행하기 위함
                MAPS[i][j] += FIX


for tc in range(1, int(input()) + 1):
    N, K = map(int, input().split())
    MAPS, START = [], []
    mx, answer = 0, 0

    for i in range(N):
        lst = list(map(int, input().split()))
        mx = max(mx, max(lst))  # 가장 높은 봉우리
        MAPS.append(lst)  # 등산 지도

    FIND(N, mx)
    FIX(N, K)

    print(f'#{tc} {answer}')


# 또는


delta = ((-1, 0), (1, 0), (0, -1), (0, 1))  # 델타 좌표


def DFS(r, c, limit, length):  # 좌표(r, c), 공사 가능 횟수, 현재 길이
    global MAX_L  # 함수 밖에  MAX_L 변수 불러오기

    if visited[r][c] == 1:  # 방문 여부 체크
        return

    visited[r][c] = 1  # 방문 처리

    for dr, dc in delta:  # 4방위 델타 좌표
        nr, nc = r + dr, c + dc

        if not (-1 < nr < N and -1 < nc < N):  # 범위가 벗어나지 않게
            continue

        if visited[nr][nc] == 1:  # 다음 좌표 방문 여부 체크
            continue

        if MAP[nr][nc] < MAP[r][c]:  # 다음 좌표의 지형이 낮다면
            DFS(nr, nc, limit, length + 1)  # 공사 없이 길이만 1 증가

        elif MAP[nr][nc] >= MAP[r][c] and limit > 0:  # 다음 좌표가 같거나 높다면, 공사 횟수가 남았다면
            for i in range(1, K + 1):
                MAP[nr][nc] -= i  # 정수 단위로 최대 K만큼 깎음

                if MAP[nr][nc] < MAP[r][c]:  # 깎은 높이의 지형이 낮아지면
                    # 공사 가능 횟수는 1 감소, 길이는 1 증가
                    DFS(nr, nc, limit - 1, length + 1)
                MAP[nr][nc] += i  # 다음 좌표를 위해 지형 원상복구

    MAX_L = max(MAX_L, length)  # 길이 갱신
    visited[r][c] = 0  # 끝자락에 도달하면 역순으로 되돌아가면서 방문 해제


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())
    MAP = [list(map(int, input().split())) for _ in range(N)]  # 등산로 좌표
    visited = [[0 for _ in range(N)] for _ in range(N)]  # 방문 체크 리스트
    HIGH = max(map(max, MAP))  # 가장 높은 봉우리

    MAX_L = 0
    for i in range(N):  # 완전 탐색
        for j in range(N):
            if MAP[i][j] == HIGH:  # 가장 높은 봉우리를 만난다면
                DFS(i, j, 1, 1)  # DFS 실행

    print(f'#{tc} {MAX_L}')
