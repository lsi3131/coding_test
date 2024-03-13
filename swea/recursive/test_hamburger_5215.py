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


def solution(materials, calorie):
    results = []

    #(점수, 칼로리)
    def dfs(path, start):
        if path[1] < calorie:
            if len(results) > 0:
                #점수가 더 높을 경우
                if path[0] > results[0][0]:
                    results.pop()
                    results.append(path)
            else:
                results.append(path)

        for i in range(start, len(materials)):
            (score, cal) = path[0] + materials[i][0], path[1] + materials[i][1]
            dfs((score, cal), i + 1)

    dfs((0, 0), 0)

    return results[0][0]


T = int(input())
for test_case in range(1, T + 1):
    n, l = map(int, input().split())
    materials = []
    for _ in range(n):
        materials.append(tuple(map(int,input().split())))

    result = solution(materials, l)
    print(f'#{test_case} {result}')


class Test(unittest.TestCase):
    def test_example1(self):
        # (점수, 칼로리)
        self.assertEqual(750,
                         solution([(100, 200), (300, 500), (250, 300), (250, 300), (500, 1000), (400, 400)],
                                  1000))


if __name__ == '__main__':
    unittest.main()
