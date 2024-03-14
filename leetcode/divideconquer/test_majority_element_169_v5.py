'''
Majority Element

https://leetcode.com/problems/majority-element/description/

DP를 사용한 풀이법
'''
import collections
import unittest
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = collections.defaultdict(int)

        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)

            if counts[num] > len(nums) // 2:
                return num
        return -1


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, Solution().majorityElement([3, 2, 3]))
        self.assertEqual(2, Solution().majorityElement([2, 2, 1, 1, 1, 2, 2]))
        self.assertEqual(5, Solution().majorityElement([6, 5, 5]))


if __name__ == '__main__':
    unittest.main()
