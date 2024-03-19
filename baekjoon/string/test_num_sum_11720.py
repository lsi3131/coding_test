'''
https://www.acmicpc.net/problem/11720
'''


import unittest

def solution(num_str):
    data_int_list = list(map(int, list(num_str)))
    return sum(data_int_list)


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, solution('0'))
        self.assertEqual(1, solution('1\n1'))
        self.assertEqual(15, solution('5\n54321'))
        self.assertEqual(7, solution('25\n7000000000000000000000000'))
        self.assertEqual(46, solution('11\n10987654321'))

    def test_submit(self):
        count = input()
        num_str = input()
        print(solution(num_str))


if __name__ == '__main__':
    unittest.main()
