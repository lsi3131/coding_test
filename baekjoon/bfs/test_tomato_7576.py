'''
https://www.acmicpc.net/problem/7576

6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
0 -1 0 0 0 0
-1 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
'''
import collections
import sys


class Solution:
    def __init__(self):
        self.queue = collections.deque()
        self.remain_count = 0
        self.day = 0

    def do(self, mat):
        w, h = len(mat[0]), len(mat)

        for y in range(h):
            for x in range(w):
                if mat[y][x] == 0:
                    self.remain_count += 1

        for y in range(h):
            for x in range(w):
                if mat[y][x] == 1:
                    self.queue.append((x, y))

        self.bfs(mat, w, h)
        if self.remain_count > 0:
            return -1
        return self.day

    def color_tomato(self, queue, mat, x, y, w, h):
        if 0 <= x < w and 0 <= y < h and mat[y][x] == 0:
            self.remain_count -= 1
            mat[y][x] = 1
            queue.append((x, y))

    def bfs(self, mat, w, h):
        while self.queue:
            for _ in range(len(self.queue)):
                x, y = self.queue.popleft()
                self.color_tomato(self.queue, mat, x + 1, y, w, h)
                self.color_tomato(self.queue, mat, x - 1, y, w, h)
                self.color_tomato(self.queue, mat, x, y - 1, w, h)
                self.color_tomato(self.queue, mat, x, y + 1, w, h)
            if len(self.queue) > 0:
                self.day += 1


M, N = map(int, input().split())

mat = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

print(Solution().do(mat))
