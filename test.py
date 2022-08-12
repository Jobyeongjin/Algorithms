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


n, m = list(map(int, input().split()))

graph = []
for _ in range(n):  # 인접 리스트 생성
    graph.append(list(map(int, input().split())))

visited = []
for _ in range(n):  # 방문 처리할 이차원 리스트 생성
    visited_list = [False] * m
    visited.append(visited_list)

dy = [-1, 0, 0, 1]  # 4방향 델타 좌표 생성
dx = [0, -1, 1, 0]

paint_cnt = 0
paint_size = []
for y in range(n):  # 이중 반복문으로 완전 탐색
    for x in range(m):
        if not visited[y][x] and graph[y][x] == 1:  # 방문 좌표가 0이면서 그림 좌표가 1이라면
            ''''
            DFS
            '''
            stack = []
            stack.append([y, x])  # 스택에 좌표 추가
            visited[y][x] = True  # 방문 처리

            paint_cnt += 1
            size = 0
            while len(stack) != 0:
                py, px = stack.pop()  # 스택에서 제거 후 변수에 저장
                size += 1  # 그림 안에 1의 개수

                for d in range(4):  # 델타 탐색
                    ny = py + dy[d]  # 다음 좌표 = 기존 좌표 + 델타 좌표
                    nx = px + dx[d]

                    if not (-1 < ny < n and -1 < nx < m):  # 범위가 벗어나지 않으면서
                        continue

                    if visited[ny][nx] == True:  # 벙문 처리를 했다면
                        continue

                    if graph[ny][nx] != 1:  # 그림 좌표가 1이 아니라면
                        continue

                    stack.append((ny, nx))  # 스택에 다음 좌표 추가
                    visited[ny][nx] = True  # 다음 좌표를 방문 처리

            paint_size.append(size)

if len(paint_size) != 0:
    print(paint_cnt)
    print(max(paint_size))
else:
    print(0)
