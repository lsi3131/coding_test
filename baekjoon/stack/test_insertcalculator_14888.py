# https://www.acmicpc.net/problem/14888
import sys
import unittest

'''
2
5 6
0 0 1 0

3
3 4 5
1 0 1 0

6
1 2 3 4 5 6
2 1 1 1
'''

import sys
import itertools


def solution(nums, operators):
    op_list = []
    op_list += '+' * operators[0]
    op_list += '-' * operators[1]
    op_list += '*' * operators[2]
    op_list += '/' * operators[3]

    op_combs = list(itertools.permutations(op_list, len(op_list)))

    max_result, min_result = -sys.maxsize, sys.maxsize
    for op_comb in op_combs:
        result = nums[0]
        for op_idx in range(len(op_comb)):
            num_idx = op_idx + 1
            op = op_comb[op_idx]
            num = nums[num_idx]
            if op == '+':
                result += num
            elif op == '-':
                result -= num
            elif op == '*':
                result *= num
            elif op == '/':
                result = int(result / num)

        max_result = max(max_result, result)
        min_result = min(min_result, result)

    return max_result, min_result


n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_value, min_value = solution(nums, operators)
print(max_value)
print(min_value)


class Test(unittest.TestCase):
    def test_example1(self):
        pass


if __name__ == '__main__':
    unittest.main()
