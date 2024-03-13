import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def subsets(nums):
    results = []

    def dfs(start, elements):
        results.append(elements)
        for i in range(start, len(nums)):
            dfs(i + 1, elements + [nums[i]])

    dfs(0, [])

    return results


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(sorted([[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]), sorted(subsets([1, 2, 3])))
        self.assertEqual(sorted([[], [0]]), sorted(subsets([0])))
        self.assertEqual(sorted([[], [0]]), sorted(subsets([-1,0,1,2])))


if __name__ == '__main__':
    unittest.main()
