import unittest
import random
import string

def solution(s : list[str]):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1


class TestProblem2(unittest.TestCase):
    def test_example1(self):
        s1 = list('abc')
        s2 = list('123abc')

        solution(s1)
        solution(s2)
        self.assertEqual(list('cba'), s1)
        self.assertEqual(list('cba321'), s2)

    def test_performance(self):
        str = self.make_rand_str(1000000)

    def make_rand_str(self, size):
        characters = string.ascii_letters + string.digits
        s = []

        for i in range(size):
            ch = random.choice(characters)
            s.append(ch)

        return ''.join(s)


if __name__ == '__main__':
    unittest.main()
