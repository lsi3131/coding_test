'''
55-50+40
10+20+30+40
'''

import unittest
import re


def solution(s: str):
    s_list = re.findall(r'\d+|[\+\-]', s)
    direction = 1
    result = 0
    for ch in s_list:
        if ch == '-':
            direction = -1
        elif ch == '+':
            pass
        else:
            result += int(ch) * direction

    return result


s = input()
print(solution(s))


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(-60, solution('0-50+10'))
        self.assertEqual(0, solution('0+10-10'))
        self.assertEqual(-35, solution('55-50+40'))
        self.assertEqual(-85, solution('55-50+40-50'))
        self.assertEqual(-95, solution('-55-40'))
        self.assertEqual(100, solution('10+20+30+40'))
        self.assertEqual(0, solution('00009-00009'))
