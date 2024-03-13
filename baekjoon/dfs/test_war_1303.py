'''
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW

2 2
WW
BW

5 5
WBBBB
WBBBB
WBBBB
WBBBB
WWBWW

5 6
WBBBB
WBBBB
WBBBB
WBBBB
WWBWW
WWBWW

'''


class Solution:
    def __init__(self):
        self.white_power = 0
        self.blue_power = 0
        self.people_count = 0

    def do(self, mat):
        visited_ch = '#'

        def dfs(mat, x, y, width, height, ch):
            if x < 0 or x >= width or y < 0 or y >= height:
                return

            if mat[y][x] != ch:
                return

            if mat[y][x] == ch:
                mat[y][x] = visited_ch
                self.people_count += 1

            dfs(mat, x + 1, y, width, height, ch)
            dfs(mat, x, y + 1, width, height, ch)
            dfs(mat, x - 1, y, width, height, ch)
            dfs(mat, x, y - 1, width, height, ch)

        width, height = len(mat[0]), len(mat)
        for y in range(height):
            for x in range(width):
                if mat[y][x] != visited_ch:
                    self.people_count = 0
                    ch = mat[y][x]
                    dfs(mat, x, y, width, height, ch)
                    if ch == 'W':
                        self.white_power += (self.people_count ** 2)
                    elif ch == 'B':
                        self.blue_power += (self.people_count ** 2)

        return self.white_power, self.blue_power


n, m = map(int, input().split())
mat = []
for _ in range(m):
    mat.append(list(input()))

# print(mat)
w, b = Solution().do(mat)
print(f'{w} {b}')
