import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

# https://www.acmicpc.net/problem/2231

def solution(num: int):
    start = 0
    for i in range(start, num):
        div_sum = i + sum([int(x) for x in str(num)])
        if div_sum == num:
            return i

    return 0


def solution2(n: int):
    num = 0
    count = 0
    target = 0

    for j in range(num, n):
        total = 0
        for i in range(len(str(j))):
            total += int(str(j)[i])
        total += j
        if total == n:
            target = j
            count += 1
            break

    if count == 0:
        target = 0
        # print(0)

    return target


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, solution(1))
        self.assertEqual(0, solution(3))
        self.assertEqual(5, solution(10))
        self.assertEqual(9, solution(18))
        self.assertEqual(10, solution(11))
        self.assertEqual(198, solution(216))
        self.assertEqual(245, solution(256))
        self.assertEqual(982, solution(1001))
        # 1000000
        # self.assertEqual(901394, solution(901420))
        # self.assertEqual(999954, solution(999999))

    def test_example2(self):
        self.assertEqual(0, solution2(1))
        self.assertEqual(0, solution2(3))
        self.assertEqual(5, solution2(10))
        self.assertEqual(9, solution2(18))
        self.assertEqual(10, solution2(11))
        self.assertEqual(198, solution2(216))
        self.assertEqual(245, solution2(256))
        self.assertEqual(982, solution2(1001))

    def test_div_sum(self):
        self.assertEqual(1, to_div_sum(100))
        self.assertEqual(19, to_div_sum(199))

    # def test_submit(self):
    #     num = int(input())
    #     print(solution(num))


if __name__ == '__main__':
    unittest.main()
