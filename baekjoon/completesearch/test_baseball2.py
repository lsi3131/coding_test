import collections
import itertools
import math

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

# https://www.acmicpc.net/problem/2503

import itertools


def solution(data_list: list):
    possible_num_comb_list = list(itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))
    for num, strike, ball in data_list:
        num_comb = list(map(int, str(num)))
        next_possible_num_comb_list = []
        for possible_num_comb in possible_num_comb_list:
            tmp_strike, tmp_ball = 0, 0

            for i in range(len(num_comb)):
                if num_comb[i] in possible_num_comb:
                    if i == possible_num_comb.index(num_comb[i]):
                        tmp_strike += 1
                    else:
                        tmp_ball += 1

            if strike == tmp_strike and ball == tmp_ball:
                next_possible_num_comb_list.append(possible_num_comb)

        possible_num_comb_list = next_possible_num_comb_list[:]

    return len(possible_num_comb_list)


#--------- submit ---------
n = int(input())
game_data_list = [map(int, input().split(' ')) for _ in range(n)]
print(solution(game_data_list))


class Test(unittest.TestCase):
    def test_example(self):
        self.assertEqual(2, solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))

    def test_1_ball_0_strike(self):
        result = max([2, 2, 1])
        print(result)
        pass

    def test_permute_comb(self):
        pass

    def test_range(self):
        pass

    def test_remove(self):
        pass


if __name__ == '__main__':
    unittest.main()
