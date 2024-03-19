'''
https://school.programmers.co.kr/learn/courses/30/lessons/12977
'''
import unittest


def so(N):
    for i in range(2, int(N ** 0.5) + 1):
        if N % i == 0:
            return False
    return True


cnt = 0


def func(nums, li=[]):
    global cnt
    if len(li) == 3:
        if so(sum(li)):
            cnt += 1
        return
    for n, i in enumerate(nums):
        li.append(i)
        func(nums[n + 1:], li)
        li.remove(i)


def solution(nums):
    global cnt
    cnt = 0
    func(nums)
    return cnt


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, solution([1, 2, 3, 4]))
        self.assertEqual(4, solution([1, 2, 7, 6, 4]))


if __name__ == '__main__':
    unittest.main()
