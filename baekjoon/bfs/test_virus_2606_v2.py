'''
https://www.acmicpc.net/problem/2606

7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''
import collections
from collections import defaultdict


def solution(inputs):
    graph = defaultdict(list)
    for f, t in inputs:
        graph[f].append(t)
        graph[t].append(f)

    visited = set()

    queue = collections.deque([1])
    while queue:
        v = queue.popleft()
        visited.add(v)
        for w in graph[v]:
            if w not in visited:
                queue.append(w)

    return len(visited) - 1


computers = int(input())
connects = int(input())

inputs = []
for _ in range(connects):
    f, t = map(int, input().split())
    inputs.append((f, t))

print(solution(inputs))
