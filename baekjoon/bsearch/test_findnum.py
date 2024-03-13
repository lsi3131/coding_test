import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

# https://www.acmicpc.net/problem/1920

import bisect

def solution(nums, find_nums):
    def binary_search(nums_arr, target):
        index = bisect.bisect_left(nums_arr, target)

        if index < len(nums_arr) and nums_arr[index] == target:
            return True

        return False

    nums.sort()

    result = [1 if binary_search(nums, find_num) else 0 for find_num in find_nums]
    return result


# --- submit ---
num_count = input()
nums = list(map(int, input().split()))
find_num_count = input()
find_nums = list(map(int, input().split()))

datas = solution(nums, find_nums)
for d in datas:
    print(d)


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([1, 1, 0, 0, 1], solution([4, 1, 5, 2, 3], [1, 3, 7, 9, 5]))

    def test_submit(self):
        nums = list(map(int, input().split()))
        find_nums = list(map(int, input().split()))

        datas = solution(nums, find_nums)
        for d in datas:
            print(d)


if __name__ == '__main__':
    unittest.main()
