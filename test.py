# 파일 불러오기
from collections import deque
from collections import Counter
import sys
import math

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline


def pprint(list_):
    for row in list_:
        print(row)

# 문제풀이는 여기에


k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]

start = 1
end = max(arr)

while start <= end:
    mid = (start + end) // 2  # 중간 위치
    cnt = 0  # 랜선 수
    for i in arr:
        cnt += i // mid  # 분할된 랜선 수
    if cnt >= n:
        start = mid + 1  # 랜선 수가 목표치보다 크다면 절반에서 1을 더한 값을 시작점으로 두고 다시 시작
    else:
        end = mid - 1  # 아니라면 절반에서 1을 뺀 값을 끝점으로 정해 다시 시작

print(end)
