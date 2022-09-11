from collections import deque

"""📝 바이러스"""

n = int(input())
m = int(input())

join = [[] for _ in range(n + 1)]
visited = [0 for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    join[v1].append(v2)
    join[v2].append(v1)


def DFS(v):
    stack = [v]
    visited[v] = 1

    while stack:
        check = stack.pop()

        for n in join[check]:
            if not visited[n]:
                visited[n] = 1
                stack.append(n)


DFS(1)

answer = 0
for i in visited:
    if i == 1:
        answer += 1

print(answer - 1)


"""📝 깊이 우선 탐색 1"""

n, m, s = map(int, input().split())

join = [[] for _ in range(n + 1)]

for _ in range(m):
    v1, v2 = map(int, input().split())
    join[v1].append(v2)
    join[v2].append(v1)

visited = [0] * (n + 1)
cnt = 1


def dfs(v):
    global cnt
    visited[v] = cnt
    join[v].sort()

    for d in join[v]:
        if visited[d] == 0:
            cnt += 1
            dfs(d)


dfs(s)

for i in visited[1:]:
    print(visited[i])


"""📝 단지번호붙이기"""

n = int(input())

graph = [list(map(int, input().strip())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

delta = ((-1, 0), (0, -1), (1, 0), (0, 1))


def dfs(r, c):
    stack = []
    stack.append((r, c))

    area = 0
    while stack:
        pr, pc = stack.pop()

        if visited[pr][pc] == 0 and graph[pr][pc] == 1:
            visited[pr][pc] = 1
            area += 1

        for dr, dc in delta:
            nr = dr + pr
            nc = dc + pc

            if -1 < nr < n and -1 < nc < n:
                if visited[nr][nc] == 0 and graph[nr][nc] == 1:
                    stack.append((nr, nc))

    return area


answer = []
for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and graph[i][j] == 1:
            answer.append(dfs(i, j))
answer.sort()

print(len(answer))
for i in answer:
    print(i)


"""📝 깊이 우선 탐색 2"""

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0 for _ in range(n + 1)]
answer = [0] * (n + 1)
cnt = 1


def DFS(v):
    global cnt
    visited[v] = 1

    answer[v] = cnt
    graph[v].sort(reverse=True)

    for i in graph[v]:
        if not visited[i]:
            cnt += 1
            DFS(i)


DFS(r)

for i in answer[1:]:
    print(i)


"""📝 너비 우선 탐색 1"""

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (n + 1)
answer = [0] * (n + 1)
cnt = 1

for i in graph:
    i.sort()


def BFS(s):
    global cnt
    visited[s] = 1
    queue = deque([s])

    while queue:
        v = queue.popleft()
        answer[v] = cnt
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = 1


BFS(r)

for i in answer[1:]:
    print(i)


"""📝 DFS와 BFS"""

n, m, v = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (n + 1)
answer = [0] * (n + 1)

for i in graph:
    i.sort()


def BFS(s):
    answer[s] = 1
    queue = deque([s])

    while queue:
        v = queue.popleft()
        print(v, end=' ')
        for i in graph[v]:
            if not answer[i]:
                queue.append(i)
                answer[i] = 1


def DFS(s):
    visited[s] = 1
    print(s, end=' ')

    for i in graph[s]:
        if not visited[i]:
            DFS(i)


DFS(v)
print()
BFS(v)


"""📝 너비 우선 탐색 2"""

n, m, r = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [0] * (n + 1)
answer = [0] * (n + 1)
cnt = 1

for i in graph:
    i.sort(reverse=True)


def BFS(s):
    global cnt
    visited[s] = 1
    q = deque([s])

    while q:
        v = q.popleft()
        answer[v] = cnt
        cnt += 1
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = 1


BFS(r)

print(*answer[1:], sep='\n')
