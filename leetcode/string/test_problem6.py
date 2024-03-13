import unittest


def solution(s: str):
    if len(s) < 2 or s == s[::-1]:
        return s

    def expand(s, left, right):
        while left >= 0 and right <= len(s) - 1 and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]

    result = ''
    for i in range(len(s)):
        result = max(
            result,
            expand(s, i, i + 1),
            expand(s, i, i + 2),
            key=len
        )

    return result


class TestProblem6(unittest.TestCase):
    def test_example1(self):
        s1 = 'aba'
        s2 = 'abacbbc'
        s3 = 'babad'
        s4 = 'cbbd'
        s5 = 'aaabbbaaa'
        self.assertEqual('aba', solution(s1))
        self.assertEqual('cbbc', solution(s2))
        self.assertEqual('bab', solution(s3))
        self.assertEqual('bb', solution(s4))
        self.assertEqual('aaabbbaaa', solution(s5))

    def test_default(self):
        s = 'abcd'
        print("s[1:1] len = {}".format(len(s[1:1])))
        print("s[1:2] len = {}".format(len(s[1:2])))
        print("s[4:5] len = {}".format(len(s[4:5])))
        print("s[4:4] len = {}".format(len(s[4:4])))

    def test_slice_copy(self):
        s = 'abc'
        s_copy = s[1:]
        print(s_copy[::-1])

    def test_range(self):
        for i in range(0, 10):
            print(i)


if __name__ == '__main__':
    unittest.main()
