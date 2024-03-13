# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWT-lPB6dHUDFAVT&categoryId=AWT-lPB6dHUDFAVT&categoryType=CODE&problemTitle=5215&orderBy=FIRST_REG_DATETIME&selectCodeLang=ALL&select-1=&pageSize=10&pageIndex=1

import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

'''
1
5 1000
100 200
300 500
250 300
500 1000
400 400
'''


class Solution:
    def __init__(self):
        self.max_score = 0

    def do(self, materials, limit_cal):
        # (점수, 칼로리)
        def dfs(path, start):
            score, cal = path
            if cal < limit_cal and score > self.max_score:
                self.max_score = score

            for i in range(start, len(materials)):
                (add_score, add_cal) = materials[i]
                (new_score, new_cal) = score + add_score, cal + add_cal
                dfs((new_score, new_cal), i + 1)

        dfs((0, 0), 0)

        return self.max_score


T = int(input())
for test_case in range(1, T + 1):
    n, l = map(int, input().split())
    materials = []
    for _ in range(n):
        materials.append(tuple(map(int, input().split())))

    result = Solution().do(materials, l)
    print(f'#{test_case} {result}')


class Test(unittest.TestCase):
    def test_example1(self):
        # (점수, 칼로리)
        self.assertEqual(750,
                         Solution().do([(100, 200), (300, 500), (250, 300), (250, 300), (500, 1000), (400, 400)],
                                       1000))


if __name__ == '__main__':
    unittest.main()
