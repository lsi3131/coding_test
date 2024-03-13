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
import collections
import sys


def print_mat(mat):
    for row in mat:
        print(row)


def solution(mat):
    def bfs(mat, x, y, width, height):
        queue = collections.deque()
        queue.append((x, y))

        while queue:
            x, y = queue.popleft()
            if 0 <= x < width and 0 <= y < height and mat[y][x] == 1:
                mat[y][x] = 0
                queue.append((x + 1, y))
                queue.append((x - 1, y))
                queue.append((x, y + 1))
                queue.append((x, y - 1))

    width = len(mat[0])
    height = len(mat)
    count = 0
    for y in range(height):
        for x in range(width):
            if mat[y][x] == 1:
                bfs(mat, x, y, width, height)
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
