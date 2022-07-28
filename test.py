# 파일 불러오기
from os import sep
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


words = []
for i in range(5):
    word = input()
    words.append(word)

# words = [input() for i in range(5)]
for i in range(15):
    for j in range(5):
        if i < len(words[j]):
            print(words[j][i], end='')
