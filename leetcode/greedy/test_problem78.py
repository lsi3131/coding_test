import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
class Solution(object):
    def maxProfit(self, prices: list):
        result = sum([max(prices[i + 1] - prices[i], 0) for i in range(len(prices) - 1)])
        return result


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(7, Solution().maxProfit([7, 1, 5, 3, 6, 4]))


if __name__ == '__main__':
    unittest.main()
