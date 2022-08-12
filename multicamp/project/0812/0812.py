from collections import deque

"""반반 💭"""


T = int(input())

for tc in range(1, T + 1):
    alpha = input()
    TWO_SET = set(alpha)  # 중복 제거

    if len(TWO_SET) == 2:  # 셋의 길이가 2라면 "Yes", 아니면 "No"
        print(f'#{tc} {"Yes"}')
    else:
        print(f'#{tc} {"No"}')


# 또는 💭


for tc in range(1, int(input()) + 1):
    S = set(input())  # 중복 제거

    if len(S) == 2:  # 셋의 길이가 2라면
        print(f'#{tc} Yes')
    else:
        print(f'#{tc} No')


# 또는 💭


T = int(input())
for tc in range(1, T + 1):
    S = input()

    for i in range(4):  # 글자 수만큼 반복
        if S.count(S[i]) != 2:  # 해당 인덱스 값이 문자열에 몇 개인지 확인, 2가 아니라면
            print(f'#{tc} No')  # 'No' 하나만 출력하고 멈춤
            break
    else:
        print(f'#{tc} Yes')


"""모음이 보이지 않는 사람 💭"""


T = int(input())

for tc in range(1, T + 1):
    word = input()

    a = word.replace('a', '')  # 문자열에서 모음을 하나씩 삭제 (변환)
    e = a.replace('e', '')
    i = e.replace('i', '')
    o = i.replace('o', '')
    u = o.replace('u', '')

    print(f'#{tc} {u}')


# 또는 💭


T = int(input())
ALPHA = ['a', 'e', 'i', 'o', 'u']

for tc in range(1, T + 1):
    word = input()

    for i in word:
        if i in ALPHA:
            word = word.replace(i, '')

    print(f'#{tc} {word}')


# 또는 💭


ALPHA = ['a', 'e', 'i', 'o', 'u']
for tc in range(1, int(input()) + 1):
    S = input()

    result = ''
    for i in S:  # 입력 문자 순회
        if i in ALPHA:  # i가 알파라면 건너뛰기
            continue

        result += i  # 나머지는 결과값에 추가

    print(f'#{tc} {result}')


"""퍼펙트 셔플 💭"""


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    DECK = input().split()
    N = N // 2  # 총 카드의 절반을 찾아 인덱스로 접근하기 위함

    ONE = []
    if len(DECK) % 2 == 0:  # 덱의 길이가 짝수라면 / 정확히 절반
        for i in range(N):
            ONE.append(DECK[i])  # 첫번째 덱으로 추가 -> 인덱스로 접근해 해당 요소 추가
    else:
        for i in range(N + 1):  # 덱의 길이가 홀수라면 절반이 아니기 때문에 + 1
            ONE.append(DECK[i])

    TWO = []
    for i in DECK:  # 덱을 순환하면서
        if i in ONE:  # 첫번째 덱의 요소라면 패스하고
            continue
        else:
            TWO.append(i)  # 그 외 나머지를 두번째 덱으로 추가

    answer = []
    while ONE or TWO:  # 첫번째 또는 두번째 요소가 빌 때까지 반복
        if ONE:
            answer.append(ONE.pop(0))  # 0번 요소부터 하나씩 정답에 추가
        if TWO:
            answer.append(TWO.pop(0))

    print(f'#{tc} {" ".join(answer)}')


# 또는 💭


T = int(input())

