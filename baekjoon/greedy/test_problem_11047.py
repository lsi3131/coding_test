import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://www.acmicpc.net/problem/11047

def solution(amount, coins):
    if len(coins) == 0:
        return 0

    count = 0
    coin = coins.pop()
    while amount > 0:
        if amount < coin:
            if not coins:
                break
            coin = coins.pop()
        else:
            add_count, amount = divmod(amount, coin)
            count += add_count
            # --- 시간 초과 ----
            # amount -= coin
            # count += 1

    return count


# --- submit ----
line_count, amount = map(int, input().split(' '))
coins = [int(input()) for _ in range(line_count)]
print(solution(amount, coins))


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(6, solution(4200, [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]))
        self.assertEqual(12, solution(4790, [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]))
        self.assertEqual(7, solution(4201, [1, 5, 10, 50, 100, 500, 1000, 5000, 10000, 50000]))


if __name__ == '__main__':
    unittest.main()
