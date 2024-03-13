import unittest


def solution(nums: list):
    p = 1
    left, right = [], []
    # plus left
    for i in range(len(nums)):
        left.append(p)
        p *= nums[i]

    # plus right
    p = 1
    right = [0] * len(nums)
    for i in range(len(nums) - 1, 0 - 1, -1):
        right[i] = p
        p *= nums[i]

    result = []
    for i in range(len(nums)):
        result.append(left[i] * right[i])

    return result


class Test(unittest.TestCase):
    def test_example1(self):
        d = [1, 2, 3, 4]
        for i in range(len(d) - 1, -1, -1):
            print(d[i])

        self.assertEqual([24, 12, 8, 6], solution([1, 2, 3, 4]))


if __name__ == '__main__':
    unittest.main()
