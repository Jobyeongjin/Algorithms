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
