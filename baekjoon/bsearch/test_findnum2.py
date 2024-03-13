import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

import bisect

# https://www.acmicpc.net/problem/1920

def solution(src_nums, target_nums):
    def binary_search(nums_arr, target):
        left, right = 0, len(nums_arr) - 1
        while left <= right:
            mid = (right + left) // 2
            mid_val = nums_arr[mid]
            if mid_val > target:
                right = mid - 1
            elif mid_val < target:
                left = mid + 1
            else:
                return True

        return False

    src_nums.sort()

    result = [1 if binary_search(src_nums, find_num) else 0 for find_num in target_nums]
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
