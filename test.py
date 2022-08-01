# 파일 불러오기
import sys

sys.stdin = open("input.txt", "r")

# 문제풀이는 여기에


n = int(stdin.readline())

people = {}
# 참가자 입력
for _ in range(n):
    name = stdin.readline()
    if name in people:
        people[name] += 1
    else:
        people[name] = 1

# 완주자 입력
for i in range(n - 1):
    name = stdin.readline()
    if people[name] == 1:
        del people[name]
    elif name in people:
        people[name] -= 1

print(*people)
