"""📝 N-Queen 🚨"""


def check(x, y, col):
    for i in range(x):
        if col[i] == y or abs(y - col[i]) == x - i:  # 같은 열 또는 대각선에 위치하는지 확인
            return False
    return True


def queen(x, n, col):
    if x == n:
        return 1
    cnt = 0
    for y in range(n):
        if check(x, y, col):  # 다음 퀸을 놓을 수 잇는지 확인
            col[x] = y  # x번째 행의 열 index를 저장
            cnt += queen(x + 1, n, col)  # 행 index 증가 후 재실행
    return cnt


def solution(n):
    col = [0] * n  # 각 행의 퀸의 위치를 담을 리스트
    return queen(0, n, col)


"""📝 JadenCase 문자열 만들기"""
# capitalize() 함수는 알파벳 단어 첫글자를 대문자로 변환하고 나머지는 소문자로 변환한다.


def solution(s):
    s = s.split(' ')
    for i in range(len(s)):
        s[i] = s[i].capitalize()

    return ' '.join(s)
