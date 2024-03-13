# https://www.acmicpc.net/problem/15650

'''
3 1
4 2
'''
def solution(n, m):
    elements = [i for i in range(1, n + 1)]
    results = []

    def dfs(path, start):
        if len(path) == m:
            results.append(path)
            return

        for i in range(start, len(elements)):
            dfs(path + [elements[i]], i + 1)

    dfs([], 0)
    return results

n, m = map(int, input().split())
nums_list = solution(n, m)
for nums in nums_list:
    print(' '.join(map(str, nums)))
