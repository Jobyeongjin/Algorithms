# 파일 불러오기
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


n = int(input())
m = int(input())

sosu_list = []
for num in range(n, m + 1):
    if num != 1:
        check = True
        for i in range(2, num):
            if num % i == 0:
                check = False
                break
        if check:
            sosu_list.append(num)

if len(sosu_list) > 0:
    print(sum(sosu_list), min(sosu_list), sep='\n')
else:
    print(-1)
