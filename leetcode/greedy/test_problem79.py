import collections
import heapq
from typing import List

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://leetcode.com/problems/queue-reconstruction-by-height/description/
class Solution:
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        heap = []
        for person in people:
            heapq.heappush(heap, [-person[0], person[1]])

        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])

        return result


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([[5, 0], [7, 0], [5, 2], [6, 1], [4, 4], [7, 1]],
                         Solution().reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]))

        self.assertEqual([[4, 0], [5, 0], [2, 2], [3, 2], [1, 4], [6, 0]],
                         Solution().reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]]))


if __name__ == '__main__':
    unittest.main()
