def list_odd(x):
    global found_text
    for line in x:
        for index in range(len(line) - n + 1):
            if line[index:index + share] == line[index + share: index + (share * 2)][::-1]:
                found_text += 1


def list_even(x):
    global found_text
    for line in x:
        for index in range(len(line) - n + 1):
            if line[index:index + share] == line[index + share + 1: index + (share * 2) + 1][::-1]:
                found_text += 1


T = 2
for test_case in range(1, T + 1):
    n = int(input())
    list_text = []
    found_text = 0

    for i in range(8):
        a = list(input())
        list_text.append(a)

    remain = n % 2
    share = n // 2

    # 짝수
    if remain == 0:
        # 가로
        list_odd(list_text)
        #   세로
        list_text = list(map(list, zip(list_text)))

        list_odd(list_text)
    # 홀수
    else:
        # 가로
        list_even(list_text)
        #  세로
        list_text = list(map(list, zip(list_text)))
        list_even(list_text)
    print(f"#{test_case} {found_text}")
