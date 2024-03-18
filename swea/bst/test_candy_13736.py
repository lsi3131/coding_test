import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *
from typing import *

import sys

'''
4
4 9 1
4 9 2
4 9 3
500 2000 2000000000
'''


def power(K, sum):
    if K == 1:
        return 2

    ret = power(K // 2, sum)
    ret = (ret ** 2) % sum

    if K % 2 == 1:
        ret = (ret * 2) % sum

    return ret


def solution(A, B, k):
    sum = A + B
    kp = power(k, sum)

    A = (A * kp) % sum

    return min(A, sum - A)


T = int(input())
for testcase in range(1, T + 1):
    A, B, K = map(int, input().split())
    result = solution(A, B, K)
    print(f'#{testcase} {result}')


class Test(unittest.TestCase):
    def test_example1(self):
        # self.assertEqual(5, solution(4, 9, 1))
        # self.assertEqual(3, solution(4, 9, 2))
        self.assertEqual(6, solution(4, 9, 3))
        # self.assertEqual(500, solution(500, 2000, 2000000000))
        pass

    # def test_mod(self):
    #     self.assertEqual(2, 2 % 0)


if __name__ == '__main__':
    unittest.main()
