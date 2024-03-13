import collections
import unittest
import random
import string
import re
from collections import *


def numJewelsInStones(jewels: str, stones: str):
    counter = Counter(stones)
    count = 0
    for jewel in jewels:
        count = count + counter[jewel]

    return count


def numJewelsInStones2(jewels: str, stones: str):
    print([st for st in stones])
    print([stone in jewels for stone in stones])
    return sum(stone in jewels for stone in stones)
    # counter = Counter(stones)
    # count = 0
    # for jewel in jewels:
    #     count = count + counter[jewel]
    #
    # return count


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, numJewelsInStones('aA', 'aAAbbbb'))
        self.assertEqual(3, numJewelsInStones2('aA', 'aAAbbbb'))

        self.assertEqual(5, sum([True, True, True, True, True, False, False]))


if __name__ == '__main__':
    unittest.main()
