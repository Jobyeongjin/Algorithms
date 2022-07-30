# 파일 불러오기
from calendar import c
from os import sep
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


a = input().split(':')

print(a, type(a))
print(a[1])
