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
arr1_r = list(map(list, zip(*arr1)))

answer = []
answer.append(sum([x * y for x, y in zip(arr1_r[0], arr2[0])]))
answer.append(sum([x * y for x, y in zip(arr1_r[1], arr2[1])]))
answer.append(sum([x * y for x, y in zip(arr1_r[2], arr2[2])]))
answer.append(sum([x * y for x, y in zip(arr1_r[3], arr2[3])]))
answer.append(sum([x * y for x, y in zip(arr1_r[4], arr2[4])]))

min_ = min(answer)
if min_ == answer[0]:
    print('Inseo')
elif min_ == answer[1]:
    print('Junsuk')
elif min_ == answer[2]:
    print('Jungwoo')
elif min_ == answer[3]:
    print('Jinwoo')
elif min_ == answer[4]:
    print('Youngki')
