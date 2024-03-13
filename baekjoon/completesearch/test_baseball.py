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
def create_num_flag_table():
    num_flag_table = [True] * 1000
    for num in range(123, 1000):
        num_str = str(num)

        # 중복된 숫자가 있으면 제거 - ex) 144, 211, 331...
        if num_str[0] == num_str[1] or num_str[1] == num_str[2] or num_str[2] == num_str[0]:
            num_flag_table[num] = False

        # 0이 포함된 숫자 조합 제거 - ex) 150, 200, 401
        if num_str[0] == '0' or num_str[1] == '0' or num_str[2] == '0':
            num_flag_table[num] = False

    return num_flag_table


def uncheck_num_flag_table(num_flag_table, target_num, strike, ball):
    target_num_str = str(target_num)

    for cur_num in range(123, 1000):
        # 이미 False 플래그된 숫자는 pass한다.
        if not num_flag_table[cur_num]:
            continue

        cur_num_str = str(cur_num)
        cur_strike = 0
        cur_ball = 0

        # j, k는 각각 입력 숫자 문자열, 현재 순회 중인 숫자 문자열의 포인터이다.
        # 각각의 for loop로 순회한 후 각 포인터에 해당하는 문자를 비교한다.
        # 문자가 동일한 경우 다음과 같이 진행한다.
        # j == k인 경우 포인터 위치가 일치하므로 strike, 다른 위치에 있는 경우 ball이다.
        # 각각 조건에 일치하는 strike, ball의 카운트를 증가한다.
        for j in range(3):
            for k in range(3):
                if target_num_str[j] == cur_num_str[k]:
                    if j == k:
                        cur_strike += 1
                    else:
                        cur_ball += 1

        # 현재 숫자가 전달한 strike, ball 개수와 일치하는지 확인힌다.
        # 둘 중 하나라도 일치하지 않으면 조건에 맞지 않는 숫자이므로 False 플래그를 설정한다
        if not (cur_strike == strike and cur_ball == ball):
            num_flag_table[cur_num] = False


def solution(game_data_list: list):
    num_flag_table = create_num_flag_table()

    for num, strike, ball in game_data_list:
        uncheck_num_flag_table(num_flag_table, num, strike, ball)

    # 123~999까지의 True인 개수를 더한다.
    count = sum([1 for i in range(123, 1000) if num_flag_table[i]])
    return count


##--------- submit ---------
# n = int(input())
# game_data_list = [map(int, input().split(' ')) for _ in range(n)]
# print(solution(game_data_list))


class Test(unittest.TestCase):
    def test_example(self):
        self.assertEqual(2, solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))

    # exists 한 숫자를

    # self.assertEqual(, get_num_flag('123', 1, 1))
    # print(num_flag)

    def test_1_ball_0_strike(self):
        result = max([2,2,1])
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
