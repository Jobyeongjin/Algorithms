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


# 또는


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    GRAPH = [[] for _ in range(N + 1)]  # 인접 리스트 생성
    for _ in range(1, M + 1):
        u, v = map(int, input().split())
        GRAPH[u].append(v)
        GRAPH[v].append(u)

    visited = [False for _ in range(N + 1)]  # 방문을 확인할 리스트 생성

    cnt = 0
    stack = []
    for i in range(1, N + 1):
        if not visited[i]:  # 방문을 하지 않았다면
            cnt += 1  # 무리를 확인하는 카운팅
            stack.append(i)  # 스택에 추가

            while stack:  # 스택이 빌 때까지 반복
                cur = stack.pop()  # 스택에서 제거
                visited[cur] = True  # 방문 처리

                for adj in GRAPH[cur]:  # 인접 정점 순회
                    if not visited[adj]:  # 방문을 하지 않았다면
                        stack.append(adj)  # 스택에 추가

    print(f'#{tc} {cnt}')


# 또는


def DFS(start):
    visited[start] = True  # 방문 처리

    for i in graph[start]:  # 인접 정점 순회
        if not visited[i]:  # 방문하지 않았다면
            DFS(i)  # DFS 실행


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    visited = [False] * (N + 1)  # 방문을 확인할 리스트 생성

    graph = [[] for _ in range(N + 1)]  # 인접 리스트 생성
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    cnt = 0
    for i in range(1, N + 1):  # 인접 리스트의 인덱스만큼 순회
        if not visited[i]:  # 방문하지 않았다면
            DFS(i)  # DFS 실행
            cnt += 1  # 무리를 확인할 카운팅

    print(f'#{tc} {cnt}')


# 또는


def DFS(i, graph_list, visited_list, component_list):
    stack = list()
    comp = list()  # 인접 정점을 저장할 리스트
    stack.append(i)

    while stack:  # 스택이 빌 때까지 반복
        P = stack.pop()  # 스택에서 제거하면서 변수로 저장

        if not visited_list[P]:  # 방문하지 않았다면
            visited_list[P] = True  # 방문 처리
            comp.append(P)

        for n in graph_list[P]:  # 인접 정점들 순회
            if not visited_list[n]:  # 방문하지 않았다면
                stack.append(n)  # 스택에 추가

    component_list.append(comp)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 마을 사람의 수, 서로 알고 있는 관계의 수

    visited = [False for _ in range(V + 1)]  # 방문을 확인할 리스트 생성

    GRAPH = [[] for _ in range(V + 1)]  # 인접 리스트 생성
    for _ in range(E):
        v1, v2 = map(int, input().split())
        GRAPH[v1].append(v2)
        GRAPH[v2].append(v1)

    connected_component = []  # 인접 정점들끼리 묶는 리스트
    for v in range(1, V + 1):
        if not visited[v]:  # 방문하지 않았다면 DFS 실행
            DFS(v, GRAPH, visited, connected_component)

    print(f'#{tc} {len(connected_component)}')
