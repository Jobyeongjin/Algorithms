# 파일 불러오기
from collections import deque
import sys
from pprint import pprint
from collections import Counter

sys.stdin = open("input.txt", "r")

input = sys.stdin.readline

# 문제풀이는 여기에


N, M = map(int, input().split())

id = {}
name = {}
for i in range(1, N + 1):
    pokemon = input().strip()
    id[i] = pokemon
    name[pokemon] = i

for _ in range(M):
    quest = input().strip()
    if quest in name:
        print(name[quest])
    else:
        print(id[int(quest)])
