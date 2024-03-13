import collections
import heapq

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://www.acmicpc.net/problem/2563

def solution(points: list):
    paper = [[True] * 100 for _ in range(100)]

    count = 0
    for point in points:
        for y in range(point[1], point[1] + 10):
            for x in range(point[0], point[0] + 10):
                if paper[y][x]:
                    paper[y][x] = False
                    count += 1

    return count


### submit ###
n = int(input())
points = [list(map(int, input().split())) for _ in range(n)]
print(solution(points))


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(200, solution([[0, 0], [11, 0]]))
        self.assertEqual(260, solution([[3, 7], [15, 7], [5, 2]]))

    def test_submit(self):
        solution([])
        pass


if __name__ == '__main__':
    unittest.main()
