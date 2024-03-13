import collections
import itertools

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://leetcode.com/problems/combinations/

def combine(n, k):
    if n == 0:
        return []

    results = []

    def dfs(elements, start, k):
        if k == 0:
            results.append(elements[:])
            return

        for i in range(start, n + 1):
            elements.append(i)
            dfs(elements, i + 1, k - 1)
            elements.pop()

    dfs([], 1, k)

    return results


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([], combine(0, 0))
        self.assertEqual([[1]], combine(1, 1))
        self.assertEqual([[1, 2]], combine(2, 2))
        self.assertEqual([[1, 2], [1, 3], [1, 4], [2, 3], [2, 4], [3, 4]], combine(4, 2))

    def test_list(self):
        n = 5
        nums = [i for i in range(1, n + 1, 1)]
        print(nums)


if __name__ == '__main__':
    unittest.main()
