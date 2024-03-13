import bisect
import collections
from typing import List

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://leetcode.com/problems/binary-search/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            mid_val = nums[mid]
            if mid_val == target:
                return mid
            elif mid_val < target:
                left = mid + 1
            else:
                right = mid - 1

        return -1

    def search_recursive(self, nums: List[int], target: int) -> int:
        def bsearch(left, right):
            if left <= right:
                mid = (left + right) // 2
                mid_val = nums[mid]

                if mid_val < target:
                    return bsearch(mid + 1, right)
                elif mid_val > target:
                    return bsearch(left, right - 1)
                else:
                    return mid
            else:
                return -1

        left, right = 0, len(nums) - 1
        return bsearch(left, right)

    def search_bisect(self, nums: List[int], target: int) -> int:
        idx = bisect.bisect_left(nums, target)
        if idx < len(nums) and nums[idx] == target:
            return idx

        return -1



class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(4, Solution().search([-1, 0, 3, 5, 9, 12], 9))
        self.assertEqual(-1, Solution().search([-1, 0, 3, 5, 9, 12], 2))

        self.assertEqual(4, Solution().search_recursive([-1, 0, 3, 5, 9, 12], 9))
        self.assertEqual(-1, Solution().search_recursive([-1, 0, 3, 5, 9, 12], 2))

        self.assertEqual(4, Solution().search_bisect([-1, 0, 3, 5, 9, 12], 9))
        self.assertEqual(-1, Solution().search_bisect([-1, 0, 3, 5, 9, 12], 2))

    def test_bsearch(self):
        d = [1, 3, 5, 7, 9]

        self.assertEqual(0, bisect.bisect_left(d, 0))
        self.assertEqual(0, bisect.bisect_left(d, 1))
        self.assertEqual(1, bisect.bisect_left(d, 2))
        self.assertEqual(1, bisect.bisect_left(d, 3))
        self.assertEqual(2, bisect.bisect_left(d, 4))
        self.assertEqual(2, bisect.bisect_left(d, 5))
        self.assertEqual(3, bisect.bisect_left(d, 6))
        self.assertEqual(3, bisect.bisect_left(d, 7))
        self.assertEqual(4, bisect.bisect_left(d, 8))
        self.assertEqual(4, bisect.bisect_left(d, 9))
        self.assertEqual(5, bisect.bisect_left(d, 50))



if __name__ == '__main__':
    unittest.main()
