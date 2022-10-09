# 파일 불러오기
from collections import deque
from collections import Counter
from curses import KEY_LEFT
import sys
import math
import heapq
import operator

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)


# 문제풀이는 여기에


n = int(input())

answer = 0
cnt = 0
while True:
    if answer == n:
        break
    cnt += 1
    word = str(cnt)
    if "4" in word:
        if word.count("4") + word.count("7") == len(word):
            answer += 1
    if "7" in word:
        if word.count("7") == len(word):
            answer += 1

print(cnt)
