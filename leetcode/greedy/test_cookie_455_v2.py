import bisect
import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *
from typing import *


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        grd_idx = 0
        for i in range(len(s)):
            idx = bisect.bisect_right(g, s[i])
            if idx > grd_idx:
                grd_idx += 1

        return grd_idx


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, Solution().findContentChildren([1, 2, 3], [1, 1]))
        self.assertEqual(2, Solution().findContentChildren([1, 2], [1, 2, 3]))
        # dd


if __name__ == '__main__':
    unittest.main()
