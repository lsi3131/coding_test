'''


'''

import unittest
from collections import *


class Solution:
    def __init__(self):
        self.dp = defaultdict()

    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        if n in self.dp:
            return self.dp[n]

        self.dp[n] = self.climbStairs(n - 1) + self.climbStairs(n - 2)
        return self.dp[n]


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, Solution().climbStairs(3))
        self.assertEqual(2, Solution().climbStairs(2))
        self.assertEqual(1836311903, Solution().climbStairs(45))


if __name__ == '__main__':
    unittest.main()
