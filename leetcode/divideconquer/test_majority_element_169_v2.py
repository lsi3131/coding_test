'''
Majority Element

https://leetcode.com/problems/majority-element/description/
'''
import collections
import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = collections.Counter(nums).most_common(1)
        return d[0][0]


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, Solution().majorityElement([3, 2, 3]))
        self.assertEqual(2, Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
        pass


if __name__ == '__main__':
    unittest.main()
