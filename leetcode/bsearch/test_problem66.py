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


# https://leetcode.com/problems/search-in-rotated-sorted-array/description/

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # pivot을 구한다. 최소값을 구한다.
        left, right = 0, len(nums) - 1
        while left < right:
            mid = left + (right - left) // 2
            # 오른쪽에 피벗이 있으니 left를 오른쪽으로
            if nums[mid] > nums[right]:
                left = mid + 1
            # 왼쪽에 피벗이 있으니 right를 왼쪽으로
            # 탈출조건이 left < right 이므로 right는 mid로 이동한다.
            else:
                right = mid

        pivot = left

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            mid_pivot = (mid + pivot) % len(nums) # 모듈로 연산으로 인덱스를 회전한다.

            if nums[mid_pivot] > target:
                right = mid - 1
            elif nums[mid_pivot] < target:
                left = mid + 1
            else:
                return mid_pivot

        return -1


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(4, Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
        self.assertEqual(-1, Solution().search([4, 5, 6, 7, 0, 1, 2], 3))
        self.assertEqual(6, Solution().search([4, 5, 6, 7, 0, 1, 2], 2))


if __name__ == '__main__':
    unittest.main()
