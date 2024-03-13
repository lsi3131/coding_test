'''


'''

import unittest
from collections import *


class Solution:
    def __init__(self):
        self.dp = defaultdict()

    def climbStairs(self, n: int) -> int:
        self.dp[0] = 0
        self.dp[1] = 1
        self.dp[2] = 2

        for i in range(3, n + 1):
            self.dp[i] = self.dp[i - 1] + self.dp[i - 2]

        return self.dp[n]



class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, Solution().climbStairs(3))
        self.assertEqual(2, Solution().climbStairs(2))
        self.assertEqual(1836311903, Solution().climbStairs(45))


if __name__ == '__main__':
    unittest.main()
