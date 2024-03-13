import collections
import mycollections
import unittest
import bisect
import random
import string
import re
from collections import *
from mycollections import *

# https://www.acmicpc.net/problem/1654
global result_height


def solution(lan_length_list: list, n):
    def binary(low, high, target_count):
        global result_height
        if high < low:
            return
        mid = (low + high) // 2
        count = 0
        mid = max(1, mid)
        for lan_length in lan_length_list:
            count += lan_length // mid

        if count > target_count:
            # res = mid
            binary(mid + 1, high, target_count)
        elif count == target_count:
            res = mid
            binary(mid + 1, high, target_count)
        else:
            binary(low, mid - 1, target_count)

        return res

    max_length = max(lan_length_list)
    result = binary(0, max_length, n)
    return result


# --- submit ---
k, n = list(map(int, input().split()))
len_lengths = [int(input()) for _ in range(k)]
print(solution(len_lengths, n))


class Test(unittest.TestCase):
    def test_example1(self):
        d = [802, 743, 457, 539]
        self.assertEqual(200, solution(d, 11))

    def test_submit(self):
        pass


if __name__ == '__main__':
    unittest.main()
