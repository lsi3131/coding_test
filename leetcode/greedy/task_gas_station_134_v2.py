'''
https://leetcode.com/problems/gas-station/description/
'''
import unittest
import heapq
from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1

        start, fuel = 0, 0
        for i in range(len(gas)):
            # 출발점이 안 되는 지점 판별
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]

        return start


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
        self.assertEqual(-1, Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]))
        self.assertEqual(-1, Solution().canCompleteCircuit([2], [3]))
        self.assertEqual(0, Solution().canCompleteCircuit([4], [3]))
        self.assertEqual(3, Solution().canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6]))
        pass
