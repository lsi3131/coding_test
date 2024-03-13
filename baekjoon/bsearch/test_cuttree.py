import collections
import mycollections
import unittest
import bisect
import random
import string
import re
from collections import *
from mycollections import *


# https://www.acmicpc.net/problem/2805

def solution(trees: list, m):
    result = 0
    low, high = 1, sum(trees)
    while low <= high:
        mid = (low + high) // 2

        tree_amount = sum([tree - mid for tree in trees if tree > mid])

        # for tree in trees:
        #     if tree > mid:
        #         tree_amount += tree - mid

        if tree_amount >= m:
            low = mid + 1
            result = mid
        else:
            high = mid - 1

    return result


# --- submit ---
n, m = map(int, input().split())
heights = list(map(int, input().split()))
print(solution(heights, m))


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(15, solution([20, 15, 10, 17], 7))
        self.assertEqual(36, solution([4, 42, 40, 26, 46], 20))

    def test_submit(self):
        pass


if __name__ == '__main__':
    unittest.main()
