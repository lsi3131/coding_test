import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def solution(mat: list[list]):
    max_row, max_col, max_val = 0, 0, 0
    for row in range(len(mat)):
        # el = ''
        for col in range(len(mat[0])):
            if max_val <= mat[row][col]:
                max_row, max_col, max_val = row + 1, col + 1, mat[row][col]
        #     el += f'({row},{col})={mat[row][col]},'
        # print(el)

    return max_val, max_row, max_col


# --- submit ---
mat = []
for _ in range(9):
    mat.append(list(map(int, input().split(' '))))
val, row, col = solution(mat)
print(val)
print(f'{row} {col}')


class Test(unittest.TestCase):
    def test_example1(self):
        mat = [
            [3, 23, 85, 34, 17, 74, 25, 52, 65],
            [10, 7, 39, 42, 88, 52, 14, 72, 63],
            [87, 42, 18, 78, 53, 45, 18, 84, 53],
            [34, 28, 64, 85, 12, 16, 75, 36, 55],
            [21, 77, 45, 35, 28, 75, 90, 76, 1],
            [65, 27, 75, 41, 7, 89, 78, 64, 39],
            [47, 47, 70, 45, 23, 65, 3, 41, 44],
            [47, 47, 70, 45, 23, 65, 3, 41, 44],
        ]
        self.assertEqual((90, 5, 7), solution(mat))

    def test_submit(self):
        mat = []
        for _ in range(9):
            mat.append(list(map(int, input().split(' '))))
        val, row, col = solution(mat)
        print(val)
        print(f'{row} {col}')


if __name__ == '__main__':
    unittest.main()
