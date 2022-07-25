# 파일 불러오기
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


n = int(input())

for i in range(1, n + 1):
    print('#', end='')
