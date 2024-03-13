'''
1
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
'''

import sys


def print_mat(mat):
    for row in mat:
        print(row)


def solution(mat):
    def dfs(mat, x, y, width, height):
        if x < 0 or x >= width or y < 0 or y >= height:
            return

        if mat[y][x] == 0:
            return

        if mat[y][x] == 1:
            mat[y][x] = 0

        dfs(mat, x + 1, y, width, height)
        dfs(mat, x - 1, y, width, height)
        dfs(mat, x, y + 1, width, height)
        dfs(mat, x, y - 1, width, height)

    width = len(mat[0])
    height = len(mat)
    count = 0
    for y in range(height):
        for x in range(width):
            if mat[y][x] == 1:
                dfs(mat, x, y, width, height)
                count += 1
    return count


t = int(input())
results = []

for _ in range(t):
    m, n, k = map(int, input().split())
    mat = [[0] * m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        mat[y][x] = 1

    results.append(solution(mat))

for r in results:
    print(r)
