import unittest


def solution(nums: list):
    return sum(sorted(nums)[::2])


class Test(unittest.TestCase):
    def test_example1(self):
        nums1 = [4, 3, 1, 2]
        nums2 = [7, 2, 5, 5, 6, 1]
        self.assertEqual(4, solution(nums1))
        self.assertEqual(12, solution(nums2))


if __name__ == '__main__':
    unittest.main()
