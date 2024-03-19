'''
https://www.acmicpc.net/problem/1152
'''

import unittest


def solution(line_str):
    line_str = line_str.strip(' ')
    if len(line_str) == 0:
        return 0
    return len(line_str.split(' '))


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, solution('   '))
        self.assertEqual(6, solution('The Curious Case of Benjamin Button'))
        self.assertEqual(2, solution('  a a  '))
        self.assertEqual(6, solution('  The first character is a blank'))
        self.assertEqual(6, solution('he first character is a blank  '))
        self.assertEqual(6, solution('  he first character is a blank  '))

    def test_submit(self):
        print(solution(input()))


if __name__ == '__main__':
    unittest.main()
