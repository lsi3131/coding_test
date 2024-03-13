import heapq

'''
https://leetcode.com/problems/maximum-subarray/description/
'''

import unittest
from typing import *


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sums = [nums[0]]
        for i in range(1, len(nums)):
            sums.append(nums[i] + (sums[i-1] if sums[i-1] > 0 else 0))
            # nums[i] += nums[i - 1] if nums[i - 1] > 0 else 0
        return max(nums)


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(18, Solution().maxSubArray([4, -1, 7, 8]))
        # self.assertEqual(6, Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
        # self.assertEqual(1, Solution().maxSubArray([1]))
        # self.assertEqual(23, Solution().maxSubArray([5, 4, -1, 7, 8]))
        # self.assertEqual(1, Solution().maxSubArray([-2, 1]))


if __name__ == '__main__':
    unittest.main()
