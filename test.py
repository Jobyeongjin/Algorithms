# 파일 불러오기
from sys import stdin

stdin = open("input.txt", "r")

input = stdin.readline

# 문제풀이는 여기에


n = int(input())

list_ = [list(map(int, input().split())) for _ in range(n)]

score_list = [0] * n

col_list = []
for x in range(3):
    col = []
    for y in range(n):
        col.append(list_[y][x])

    col_list.append(col)

socre_list = [0] * n
for x in range(3):
    col = col_list[x]
    for y in range(n):
        score = col[y]
        if col.count(score) == 1:
            score_list[y] += score

for i in score_list:
    print(i)
