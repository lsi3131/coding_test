'''
https://www.acmicpc.net/problem/1916

5
8
1 2 2
1 3 3
1 4 1
1 5 10
2 4 2
3 4 1
3 5 1
4 5 3
1 5
'''

import heapq
import collections
import sys

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

# g[시작] =[(비용1, 도착1), (비용2, 도착2)]
visited = collections.defaultdict()
graph = collections.defaultdict(list)
for _ in range(m):
    start, end, cost = map(int, sys.stdin.readline().strip().split())
    graph[start].append((cost, end))

d_start, d_end = map(int, sys.stdin.readline().strip().split())

# (비용, 시작 위치)
heap = [(0, d_start)]
while heap:
    v_cost, v_start = heapq.heappop(heap)
    if v_start not in visited:
        visited[v_start] = v_cost
        for w_cost, w_end in graph[v_start]:
            next_cost = v_cost + w_cost
            heapq.heappush(heap, (next_cost, w_end))

print(visited[d_end])
