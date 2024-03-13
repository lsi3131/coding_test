import collections
import unittest
from typing import *


class Solution:
    def __init__(self):
        self.dp = collections.defaultdict()

    def rob(self, nums: List[int]) -> int:
        def dfs(nums, idx):
            if idx >= len(nums):
                return 0

            if idx in self.dp:
                return self.dp[idx]

            n1 = dfs(nums, idx + 2)
            n2 = dfs(nums, idx + 3)
            result = nums[idx] + max(n1, n2)
            self.dp[idx] = result
            return self.dp[idx]

        n1 = dfs(nums, 0, 0)
        n2 = dfs(nums, 1, 0)
        return max(n1, n2)


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(4, Solution().rob([1, 2, 3, 1]))
        self.assertEqual(12, Solution().rob([2, 7, 9, 3, 1]))
        self.assertEqual(3, Solution().rob([1, 2, 1, 1]))
        pass


if __name__ == '__main__':
    unittest.main()
