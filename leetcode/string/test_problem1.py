import collections
import unittest
import random
import string
import re


def solution(s: str):
    s = s.lower()
    s = re.sub('[^a-z0-9]', '', s)

    return s == s[::-1]


def solution2(s: str):
    s = s.lower()

    s_list = collections.deque()
    for ch in s:
        if ch.isalnum():
            s_list.append(ch)

    while len(s_list) >= 2:
        d1 = s_list.popleft()
        d2 = s_list.pop()
        if d1 != d2:
            return False

    return True


class TestProblem2(unittest.TestCase):
    def test_example1(self):
        s1 = 'abba'
        s2 = 'baaa'
        s3 = 'aBbA'
        s4 = 'a123*&321a'
        s5 = 'abcba'

        self.assertTrue(solution(s1))
        self.assertFalse(solution(s2))
        self.assertTrue(solution(s3))
        self.assertTrue(solution(s4))
        self.assertTrue(solution(s5))

        self.assertTrue(solution2(s1))
        self.assertFalse(solution2(s2))
        self.assertTrue(solution2(s3))
        self.assertTrue(solution2(s4))
        self.assertTrue(solution2(s5))

    def test_perfomance(self):
        d1 = self.make_palindrom(100000)

    def test_sample(self):
        strs = 'abc'
        self.assertEqual(3, len(strs))

    def make_palindrom(self, size):
        characters = string.ascii_letters + string.digits
        s = []
        if size % 2 == 1:
            ch = random.choice(characters)
            s.append(ch)

        mid = int(size / 2)
        for i in range(mid):
            ch = random.choice(characters)
            s.insert(0, ch)
            s.append(ch)

        return ''.join(s)

    def test_random_str(self):
        s = self.make_palindrom(10)
        print(s)

    def test_tolower(self):
        s3 = 'aBbA'
        solution2(s3)


if __name__ == '__main__':
    unittest.main()
