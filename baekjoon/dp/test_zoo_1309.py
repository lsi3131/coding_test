'''
https://www.acmicpc.net/problem/1309

4
'''
N = int(input())


def lion(N):
    dict_lion = 2
    dict_none = 1
    for i in range(2, N + 1):
        dict_lion, dict_none = dict_lion + 2 * dict_none, dict_lion + dict_none

    return dict_lion + dict_none


print(lion(N) % 9901)
