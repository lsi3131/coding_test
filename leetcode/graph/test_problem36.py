import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://leetcode.com/problems/combination-sum/description/

def combinationSum(candidates, target):
    results = []

    def dfs(start, path: list, sum_comb):
        if sum_comb > target:
            return
        elif sum_comb == target:
            results.append(path)
            return

        for i in range(start, len(candidates)):
            dfs(i, path + [candidates[i]], sum_comb + candidates[i])

    dfs(0, [], 0)

    return results


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(sorted([]), sorted(combinationSum([2], 3)))
        self.assertEqual(sorted([]), sorted(combinationSum([], 3)))
        self.assertEqual([[1, 1, 1], [1, 2], [3]], sorted(combinationSum([1, 2, 3], 3)))
        self.assertEqual(sorted([[7], [2, 2, 3]]), sorted(combinationSum([2, 3, 6, 7], 7)))
        self.assertEqual(sorted([[2, 2, 2, 2], [2, 3, 3], [3, 5]]), sorted(combinationSum([2, 3, 5], 8)))

    def test_plus_list(self):
        path1 = [1, 2, 3]
        print(f'path1={path1}, id={id(path1)}')
        path2 = path1 + [4]
        print(f'path2={path2}, id={id(path2)}')


if __name__ == '__main__':
    unittest.main()
