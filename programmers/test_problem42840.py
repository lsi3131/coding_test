import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def solution(answers: list):
    person1 = [1, 2, 3, 4, 5]
    person2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    val = [0, 0, 0]
    for i in range(len(answers)):
        if person1[i % len(person1)] == answers[i]:
            val[0] += 1

        if person2[i % len(person2)] == answers[i]:
            val[1] += 1

        if person3[i % len(person3)] == answers[i]:
            val[2] += 1

    answer = []
    for i in range(len(val)):
        if val[i] == max(val):
            answer.append(i + 1)

    return answer


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([1], solution([1, 2, 3, 4, 5]))


if __name__ == '__main__':
    unittest.main()
