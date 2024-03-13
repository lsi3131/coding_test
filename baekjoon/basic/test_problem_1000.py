import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://www.acmicpc.net/problem/1000

def solution(n1, n2):
    return n1 + n2

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, solution(1, 2))

    def submit(self):
        n1, n2 = map(int, input().split())
        print(solution(n1, n2))


if __name__ == '__main__':
    unittest.main()
