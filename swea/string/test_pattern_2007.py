# https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV5P1kNKAl8DFAUq

import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

'''
sample
3
KOREAKOREAKOREAKOREAKOREAKOREA
SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA
GALAXYGALAXYGALAXYGALAXYGALAXY
'''

def is_pattern(s: str, pattern: str):
    step = len(pattern)
    end = len(s) - len(pattern)
    for i in range(0, end + 1, step):
        if s[i:i + step] != pattern:
            return False

    return True


def solution(s: str):
    for i in range(len(s)):
        pattern = s[0:i + 1]
        if is_pattern(s, pattern):
            return len(pattern)

    return 0


# --- submit ----
T = int(input())

for test_case in range(1, T + 1):
    s = input()

    result = solution(s)
    print(f'#{test_case} {result}')


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(is_pattern('aa', 'a'))
        self.assertFalse(is_pattern('abcabc', 'ab'))
        self.assertTrue(is_pattern('abcabc', 'abc'))
        self.assertTrue(is_pattern('abcabca', 'abc'))

    def test_solution1(self):
        self.assertEqual(5, solution('KOREAKOREAKOREAKOREAKOREAKOREA'))
        self.assertEqual(7, solution('SAMSUNGSAMSUNGSAMSUNGSAMSUNGSA'))
        self.assertEqual(6, solution('GALAXYGALAXYGALAXYGALAXYGALAXY'))


if __name__ == '__main__':
    unittest.main()
