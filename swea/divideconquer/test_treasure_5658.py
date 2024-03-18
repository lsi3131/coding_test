'''
2
12 10
1B3B3B81F75E
16 2
F53586D76286B2D8
'''
import unittest
import collections


def solution(lock_nums: collections.deque, k):
    num_set = set()

    divide = len(lock_nums) // 4

    while True:
        should_rotate = False
        for i in range(0, len(lock_nums), divide):
            num = []
            for j in range(i, i + divide):
                num.append(lock_nums[j])
            num_tuple = tuple(num)
            if num_tuple not in num_set:
                num_set.add(num_tuple)
                should_rotate = True
        if not should_rotate:
            break

        lock_nums.appendleft(lock_nums.pop())

    sorted_nums = sorted(list(num_set), reverse=True)
    hex_str = ''.join(sorted_nums[k - 1])
    return int(hex_str, 16)


results = []
T = int(input())
for testcase in range(1, T + 1):
    N, K = map(int, input().split())
    lock_nums = collections.deque(input())
    result = solution(lock_nums, K)
    print(f'#{testcase} {result}')


class Test(unittest.TestCase):
    def test_example1(self):
        nums = collections.deque('1B3B3B81F75E')
        print(solution(nums, 10))
        nums = collections.deque('F53586D76286B2D8')
        print(solution(nums, 2))

        pass


if __name__ == '__main__':
    unittest.main()
