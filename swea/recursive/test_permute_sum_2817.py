# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AXTC0x16D8EDFASe

import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

'''
1
4 3
1 2 1 2
'''


def solution(nums: list, k):
    results = []

    def dfs(path, start, k):
        num_sum = sum(path)
        if num_sum == k:
            results.append(path)
            return
        elif num_sum > k:
            return

        for i in range(start, len(nums)):
            dfs(path + [nums[i]], i + 1, k)

    dfs([], 0, k)
    return len(results)

# --- submit ---

T = int(input())

for test_case in range(1, T + 1):
    n, k = map(int, input().split(' '))
    nums = list(map(int, input().split(' ')))

    result = solution(nums, k)
    print(f'#{test_case} {result}')


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(4, solution([1, 2, 1, 2], 3))


if __name__ == '__main__':
    unittest.main()
