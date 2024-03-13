# https://www.acmicpc.net/problem/2606

'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

from collections import defaultdict


def solution(inputs):
    graph = defaultdict(list)
    for f, t in inputs:
        graph[f].append(t)
        graph[t].append(f)

    visited = set()

    def dfs(v):
        visited.add(v)
        for w in graph[v]:
            if w not in visited:
                dfs(w)

    dfs(1)
    return len(visited) - 1


computers = int(input())
connects = int(input())

inputs = []
for _ in range(connects):
    f, t = map(int, input().split())
    inputs.append((f, t))

print(solution(inputs))
