import collections
import copy

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://leetcode.com/problems/permutations/description/

def permute(nums: list[int]):
    if len(nums) == 0:
        return []

    results = []
    cur_elelement = []

    def dfs(elements: list):
        if len(elements) == 0:
            results.append(cur_elelement[:])

        for e in elements:
            cur_elelement.append(e)

            next_element = elements[:]
            next_element.remove(e)

            dfs(next_element)
            cur_elelement.pop()

    dfs(nums)

    return results


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([], permute([]))
        self.assertEqual([[1]], permute([1]))
        self.assertEqual([[1, 2], [2, 1]], permute([1, 2]))
        self.assertEqual([
            [1, 2, 3],
            [1, 3, 2],
            [2, 1, 3],
            [2, 3, 1],
            [3, 1, 2],
            [3, 2, 1],
        ], permute([1, 2, 3]))

    def test_list_copy(self):
        l1 = [1, 2, 3]
        l2 = copy.deepcopy(l1)
        l2.pop(1)
        self.assertEqual([1, 2, 3], l1)
        self.assertEqual([1, 3], l2)


if __name__ == '__main__':
    unittest.main()
