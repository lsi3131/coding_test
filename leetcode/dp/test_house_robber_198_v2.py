import collections
import unittest
from typing import *


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        if len(nums) <= 2:
            return max(nums)

        sums = [nums[0], max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            sums.append(max(sums[i - 1], sums[i - 2] + nums[i]))

        return sums[-1]


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(4, Solution().rob([1, 2, 3, 1]))
        self.assertEqual(12, Solution().rob([2, 7, 9, 3, 1]))
        self.assertEqual(3, Solution().rob([1, 2, 1, 1]))
        self.assertEqual(17, Solution().rob([8, 7, 3, 9]))


if __name__ == '__main__':
    unittest.main()
