import unittest


def twoSum(nums: list[int], target: int) -> list[int]:
    dict_nums = {}
    for i in range(len(nums)):
        dict_nums[nums[i]] = i

    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in dict_nums and dict_nums[complement] != i:
            return [i, dict_nums[complement]]

    return []


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([0, 1], twoSum([2, 7, 11, 15], 9))
        self.assertEqual([1, 2], twoSum([2, 7, 11, 15], 18))
        self.assertEqual([2, 3], twoSum([2, 7, 11, 15], 26))


if __name__ == '__main__':
    unittest.main()
