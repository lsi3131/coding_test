'''
Majority Element

https://leetcode.com/problems/majority-element/description/

sort를 사용한 풀이법
'''
import collections
import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums) // 2]


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, Solution().majorityElement([3, 2, 3]))
        self.assertEqual(2, Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
        self.assertEqual(5, Solution().majorityElement([6, 5, 5]))


if __name__ == '__main__':
    unittest.main()
