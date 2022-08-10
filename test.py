# 파일 불러오기
from collections import deque
from collections import Counter
import sys

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


T = int(input())
N, M = map(int, input().split())
J = int(input())

JOIN = [[] for _ in range(T + 1)]  # 인접 리스트 생성
for i in range(J):
    v1, v2 = map(int, input().split())
    JOIN[v1].append(v2)
    JOIN[v2].append(v1)

visited = [0] * (T + 1)  # 방문 여부 확인

print(JOIN)


def DFS(v):
    print(v)
    for i in JOIN[v]:  # 확인하고 싶은 수와 인접한 수 반복
        if visited[i] == 0:
            visited[i] = visited[v] + 1  # 인접 정점 = 확인 정점의 인덱스 값 + 1
            print(visited[i], visited[v])
            DFS(i)


DFS(N)  # 확인하고 싶은 수 N

if visited[M] > 0:
    print(visited[M])
else:
    print(-1)
