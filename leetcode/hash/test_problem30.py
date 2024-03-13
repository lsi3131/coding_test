import collections
import mycollections
import unittest
import random
import string
import re
from collections import *


def lengthOfLongestSubstring(s: str):
    used = {}
    max_length = 0
    start = 0
    for i, ch in enumerate(s):
        if ch in used and start <= used[ch]:
            start = used[ch] + 1
        else:
            max_length = max(max_length, i - start + 1)

        used[ch] = i

    return max_length


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, lengthOfLongestSubstring(''))
        self.assertEqual(2, lengthOfLongestSubstring('aab'))
        self.assertEqual(4, lengthOfLongestSubstring('abcbda'))
        self.assertEqual(3, lengthOfLongestSubstring('abcabcbb'))
        self.assertEqual(1, lengthOfLongestSubstring('bbbbb'))
        self.assertEqual(3, lengthOfLongestSubstring('pwwkew'))
        self.assertEqual(3, lengthOfLongestSubstring('dvdf'))


if __name__ == '__main__':
    unittest.main()
