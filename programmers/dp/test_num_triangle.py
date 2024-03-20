'''
https://school.programmers.co.kr/learn/courses/30/lessons/43105
'''

import unittest


def solution(triangle):
    for idx in range(len(triangle) - 1):
        cur = triangle[idx]
        next = triangle[idx + 1]
        temp = [0] * len(next)

        for i in range(len(cur)):
            temp[i] = max(temp[i], next[i] + cur[i])
            temp[i + 1] = max(temp[i + 1], next[i + 1] + cur[i])

        triangle[idx + 1] = temp

    return max(triangle[-1])


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(30, solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
