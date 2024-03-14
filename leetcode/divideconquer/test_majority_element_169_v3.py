'''
Majority Element

https://leetcode.com/problems/majority-element/description/
'''
import collections
import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if nums is None:
            return 0

        if len(nums) == 1:
            return nums[0]

        half = len(nums) // 2
        a = self.majorityElement(nums[:half])
        b = self.majorityElement(nums[half:])

        return [b, a][nums.count(a) > len(nums) // 2]


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, Solution().majorityElement([3, 2, 3]))
        self.assertEqual(2, Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
        self.assertEqual(5, Solution().majorityElement([6, 5, 5]))


if __name__ == '__main__':
    unittest.main()
