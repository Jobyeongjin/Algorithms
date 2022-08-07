# 수 정렬하기 🐳
# 문제 : 오름차순 정렬하기

import sys
from collections import Counter
from collections import deque

arr = [int(input()) for _ in range(int(input()))]
sort_ = sorted(arr)

for i in sort_:
    print(i)


# 수 정렬하기 2 🐳
# 문제 : 오름차순 정렬하기

input = sys.stdin.readline

n = int(input())
arr = [int(input()) for _ in range(n)]
sort_ = sorted(arr)

print(*sort_, sep='\n')


# 수 정렬하기 3 🚨 🐳
# 문제 : 오름차순 정렬하기

n = int(input())
arr = [0] * 10001

for _ in range(n):
    arr[int(input())] += 1

for i in range(10001):
    if arr[i] != 0:
        for j in range(arr[i]):
            print(i)


# 커트라인 🐳
# 문제 : 상을 받는 커트라인이 몇 점인지 구하기

N, K = map(int, input().split())

score = list(map(int, input().split()))

sort_ = sorted(score, reverse=True)

print(sort_[K - 1])


# 통계학 🐳
# 문제 : 4가지 기본 통계값 구하기

N = int(input())

numbers = [int(input()) for _ in range(N)]
numbers.sort()
# 평균
avg = round(sum(numbers) / N)

print(avg)

# 중앙값
queue = deque(numbers)
while len(queue) > 1:
    queue.popleft()
    queue.pop()

print(*queue)

# 최빈값
cnt = Counter(numbers).most_common()

if len(numbers) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])

# 범위
scope = max(numbers) - min(numbers)

print(scope)


# 소트인사이드 🐳
# 문제 : 내림차순 정렬하기

word = input()
numbers = [i for i in word]
numbers.sort(reverse=True)

print(*numbers, sep='')


# 좌표 정렬하기 🐳
# 문제 : 2차원 평면 위의 점 N개가 주어진다. 좌표를 x좌표가 증가하는 순으로, x좌표가 같으면 y좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

N = int(input())

position = [list(map(int, input().split())) for _ in range(N)]
position.sort()

for i in position:
    print(*i)


# 좌표 정렬하기 2 🐳
# 문제 : 2차원 평면 위의 점 N개가 주어진다. 좌표를 y좌표가 증가하는 순으로, y좌표가 같으면 x좌표가 증가하는 순서로 정렬한 다음 출력하는 프로그램을 작성하시오.

# 정답은 맞게 나오는데 정답은 아님...
N = int(input())

position = [list(map(int, input().split())) for _ in range(N)]
position.sort()
rotation = deque(position)
rotation.rotate(-1)

for i in rotation:
    print(*i)

# 정답, 람다 함수 사용
N = int(input())

position = [list(map(int, input().split())) for _ in range(N)]
position.sort(key=lambda x: (x[1], x[0]))  # 인덱스 0을 1부터 시작

for i in position:
    print(*i)


# 단어 정렬 🐳
# 문제 : 길이가 짧은 것부터, 길이가 같으면 사전 순으로 정렬하기

N = int(input())

word = [input().strip() for _ in range(N)]  # strip 함수는 시작 또는 끝의 공백 제거

set_ = set(word)  # 중복 값 제거
list_ = list(set_)
list_.sort()  # 알파벳 순 정렬
list_.sort(key=len)  # 길이 기준으로 정렬

for i in list_:
    print(i)


# 나이순 정렬 🐳
# 문제 : 나이가 많은 순으로 정렬, 나이가 같으면 먼저 가입한 순으로 정렬

N = int(input())

members = [list(input().split()) for _ in range(N)]
members.sort(key=lambda x: int(x[0]))

for i in members:
    print(*i)
