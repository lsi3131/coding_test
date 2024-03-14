'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''

T = int(input())


def preorder(n):
    global result
    if n:
        result += 1
        preorder(ch1[n])
        preorder(ch2[n])


for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    inputlist = list(map(int, input().split()))

    result = 0
    # 노드의 개수는 E+1 이고 0번째 리스트 요소를 쓰지 않으니 +1을 더해서 +2를 한다.
    ch1 = [0] * (E + 2)
    ch2 = [0] * (E + 2)

    for i in range(0, len(inputlist), 2):
        parent, child = inputlist[i], inputlist[i + 1]

        if ch1[parent] == 0:
            ch1[parent] = child
        elif ch2[parent] == 0:
            ch2[parent] = child

    preorder(N)

    print(f'{test_case} {result}')
