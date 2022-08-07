# 숫자 카드 🐳
# 문제 : 상근이가 가지고 있는 카드인지 아닌지 구별하기

N = int(input())
cards = set(map(int, input().split()))  # 리스트로 하면 시간 초과
M = int(input())
stack = list(map(int, input().split()))

for i in stack:
    if i in cards:
        print(1, end=' ')
    else:
        print(0, end=' ')


# 또는 (이진탐색)
N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
stack = list(map(int, input().split()))

answer = []


def binary(item, cards, start, end):
    # cards = [-10, 2, 3, 6, 10]
    # stack = [10, 9, -5, 2, 3, 4, 5, -10]
    # start = 0
    # end = 4
    mid = (start + end) // 2

    if start > end:
        answer.append(0)
    elif item == cards[mid]:
        answer.append(1)
    elif item > cards[mid]:
        binary(item, cards, mid + 1, end)
    else:
        binary(item, cards, start, mid - 1)


for item in stack:
    start = 0
    end = len(cards) - 1
    binary(item, cards, start, end)

print(*answer)


# 숫자 카드 2 🐳
# 문제 : 상근이가 몇 개의 카드를 가지고 있는지 구하기

# 정답과 같지만 시간초과
# N = int(input())
# cards = sorted(list(map(int, input().split())))
# M = int(input())
# stack = list(map(int, input().split()))

# answer = []
# for i in stack:
#     if i in cards:
#         answer.append(cards.count(i))
#     else:
#         answer.append(0)

# print(*answer)

# 딕셔너리로 풀이
N = int(input())
cards = sorted(list(map(int, input().split())))
M = int(input())
stack = list(map(int, input().split()))

answer = {}
for i in cards:
    if i in answer:
        answer[i] += 1
    else:
        answer[i] = 1

for i in range(M):
    if stack[i] in answer:
        print(answer[stack[i]], end=' ')
    else:
        print(0, end=' ')


# 문자열 집합 🐳
# 문제 : 주어진 집합문자에 입력 문자가 총 몇 개인지 구하기

N, M = map(int, input().split())
S = set([input() for _ in range(N)])  # set으로 처리하니 리스트보다 속도가 훨씬 빨라졌다

cnt = 0
for _ in range(M):
    word = input()
    if word in S:
        cnt += 1

print(cnt)


# 나는야 포켓몬 마스터 이다솜 🐳
# 문제 : 도감에 있는 포켓몬 이름과 번호 구하기

# 인덱스로 접근하려다가 실패
# N, M = map(int, input().split())

# pokemon = [input().strip() for _ in range(N)]

# quest = [input().strip() for _ in range(M)]

# for i in quest:
#     if i in pokemon:
#         print(pokemon.index(i))
#     else:
#         print(pokemon[int(i)])

# 딕셔너리로 풀이
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
