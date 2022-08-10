# 파일 불러오기
from audioop import reverse
from collections import deque
from collections import Counter
import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


N, M = map(int, input().split())

JOIN = [[] for _ in range(N + 1)]  # 인접 리스트 생성
for _ in range(M):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

stack = []
visited = [False] * (N + 1)  # 방문 여부 확인

# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]


def DFS(v):
    visited[v] = True  # 방문 처리
    stack.append(v)  # 스택에 추가

    while stack:  # 스택에 비어있을 때까지 반복
        cur = stack.pop()  # 스택에서 제거

        for adj in JOIN[cur]:  # 제거한 수의 인접 요소들 반복

            if not visited[adj]:  # 인접 요소가 방문 리스트에 없다면
                visited[adj] = True  # 방문 처리
                stack.append(adj)  # 스택에 추가


cnt = 0
for i in range(1, N + 1):
    if visited[i] == False:  # 방문 리스트가 비어있다면
        DFS(i)
        cnt += 1  # DFS를 종료하면서 카운팅

print(cnt)

# 1
