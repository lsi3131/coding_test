import collections
import heapq

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://www.acmicpc.net/problem/1931

def solution(meetings: list):
    meetings.sort(key=lambda x: (x[1], x[0]))

    count = 0
    last_end = 0
    for start, end in meetings:
        if last_end <= start:
            last_end = end
            count += 1

    return count


### submit ###
n = int(input())
meetings = []
for _ in range(n):
    start, end = map(int, input().split(' '))
    meetings.append((start, end))

print(solution(meetings))


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(4, solution(
            [[1, 4], [3, 5], [0, 6], [5, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]))
        self.assertEqual(4, solution(
            [[1, 4], [3, 5], [0, 6], [4, 7], [3, 8], [5, 9], [6, 10], [8, 11], [8, 12], [2, 13], [12, 14]]))

    def test_submit(self):
        pass


if __name__ == '__main__':
    unittest.main()