for tc in range(1, T + 1):
    N = int(input())

    CARD = list(input().split())

    CUT = N - (N // 2)  # 그토록 바라던 컷 💡
    F_CARD = deque(CARD[:CUT])  # 디큐(문자열 슬라이싱)
    S_CARD = deque(CARD[CUT:])

    result = []
    while F_CARD or S_CARD:
        if F_CARD:
            result.append(F_CARD.popleft())  # 하나씩 빼면서 결과에 담아주기
        if S_CARD:
            result.append(S_CARD.popleft())

    print(f'#{tc}', end=' ')
    print(*result)


"""Flatten 💭"""


T = 10
for tc in range(1, T + 1):
    N = int(input())
    BOX = list(map(int, input().split()))  # 박스 리스트

    for _ in range(N):  # 입력으로 주어진 총 이동수만큼 반복
        MAX = max(BOX)  # 가장 큰 수
        MIN = min(BOX)  # 가장 작은 수

        I_MAX = BOX.index(MAX)  # 해당 인덱스 구하기
        I_MIN = BOX.index(MIN)

        BOX[I_MAX] -= 1  # 해당 인덱스 요소 값에서 큰 값은 빼주고 작은 값은 더해준다
        BOX[I_MIN] += 1

    print(f'#{tc} {max(BOX) - min(BOX)}')


# 또는 💭


for tc in range(1, 11):
    dump = int(input())  # 평탄화 횟수
    N = list(map(int, input().split()))

    while dump:
        N[N.index(max(N))] -= 1  # 가장 높은 인덱스 값을 찾아 - 1
        N[N.index(min(N))] += 1  # 가장 낮은 인덱스 값을 찾아 + 1

        dump -= 1  # 평탄화 수 - 1

    print(f'#{tc} {max(N) - min(N)}')  # 큰 값과 작은 값의 차이 출력


"""창용마을 무리의 개수 💭"""


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    PEOPLE = [[] for _ in range(N + 1)]  # 인접 리스트 생성
    for _ in range(M):
        v1, v2 = map(int, input().split())
        PEOPLE[v1].append(v2)
        PEOPLE[v2].append(v1)

    visited = [0] * (N + 1)  # 방문 처리할 리스트 생성

    def DFS(v):
        visited[v] = 1  # 방문 처리

        for d in PEOPLE[v]:  # 인접 정점들 순환
            if visited[d] == 0:  # 인접 정점이 방문 처리가 되지 않았다면
                DFS(d)  # DFS 실행

        return 1  # DFS가 종료되면서 리턴하는 값은 1

    cnt = 0
    for i in range(1, N + 1):
        if visited[i] == 0:  # 방문 처리가 되어있지 않다면
            cnt += DFS(i)  # DFS 실행 뒤 카운팅

    print(f'#{tc} {cnt}')


# 또는 💭


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    GRAPH = [[] for _ in range(N + 1)]  # 인접 리스트 생성
    for _ in range(1, M + 1):
        u, v = map(int, input().split())
        GRAPH[u].append(v)
        GRAPH[v].append(u)

    visited = [False for _ in range(N + 1)]  # 방문을 확인할 리스트 생성

    cnt = 0
    stack = []
    for i in range(1, N + 1):
        if not visited[i]:  # 방문을 하지 않았다면
            cnt += 1  # 무리를 확인하는 카운팅
            stack.append(i)  # 스택에 추가

            while stack:  # 스택이 빌 때까지 반복
                cur = stack.pop()  # 스택에서 제거
                visited[cur] = True  # 방문 처리

                for adj in GRAPH[cur]:  # 인접 정점 순회
                    if not visited[adj]:  # 방문을 하지 않았다면
                        stack.append(adj)  # 스택에 추가

    print(f'#{tc} {cnt}')


# 또는 💭


def DFS(start):
    visited[start] = True  # 방문 처리

    for i in graph[start]:  # 인접 정점 순회
        if not visited[i]:  # 방문하지 않았다면
            DFS(i)  # DFS 실행


for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    visited = [False] * (N + 1)  # 방문을 확인할 리스트 생성

    graph = [[] for _ in range(N + 1)]  # 인접 리스트 생성
    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    cnt = 0
    for i in range(1, N + 1):  # 인접 리스트의 인덱스만큼 순회
        if not visited[i]:  # 방문하지 않았다면
            DFS(i)  # DFS 실행
            cnt += 1  # 무리를 확인할 카운팅

    print(f'#{tc} {cnt}')


# 또는 💭


def DFS(i, graph_list, visited_list, component_list):
    stack = list()
    comp = list()  # 인접 정점을 저장할 리스트
    stack.append(i)

    while stack:  # 스택이 빌 때까지 반복
        P = stack.pop()  # 스택에서 제거하면서 변수로 저장

        if not visited_list[P]:  # 방문하지 않았다면
            visited_list[P] = True  # 방문 처리
            comp.append(P)

        for n in graph_list[P]:  # 인접 정점들 순회
            if not visited_list[n]:  # 방문하지 않았다면
                stack.append(n)  # 스택에 추가

    component_list.append(comp)


T = int(input())

for tc in range(1, T + 1):
    V, E = map(int, input().split())  # 마을 사람의 수, 서로 알고 있는 관계의 수

    visited = [False for _ in range(V + 1)]  # 방문을 확인할 리스트 생성

    GRAPH = [[] for _ in range(V + 1)]  # 인접 리스트 생성
    for _ in range(E):
        v1, v2 = map(int, input().split())
        GRAPH[v1].append(v2)
        GRAPH[v2].append(v1)

    connected_component = []  # 인접 정점들끼리 묶는 리스트
    for v in range(1, V + 1):
        if not visited[v]:  # 방문하지 않았다면 DFS 실행
            DFS(v, GRAPH, visited, connected_component)

    print(f'#{tc} {len(connected_component)}')


"""등산로 조성 🚨 💭"""


T = int(input())

for tc in range(1, T + 1):
    N, K = map(int, input().split())

    MAP = [list(map(int, input().split())) for _ in range(N)]  # 등산지도 리스트 생성
    visited = [[0] * N for _ in range(N)]  # 방문처리할 이중 리스트 생성

    dr = [0, 0, -1, 1]  # 4방위 델타 좌표
    dy = [-1, 1, 0, 0]

    high = 0
    for i in range(N):  # 이중 반복문을 이용한 완전탐색
        for j in range(N):
            if high < MAP[i][j]:  # 가장 높은 수 구하기
                high = MAP[i][j]

    def DFS(r, c):
        pass

    for i in range(N):  # 이중 반복문을 이용한 완전탐색
        for j in range(N):
            if MAP[i][j] == high:  # 지도에서 좌표가 가장 큰 값과 동일하다면
                visited[i][j] = 1  # 방문 처리
                DFS(i, j)  # DFS 실행
