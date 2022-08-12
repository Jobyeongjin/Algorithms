# 창용마을 무리의 개수

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    PEOPLE = [[] for _ in range(N + 1)]  # 인접 리스트 생성
    for _ in range(M):
        v1, v2 = map(int, input().split())
        PEOPLE[v1].append(v2)
        PEOPLE[v2].append(v1)

    visited = [0] * (N + 1)  # 방문 처리할 리스트 생성

    def DFS(v):
        visited[v] = 1  # 방문 처리

        for d in PEOPLE[v]:  # 인접 정점들 순환
            if visited[d] == 0:  # 인접 정점이 방문 처리가 되지 않았다면
                DFS(d)  # DFS 실행

        return 1  # DFS가 종료되면서 리턴하는 값은 1

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:  # 방문 처리가 되어있지 않다면
            cnt += DFS(i)  # DFS 실행 뒤 카운팅

    print(f'#{tc} {cnt}')
