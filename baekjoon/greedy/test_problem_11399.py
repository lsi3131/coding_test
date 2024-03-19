import collections
import heapq

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://www.acmicpc.net/problem/11047

def solution(times: list):
    heap = []
    for i in range(len(times)):
        heapq.heappush(heap, (times[i], i))

    order_idx_list = []
    while heap:
        time, idx = heapq.heappop(heap)
        order_idx_list.append(idx)

    accu = 0
    result = []
    for idx in order_idx_list:
        accu += times[idx]
        result.append(accu)

    return sum(result)


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, solution([]))
        self.assertEqual(3, solution([3]))
        self.assertEqual(32, solution([3, 1, 4, 3, 2]))

    def test_submit(self):
        pass
        # count = input()
        # words = []
        # for _ in range(int(count)):
        #     words.append(input())
        # print(solution(words))


if __name__ == '__main__':
    unittest.main()
