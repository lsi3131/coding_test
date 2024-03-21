'''
https://www.acmicpc.net/problem/1309

4
'''
N = int(input())


def solution(N):
    lion = 2
    empty = 1
    for i in range(2, N + 1):
        lion, empty = lion + 2 * empty, lion + empty

    return lion + empty


print(solution(N) % 9901)
