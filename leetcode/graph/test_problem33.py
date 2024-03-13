import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://leetcode.com/problems/letter-combinations-of-a-phone-number/description/
def letterCombinations(digits: str):
    if len(digits) == 0:
        return []

    dials = {
        '2': 'abc', '3': 'def',
        '4': 'ghi', '5': 'jkl', '6': 'mno',
        '7': 'pqrs', '8': 'tuv', '9': 'wxyz',
    }

    results = []

    def dfs(i, comb: str):
        if len(digits) == len(comb):
            results.append(comb)
            return

        num = digits[i]
        dial = dials[num]
        for j in range(len(dial)):
            dfs(i + 1, comb + dial[j])

    dfs(0, '')

    return results


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([], letterCombinations(''))
        self.assertEqual(['a', 'b', 'c'], letterCombinations('2'))
        self.assertEqual(['aa', 'ab', 'ac', 'ba', 'bb', 'bc', 'ca', 'cb', 'cc'], letterCombinations('22'))
        self.assertEqual(['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'], letterCombinations('23'))
        self.assertEqual(
            ['adg', 'adh', 'adi', 'aeg', 'aeh', 'aei', 'afg', 'afh', 'afi', 'bdg', 'bdh', 'bdi', 'beg', 'beh', 'bei',
             'bfg', 'bfh', 'bfi', 'cdg', 'cdh', 'cdi', 'ceg', 'ceh', 'cei', 'cfg', 'cfh', 'cfi'],
            letterCombinations('234'))
        self.assertEqual(['gw', 'gx', 'gy', 'gz', 'hw', 'hx', 'hy', 'hz', 'iw', 'ix', 'iy', 'iz'],
                         letterCombinations('49'))


if __name__ == '__main__':
    unittest.main()
