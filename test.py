# 파일 불러오기
from importlib.util import find_spec
from sys import stdin
from pprint import pprint
from collections import Counter

stdin = open("input.txt", "r")

input = stdin.readline

# 문제풀이는 여기에

n = int(input())
x_num, y_num = map(int, input().split())

box_list = [list(map(int, input().split())) for _ in range(x_num)]

box = 1
space = 0
cnt = 0

for x in range(y_num):
    for y in range(x_num-1, -1, -1):
        if box_list[y][x] == box:
            while True:
                if y + 1 == y_num:
                    break
                if box_list[y + 1][x] == box:
                    break

                box_list[y][x] == box
                box_list[y + 1][x] == space
                y += 1
                cnt += 1

print(cnt)
