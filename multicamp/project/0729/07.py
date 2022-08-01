# 암호문 1 🚨

for tc in range(1, 11):
    ori_n = int(input())  # 원본 뭉치의 갯수
    data = list(map(int, input().split()))  # 원본
    cmd = int(input())  # 명령어, 무시해도 됨
    cmd_order = list(input().split())  # 삽입할 명령어 뭉치들

    type = ''  # 명령어 파악
    pos = -1  # 삽입 위치
    cnt = -1  # 삽입 갯수
    for i in range(len(cmd_order)):
        # 암호화 첫번째 단어 체크 I 1 5
        if cmd_order[i] == 'I':
            type = cmd_order[i]
            pos = -1
            cnt = -1
        else:
            # 두번째 단어 체크
            if type == 'I':
                if pos == -1:
                    pos = int(cmd_order[i])
                    continue
                else:
                    # 세번째 단어 체크
                    if cnt == -1:
                        cnt = int(cmd_order[i])
                        continue

                    data.insert(pos, cmd_order[i])
                    pos += 1

    print(f'#{tc}', end=' ')
    print(*data[:10])

# 또는

t = 10

for tc in range(1, t + 1):
    origin_len = int(input())
    origin_list = list(map(int, input().split()))

    command_len = int(input())
    command_list = input().split()

    i = 0

    while i < len(command_list):
        command = command_list[i]
        if command == 'I':
            x = int(command_list[i + 1])
            y = int(command_list[i + 2])

            number_list = command_list[i + 3: i + 3 + y]

            for number in number_list[::-1]:
                origin_list.insert(x, int(number))

        i = i + 1

    print(f'#{tc}' * origin_list[:10])
