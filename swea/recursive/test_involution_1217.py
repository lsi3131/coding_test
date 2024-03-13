import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

'''
1
9 8
2
2 8
'''


def involution(n, m):
    print(f'n={n}, m={m}')
    if m < 2:
        return n

    result = n * involution(n, m - 1)
    print(result)
    return result


T = 10
for test_case in range(1, T + 1):
    t_num = int(input())
    n, m = map(int, input().split(' '))

    result = involution(n, m)
    print(f'#{test_case} {result}')


class Test(unittest.TestCase):
    def test_example1(self):
        pass
        # self.assertEqual(4, solution([1, 2, 1, 2], 3))


if __name__ == '__main__':
    unittest.main()
