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

result_count = sys.maxsize


def print_mat(mat):
    print('----------------------')
    for row in mat:
        print(row)


def solution(mat):
    def dfs(mat, x, y, width, height, count):
        global result_count
        if x < 0 or x >= width or y < 0 or y >= height:
            return

        if mat[y][x] == '0':
            return

        if mat[y][x] == '1':
            # print_mat(mat)
            mat[y][x] = '0'
            count += 1

        if x == (width - 1) and y == (height - 1):
            result_count = min(result_count, count)
            mat[y][x] = '1'  # 다른 경로에서 접근을 위해
            return

        dfs(mat, x + 1, y, width, height, count)
        dfs(mat, x, y + 1, width, height, count)
        dfs(mat, x - 1, y, width, height, count)
        dfs(mat, x, y - 1, width, height, count)

    dfs(mat, 0, 0, len(mat[0]), len(mat), 0)
    global result_count
    return result_count


n, m = map(int, input().split())
mat = []
for _ in range(n):
    mat.append(list(input()))

# print(mat)
print(solution(mat))
