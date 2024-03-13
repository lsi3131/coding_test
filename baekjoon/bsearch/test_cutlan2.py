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

def solution(lan_length_list: list, n):
    max_length = max(lan_length_list)
    result_length = 0
    low, high = 0, max_length
    while low <= high:
        count = 0
        mid = (low + high) // 2
        for length in lan_length_list:
            mid = max(1, mid)
            count += length // mid

        if count >= n:
            # 더 많이 개수가 남았다면 길이를 좀더 키워야한다.
            result_length = max(result_length, mid)
            low = mid + 1
        else:
            # 개수가 부족하면 길이를 줄여야한다.
            high = mid - 1

    return result_length


# --- submit ---
k, n = list(map(int, input().split()))
len_lengths = [int(input()) for _ in range(k)]
print(solution(len_lengths, n))


class Test(unittest.TestCase):
    def test_example1(self):
        d = [802, 743, 457, 539]
        self.assertEqual(200, solution(d, 11))
        self.assertEqual(1, solution([1, 1], 1))

    def test_submit(self):
        pass


if __name__ == '__main__':
    unittest.main()
