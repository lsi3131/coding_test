import collections
import unittest
import re


def solution(s : str, banned : list[str]):
    words = [word for word in re.sub('[^\w]', ' ', s).lower().split() if word not in banned]

    counters = collections.Counter(words)
    print(counters.most_common(1))
    print(counters.most_common(1)[0][0])

    return counters.most_common(1)[0][0]

class TestProblem3(unittest.TestCase):
    def test_example1(self):
        s = 'Bob hit a ball, the hit BALL flew after was hit.'
        banned = ['hit']
        self.assertEquals('ball', solution(s, banned))

    def test_regex(self):
        s = '..,,abc,def...'
        result = re.sub(r'[^\w]', ' ', s)
        self.assertEqual(['abc', 'def'], result.split())
        # str = self.make_rand_str(1000000)
        # self.solution(str)
        # self.solution2(array(str))


if __name__ == '__main__':
    unittest.main()
