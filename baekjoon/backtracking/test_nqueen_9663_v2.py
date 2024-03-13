# https://www.acmicpc.net/problem/9663
import copy
import unittest


# n = map(int, input())
def print_mat(mat):
    for row in mat:
        print(row)


def solution(n: int):
    def add_tiles_to_direction(tiles: set, col, row, col_d, row_d, n):
        while not (col < 0 or col >= n or row < 0 or row >= n):
            if (col, row) in tiles:
                tiles.remove((col, row))
            row += row_d
            col += col_d

    def pop_tiles(tiles, col, row, n):
        add_tiles_to_direction(tiles, col, row, 1, 0, n)
        add_tiles_to_direction(tiles, col, row, -1, 0, n)
        add_tiles_to_direction(tiles, col, row, 0, 1, n)
        add_tiles_to_direction(tiles, col, row, 0, -1, n)
        add_tiles_to_direction(tiles, col, row, -1, -1, n)
        add_tiles_to_direction(tiles, col, row, 1, -1, n)
        add_tiles_to_direction(tiles, col, row, -1, 1, n)
        add_tiles_to_direction(tiles, col, row, 1, 1, n)

    results = []

    def dfs(tiles, n, path):
        if len(tiles) == 0:
            if len(path) == n:
                results.append(path)
                return path
            else:
                return []

        result_path = []
        while tiles:
            col, row = tiles.pop()
            new_tiles = copy.deepcopy(tiles)
            pop_tiles(new_tiles, col, row, n)
            result_path = dfs(new_tiles, n, path + [(col, row)])
        return result_path

    tiles = set()
    for row in range(n):
        for col in range(n):
            tiles.add((col, row))
    dfs(tiles, n, [])

    return len(results)

n = int(input())
print(solution(n))


class Test(unittest.TestCase):
    def test_example1(self):
        # self.assertEqual(0, solution(1))
        # self.assertEqual(0, solution(2))
        self.assertEqual(2, solution(4))
        # self.assertEqual(10, solution(5))
        # self.assertEqual(4, solution(6))
        # self.assertEqual(40, solution(7))
        self.assertEqual(92, solution(8))
        # self.assertEqual(352, solution(9))
        # self.assertEqual(2, solution(6))

    def test_remove(self):
        test_set = set()
        test_set.add((0, 0))
