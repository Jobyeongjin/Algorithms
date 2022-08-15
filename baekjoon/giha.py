import math

'''직사각형에서 탈출'''
# 벽과 가까운 거리는 x와 y가 될 수도 있고, 가장 큰 수인 w, h와의 거리일 수도 있다.

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))


'''네 번째 점'''
# 네 번째 점은 결국 하나뿐인 값이 되니 리스트에 따로 담아서 1개인 값을 찾아주면 된다.

A, B = [], []
for _ in range(3):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

a, b = 0, 0
for i in range(3):
    if A.count(A[i]) == 1:
        a = A[i]
    if B.count(B[i]) == 1:
        b = B[i]

print(a, b)


'''직각삼각형'''
# 피타고라스의 정리 = 대변의 길이중 가장 긴 빗변의 제곱은 다른 두 변의 제곱의 합과 같다.

while True:
    TRAG = list(map(int, input().split()))

    if TRAG[0] == 0 and TRAG[1] == 0 and TRAG[2] == 0:
        break

    TRAG.sort()
    if TRAG[2]**2 == TRAG[0]**2 + TRAG[1]**2:
        print('right')
    else:
        print('wrong')


'''택시 기하학'''
# 유클리드 기하학에서 원의 넓이 = 반지름 * 반지름 * 3.14(파이)
# 택시 기하학에서 원의 넓이(정사각형의 넓이) = 2 * 반지름 * 반지름

R = int(input())

UCLID = R * R * math.pi  # 원주율(파이) 사용
TAXI = 2 * R * R

print(round(UCLID, 6))
print(round(TAXI, 6))
