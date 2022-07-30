# 파일 불러오기
from os import sep
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


# a, b, v = map(int, input().split())

# day = 0
# height = 0
# while True:
#     day += 1
#     if a * day - b * (day - 1) >= v:
#         break

# print(day)


a, b, v = map(int, input().split())

goal = v - b  # 올라가야 하는 높이
going = a - b  # 하루에 올라가는 높이
if goal % going == 0:
    print(goal // going)
else:
    print(goal // going + 1)
