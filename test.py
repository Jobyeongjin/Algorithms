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


dr = [0, 1, 1]
dc = [1, 1, 0]
BUILDING = "#"
CAR = "X"
VOID = "."

R, C = list(map(int, input().split()))

list_ = []
for _ in range(R):
    # 숫자 X 문자 O
    # 공백 X
    temp_list = list(input())
    list_.append(temp_list)

break_count_list = [0] * 5

for r in range(R):
    for c in range(C):
        break_count = 0

        if list_[r][c] == BUILDING:
            continue

        if list_[r][c] == CAR:
            break_count += 1

        for d in range(3):
            next_r = r + dr[d]
            next_c = c + dc[d]

            if not (-1 < next_r < R and -1 < next_c < C):
                break

            if list_[next_r][next_c] == BUILDING:
                break

            if list_[next_r][next_c] == CAR:
                break_count += 1
        else:
            break_count_list[break_count] += 1

for count in break_count_list:
    print(count)
