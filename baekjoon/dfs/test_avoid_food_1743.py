'''
https://www.acmicpc.net/problem/1743

3 4 5
3 2
2 2
3 1
2 3
1 1

'''

import sys

sys.setrecursionlimit(100000)
max_count = 0
count = 0


def solution(mat):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]
    w = len(mat[0])
    h = len(mat)

    def dfs(mat, x, y, w, h):
        global max_count
        global count
        if 0 <= x < w and 0 <= y < h and mat[y][x] == 1:
            mat[y][x] = 0
            count += 1
            for i in range(len(dx)):
                dfs(mat, x + dx[i], y + dy[i], w, h)

    global max_count
    global count
    for y in range(h):
        for x in range(w):
            if mat[y][x] == 1:
                count = 0
                dfs(mat, x, y, w, h)
                max_count = max(max_count, count)

    return max_count


N, M, K = map(int, input().split())
mat = [[0] * M for _ in range(N)]
# print(mat)

for _ in range(K):
    y, x = map(int, sys.stdin.readline().split())
    mat[y - 1][x - 1] = 1

print(solution(mat))
