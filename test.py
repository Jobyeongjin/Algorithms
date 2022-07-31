# 파일 불러오기
import base64
from calendar import c
from os import sep
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


# n 킬로그램 설탕 배달
# 3킬로 봉지, 5킬로 봉지
# 봉지의 최소 개수, 없으면 -1


t = int(input())

for tc in range(t):
    k = int(input())  # 층수
    n = int(input())  # 호수

    # people 리스트에 1 ~ n까지 수
    people = [i for i in range(1, n + 1)]  # 0층

    for _ in range(k):
        for j in range(1, n):
            people[j] += people[j - 1]  # 아래층 인덱스 값 더하기

    print(people[-1])
