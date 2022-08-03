# 파일 불러오기
from sys import stdin

stdin = open("input.txt", "r")

input = stdin.readline

# 문제풀이는 여기에

n = int(input())

log_list = []
for i in range(n):
    name = input()
    log_list.append(name)

gom = 0
set_ = set()
for log in log_list:
    if log == 'ENTER':
        set_.clear()
    else:
        if log not in set_:
            set_.add(log)
            gom += 1

print(gom)

# log_list = ['입력값']
# gom = 0
# # 리스트에서 중복탐색을 할 때는 n만큼의 시간이 필요 💡
# # 셋에서 중복탐색을 할 때는 1만큼의 시간이 필요 💡
# set_ = set()
# for log in log_list:
#     if log == 'ENTER':
#         set_.clear()
#     else:
#         if log not in set_:
#             set_.add(log)
#             gom += 1
