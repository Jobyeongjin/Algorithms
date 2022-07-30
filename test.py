# 파일 불러오기
from os import sep
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


t = int(input())

cnt = t
for tc in range(1, t + 1):
    word = input()

    for i in range(len(word) - 1):
        if word[i] == word[i + 1]:
            pass
        elif word[i] in word[i + 1:]:
            cnt -= 1
            break

print(cnt)
