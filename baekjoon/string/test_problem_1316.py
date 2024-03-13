import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://www.acmicpc.net/problem/1316

# n = int(input())
# count=0
#
# for _ in range(n):
#     word = array(input())
#     for i in range(len(word)-1):
#         if word[i] == word[i+1]:
#             word[i] = '0'
#
#     while '0' in word:
#         word.remove('0')
#
#     if len(word)==len(set(word)):
#         count += 1
#
# print(count)

def solution(words):
    if words is None:
        return 0

    def is_sequence_word(word):
        if word is None or len(word) == 0:
            return False

        ch_set = set()
        cur_ch = ''
        for ch in word:
            if ch != cur_ch:
                if ch in ch_set:
                    return False
                ch_set.add(ch)
                cur_ch = ch
        return True

    target = [word for word in words if is_sequence_word(word)]
    return len(target)


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, solution(None))
        self.assertEqual(0, solution(['']))
        self.assertEqual(2, solution([None, '','a','ab']))
        self.assertEqual(1, solution(['ccazzzzbb']))
        self.assertEqual(0, solution(['aabbbccb']))
        self.assertEqual(0, solution([]))
        self.assertEqual(3, solution(['aa', 'b', 'cc']))
        self.assertEqual(3, solution(['happy', 'new', 'year']))
        self.assertEqual(1, solution(['aba', 'abab', 'abcabc', 'a']))
        self.assertEqual(1, solution(['z']))
        self.assertEqual(2, solution(['aaa', 'aazbz', 'babb', 'aazz', 'azbz', 'aabbaa', 'abacc', 'aba', 'zzaz']))

    def test_submit(self):
        count = input()
        words = []
        for _ in range(int(count)):
            words.append(input())
        print(solution(words))


if __name__ == '__main__':
    unittest.main()
