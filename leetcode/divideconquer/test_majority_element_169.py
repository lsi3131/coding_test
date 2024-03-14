'''
Majority Element

https://leetcode.com/problems/majority-element/description/
'''
import collections
import unittest
from typing import List


class Solution:
    def __init__(self):
        self.is_found = False
        self.found_num = -1

    def majorityElement(self, nums: List[int]) -> int:
        counter = collections.defaultdict(int)

        def divide(left, right):
            if self.is_found:
                return

            if left >= right:
                counter[nums[left]] += 1
                if counter[nums[left]] > (len(nums) // 2):
                    self.found_num = nums[left]
                    self.is_found = True
                return

            mid = (right + left) // 2
            divide(left, mid)
            divide(mid + 1, right)

        divide(0, len(nums) - 1)

        return self.found_num


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, Solution().majorityElement([3, 2, 3]))
        self.assertEqual(2, Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
        self.assertEqual(5, Solution().majorityElement([6, 5, 5]))
        pass


if __name__ == '__main__':
    unittest.main()
