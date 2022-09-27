# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math
import heapq

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에


arr1 = [list(map(int, input().split())) for _ in range(5)]
arr2 = [list(map(int, input().split())) for _ in range(5)]

# answer.append(sum([x * y for x, y in zip(arr1[0], arr2[0])]))
# answer.append(sum([x * y for x, y in zip(arr1[1], arr2[1])]))
# answer.append(sum([x * y for x, y in zip(arr1[2], arr2[2])]))
# answer.append(sum([x * y for x, y in zip(arr1[3], arr2[3])]))
# answer.append(sum([x * y for x, y in zip(arr1[4], arr2[4])]))

# 1 = arr1[0][0] * arr2[0][0]
# 2 = arr1[0][1] * arr2[1][1]
# 3 = arr1[0][2] * arr2[2][2]
# 4 = arr1[0][3] * arr2[3][3]
# 5 = arr1[0][4] * arr2[4][4]

answer = []
one = []
for i in range(5):
    for j in range(5):
        if i == j:
            one.append(arr2[i][j])

cnt1 = 0
for i in range(5):
    cnt1 += arr1[0][i] * one[i]
answer.append(cnt1)

cnt2 = 0
for i in range(5):
    cnt2 += arr1[1][i] * one[i]
answer.append(cnt2)

cnt3 = 0
for i in range(5):
    cnt3 += arr1[2][i] * one[i]
answer.append(cnt3)

cnt4 = 0
for i in range(5):
    cnt4 += arr1[3][i] * one[i]
answer.append(cnt4)

cnt5 = 0
for i in range(5):
    cnt5 += arr1[4][i] * one[i]
answer.append(cnt5)

print(answer)
min_ = min(answer)
if min_ == answer[4]:
    print("Youngki")
elif min_ == answer[3]:
    print("Jinwoo")
elif min_ == answer[2]:
    print("Jungwoo")
elif min_ == answer[1]:
    print("Junsuk")
elif min_ == answer[0]:
    print("Inseo")
