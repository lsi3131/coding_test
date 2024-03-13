import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def merge_two_area(arr, left, mid, right):
    l_idx = left
    r_idx = mid + 1

    sort_arr = [0] * len(arr)
    s_idx = left

    while l_idx <= mid and r_idx <= right:
        if arr[l_idx] <= arr[r_idx]:
            sort_arr[s_idx] = arr[l_idx]
            l_idx += 1
        else:
            sort_arr[s_idx] = arr[r_idx]
            r_idx += 1
        s_idx += 1

    # 왼쪽이 먼저 완료 -> 오른쪽 마저 merge
    if l_idx > mid:
        for i in range(r_idx, right + 1):
            sort_arr[s_idx] = arr[i]
            s_idx += 1
    # 오른쪽 먼저 완료 -> 왼쪽 마저 merge
    else:
        for i in range(l_idx, mid + 1):
            sort_arr[s_idx] = arr[i]
            s_idx += 1

    for i in range(left, right + 1):
        arr[i] = sort_arr[i]


def merge_sort(arr, left, right):
    if left < right:
        mid = (right + left) // 2

        # 좌, 우 분할 정복
        merge_sort(arr, left, mid)
        merge_sort(arr, mid + 1, right)

        # 분할 된 리스트 병합
        merge_two_area(arr, left, mid, right)


def sort(arr: list):
    merge_sort(arr, 0, len(arr) - 1)
    return arr


# 테스트용 리스트
print(sort([8, 2, 3, 7, 1, 5, 4, 6]))
print(sort([70, 89, 95, 34, 74, 56, 96, 70, 84, 33]))


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([1, 2, 3, 4, 5], sort([3, 2, 4, 5, 1]))
        self.assertEqual([1, 1, 2, 2, 3, 4, 5], sort([3, 2, 4, 5, 1, 1, 2]))


if __name__ == '__main__':
    unittest.main()
