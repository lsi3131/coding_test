'''
https://www.acmicpc.net/problem/2178

4 6
101111
101010
101011
111011

7 7
1011111
1110001
1000001
1000001
1000001
1000001
1111111

3 3
111
101
101
'''
import sys
import collections


def solution(mat):
    def is_promising(mat, x, y, width, height):
        return 0 <= x < width and 0 <= y < height and mat[y][x] == '1'

    def bfs(mat, x, y, width, height):
        queue = collections.deque()
        queue.append((x, y, 0))
        min_count = sys.maxsize

        while queue:
            (x, y, count) = queue.popleft()
            if is_promising(mat, x, y, width, height):
                mat[y][x] = '0'
                queue.append((x + 1, y, count + 1))
                queue.append((x - 1, y, count + 1))
                queue.append((x, y - 1, count + 1))
                queue.append((x, y + 1, count + 1))

            if x == (width - 1) and y == (height - 1):
                count += 1
                min_count = min(min_count, count)
                break
        return min_count

    return bfs(mat, 0, 0, len(mat[0]), len(mat))


n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(input()))

print(solution(mat))
