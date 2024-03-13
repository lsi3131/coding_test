import unittest


def solution(height: list):
    left, right = 0, len(height) - 1
    max_left = max_right = 0
    volume = 0
    while left < right:
        max_left = max(max_left, height[left])
        max_right = max(max_right, height[right])
        if max_left <= max_right:
            volume += max_left - height[left]
            left += 1
        else:
            volume += max_right - height[right]
            right -= 1

    return volume


class TestProblem8(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(6, solution([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))
        s1 = 'aba'

    def test_stack(self):
        data = [1, 2, 3]
        data1 = []
        print(data[-1])

        in_while = False
        while data1:
            in_while = True

        if in_while:
            print('in while')
        else:
            print('not in while')

    def test_stack2(self):
        s = [1, 2, 3, 4, 5]
        while s:
            print(s[-1])
            s.pop()

            if not len(s):
                print('not len(s)')
                break


if __name__ == '__main__':
    unittest.main()
