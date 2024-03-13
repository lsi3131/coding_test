# https://www.acmicpc.net/problem/14888

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


class Solution:
    def __init__(self):
        self.min_value, self.max_value = sys.maxsize, -sys.maxsize

    def do(self, nums, operators_count):
        add, minus, mul, div = operators_count

        def dfs(result, add, minus, mul, div, idx):
            if idx == len(nums):
                self.min_value = min(result, self.min_value)
                self.max_value = max(result, self.max_value)
                return

            if add > 0:
                dfs(result + nums[idx], add - 1, minus, mul, div, idx + 1)
            if minus > 0:
                dfs(result - nums[idx], add, minus - 1, mul, div, idx + 1)
            if mul > 0:
                dfs(result * nums[idx], add, minus, mul - 1, div, idx + 1)
            if div > 0:
                dfs(int(result / nums[idx]), add, minus, mul, div - 1, idx + 1)

        dfs(nums[0], add, minus, mul, div, 1)

        return self.max_value, self.min_value


n = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
max_value, min_value = Solution().do(nums, operators)
print(max_value)
print(min_value)


class Test(unittest.TestCase):
    def test_example1(self):
        pass


if __name__ == '__main__':
    unittest.main()
