'''
https://www.acmicpc.net/problem/1309

4
'''
N = int(input())
mod = 9901

def solution(N):
    lion = 2
    empty = 1
    for i in range(2, N + 1):
        # lion, empty = lion + 2 * empty, lion + empty
        lion, empty = (lion + 2 * empty) % mod, (lion + empty) % mod

    return lion + empty


print(solution(N) % mod)
