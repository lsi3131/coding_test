import unittest


def solution(nums: list):
    if len(nums) < 3:
        return []

    result = []
    nums.sort()
    for i in range(0, len(nums) - 2):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        left = i + 1
        right = len(nums) - 1

        print('left={}, right={}, i={}'.format(left, right, i))

        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[i], nums[left], nums[right]])
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result


class TestProblem8(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([], solution([1, 2]))
        nums = [-1, 0, 1, 2, -1, -4]
        self.assertEqual([[-1, 0, 1], [-1, -1, 2]].sort(), solution(nums).sort())

    def test_stack(self):
        d = [1, 2, 3, 4]
        for i in range(len(d) - 2):
            print(i)


if __name__ == '__main__':
    unittest.main()
