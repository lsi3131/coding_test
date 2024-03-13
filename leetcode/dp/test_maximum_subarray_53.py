import collections
import copy
import sys

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *
from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        max_value = -sys.maxsize
        d_basic = collections.defaultdict(int)
        for i, n in enumerate(nums):
            d_basic[(i, i + 1)] = n
            max_value = max(n, max_value)

        j = 1
        d_from = copy.deepcopy(d_basic)
        d_to = defaultdict()
        while j < len(nums):
            for i in range(len(nums) - j):
                start, end = i, i + j + 1
                d_to[(start, end)] = d_from[(start, end - 1)] + d_basic[(end - 1, end)]
                max_value = max(max_value, d_to[(start, end)])
            d_from = copy.deepcopy(d_to)
            d_to.clear()

            j += 1

        return max_value


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(18, Solution().maxSubArray([4, -1, 7, 8]))
        # self.assertEqual(6, Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        # self.assertEqual(1, Solution().maxSubArray([1]))
        # self.assertEqual(23, Solution().maxSubArray([5, 4, -1, 7, 8]))
        # self.assertEqual(1, Solution().maxSubArray([-2, 1]))

    def test_slicing(self):
        d = [1, 2, 3]
        self.assertEqual([1], d[0:1])


if __name__ == '__main__':
    unittest.main()
