# 팩토리얼 🐳
# 문제 : n!

def fact(n):
    if n == 0:  # 0이라면 1
        return 1
    return n * fact(n - 1)  # 10 * 9(8, 7, 6, ..., 1)


n = int(input())

print(fact(n))


# 재귀함수가 뭔가요? 🐳
# 문제 : 교수님의 챗봇 만들기

def recursion(i, n):
    print("____" * i + '"재귀함수가 뭔가요?"')
    if i == n:
        print("____" * i + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print("____" * i + '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.')
        print("____" * i + "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
        print("____" * i + '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."')
        recursion(i + 1, n)
    print("____" * i + "라고 답변하였지.")


n = int(input())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
recursion(0, n)
