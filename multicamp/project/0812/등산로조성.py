# 등산로 조성 🚨

T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]  # 등산지도 리스트 생성
    visited = [[0] * N for _ in range(N)]  # 방문처리할 이중 리스트 생성

    dr = [0, 0, -1, 1]  # 4방위 델타 좌표
    dy = [-1, 1, 0, 0]

    high = 0
    for i in range(N):  # 이중 반복문을 이용한 완전탐색
        for j in range(N):
            if high < MAP[i][j]:  # 가장 높은 수 구하기
                high = MAP[i][j]

    def DFS(r, c):
        pass

    for i in range(N):  # 이중 반복문을 이용한 완전탐색
        for j in range(N):
            if MAP[i][j] == high:  # 지도에서 좌표가 가장 큰 값과 동일하다면
                visited[i][j] = 1  # 방문 처리
                DFS(i, j)  # DFS 실행
