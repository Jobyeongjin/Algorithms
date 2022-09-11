import heapq

"""📝 최소 힙"""

n = int(input())
heap = []

for _ in range(n):
    number = int(input())

    if number != 0:
        heapq.heappush(heap, number)
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap))


"""📝 최대 힙"""

n = int(input())
heap = []

for _ in range(n):
    number = int(input())

    if number != 0:
        heapq.heappush(heap, -number)
    else:
        if not heap:
            print(0)
        else:
            print(-1 * heapq.heappop(heap))


"""📝 절대값 힙"""

n = int(input())
heap = []

for _ in range(n):
    number = int(input())

    if number != 0:
        heapq.heappush(heap, (abs(number), number))
    else:
        if not heap:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
