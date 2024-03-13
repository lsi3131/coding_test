import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14QpAaAAwCFAYi


def solution(mat, str_len):
    if str_len == 0:
        return 0
    palindromes = []
    for row in range(len(mat)):
        for i in range(0, len(mat[0]) - str_len + 1):
            s = mat[row][i:i + str_len]
            if s == s[::-1]:
                palindromes.append(s)

    for col in range(len(mat[0])):
        for i in range(0, len(mat) - str_len + 1):
            s = []
            for j in range(str_len):
                s.append(mat[i + j][col])
            if s == s[::-1]:
                palindromes.append(s)

    return len(palindromes)

# ========== submit ===============
T = 10
for test_case in range(1, T + 1):
    str_len = int(input())
    mat = []
    for row in range(8):
        row_data = []
        col_str = input()
        for col in col_str:
            row_data.append(col)

        mat.append(row_data[:])

    num = solution(mat, str_len)
    print(f'#{test_case} {num}')


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(12,
                         solution([['C', 'B', 'B', 'C', 'B', 'A', 'A', 'B'], ['C', 'C', 'C', 'B', 'A', 'B', 'C', 'B'],
                                   ['C', 'A', 'A', 'A', 'A', 'C', 'A', 'B'], ['B', 'A', 'C', 'C', 'C', 'C', 'A', 'C'],
                                   ['A', 'A', 'B', 'C', 'B', 'B', 'A', 'C'], ['A', 'C', 'A', 'A', 'C', 'A', 'B', 'C'],
                                   ['B', 'C', 'C', 'B', 'A', 'A', 'B', 'C'], ['A', 'B', 'B', 'B', 'C', 'C', 'A', 'A']],
                                  4))
        self.assertEqual(31,
                         solution([['B', 'A', 'B', 'B', 'B', 'A', 'C', 'B'], ['A', 'B', 'C', 'A', 'A', 'C', 'C', 'B'],
                                   ['C', 'C', 'A', 'C', 'B', 'C', 'B', 'A'], ['C', 'A', 'C', 'A', 'C', 'B', 'C', 'A'],
                                   ['C', 'C', 'A', 'B', 'A', 'C', 'C', 'B'], ['C', 'C', 'B', 'A', 'A', 'A', 'A', 'A'],
                                   ['B', 'B', 'A', 'C', 'B', 'A', 'C', 'A'], ['C', 'B', 'C', 'C', 'B', 'A', 'B', 'C']],
                                  3))
        self.assertEqual(0,
                         solution([['B', 'A', 'B', 'B', 'B', 'A', 'C', 'B'], ['A', 'B', 'C', 'A', 'A', 'C', 'C', 'B'],
                                   ['C', 'C', 'A', 'C', 'B', 'C', 'B', 'A'], ['C', 'A', 'C', 'A', 'C', 'B', 'C', 'A'],
                                   ['C', 'C', 'A', 'B', 'A', 'C', 'C', 'B'], ['C', 'C', 'B', 'A', 'A', 'A', 'A', 'A'],
                                   ['B', 'B', 'A', 'C', 'B', 'A', 'C', 'A'], ['C', 'B', 'C', 'C', 'B', 'A', 'B', 'C']],
                                  0))

        self.assertEqual(128,
                         solution([['B', 'A', 'B', 'B', 'B', 'A', 'C', 'B'], ['A', 'B', 'C', 'A', 'A', 'C', 'C', 'B'],
                                   ['C', 'C', 'A', 'C', 'B', 'C', 'B', 'A'], ['C', 'A', 'C', 'A', 'C', 'B', 'C', 'A'],
                                   ['C', 'C', 'A', 'B', 'A', 'C', 'C', 'B'], ['C', 'C', 'B', 'A', 'A', 'A', 'A', 'A'],
                                   ['B', 'B', 'A', 'C', 'B', 'A', 'C', 'A'], ['C', 'B', 'C', 'C', 'B', 'A', 'B', 'C']],
                                  1))
        self.assertEqual(0,
                         solution([['B', 'A', 'B', 'B', 'B', 'A', 'C', 'B'], ['A', 'B', 'C', 'A', 'A', 'C', 'C', 'B'],
                                   ['C', 'C', 'A', 'C', 'B', 'C', 'B', 'A'], ['C', 'A', 'C', 'A', 'C', 'B', 'C', 'A'],
                                   ['C', 'C', 'A', 'B', 'A', 'C', 'C', 'B'], ['C', 'C', 'B', 'A', 'A', 'A', 'A', 'A'],
                                   ['B', 'B', 'A', 'C', 'B', 'A', 'C', 'A'], ['C', 'B', 'C', 'C', 'B', 'A', 'B', 'C']],
                                  0))





if __name__ == '__main__':
    unittest.main()
