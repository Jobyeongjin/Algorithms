# 파일 불러오기
from os import sep
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에

alpha = input().upper()
alpha_set = list(set(alpha))

cnt_ = []
for i in alpha_set:
    cnt = alpha.count(i)
    cnt_.append(cnt)

max_ = max(cnt_)
if cnt_.count(max_) >= 2:
    print('?')
else:
    print(alpha_set[cnt_.index(max_)])
