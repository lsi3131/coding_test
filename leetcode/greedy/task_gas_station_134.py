'''
https://leetcode.com/problems/gas-station/description/
'''
import unittest
import heapq
from typing import *


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        delta_list = []
        start_idx_set = set()
        for i in range(len(gas)):
            delta = gas[i] - cost[i]
            delta_list.append(delta)
            if delta >= 0:
                start_idx_set.add(i)

        start_idx = -1
        while start_idx_set:
            start_idx = start_idx_set.pop()
            i = start_idx
            count = 0
            cur = 0
            length = len(delta_list)
            while count < length:
                if i in start_idx_set:
                    start_idx_set.remove(i)
                i = i % length
                cur += delta_list[i]
                if cur < 0:
                    start_idx = -1
                    break

                i += 1
                count += 1

        if len(start_idx_set) > 0:
            return -1
        return start_idx


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, Solution().canCompleteCircuit([1, 2, 3, 4, 5], [3, 4, 5, 1, 2]))
        self.assertEqual(-1, Solution().canCompleteCircuit([2, 3, 4], [3, 4, 3]))
        self.assertEqual(-1, Solution().canCompleteCircuit([2], [3]))
        self.assertEqual(0, Solution().canCompleteCircuit([4], [3]))
        self.assertEqual(3, Solution().canCompleteCircuit([5, 8, 2, 8], [6, 5, 6, 6]))
        pass
