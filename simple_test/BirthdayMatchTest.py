import collections
import unittest
import random
import string
import re
from collections import *
from ElapedTimer import *
from mycollections import *


def solution(nums: list):
    return []


class Test(unittest.TestCase):
    def test_example1(self):
        TRIALS = 100000
        same_birthday = 0

        for _ in range(TRIALS):
            birthdays = []

            for i in range(57):
                birthday = random.randint(1, 365)
                if birthday in birthdays:
                    same_birthday += 1
                    break
                birthdays.append(birthday)

        print(f'{same_birthday / TRIALS * 100}%')


if __name__ == '__main__':
    unittest.main()
