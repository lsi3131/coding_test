import unittest


def solution(logs : list[str]):
    digits, letters = [], []

    for log in logs:
        if log.split()[1].isdigit():
            digits.append(log)
        else:
            letters.append(log)

    letters.sort(key = lambda x:(x.split()[1:], x.split()[0]))

    return letters + digits


class TestProblem3(unittest.TestCase):
    def test_example1(self):
        input = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let2 own kit dig', 'let3 art zero']
        out = ['let1 art can', 'let3 art zero', 'let2 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']

        self.assertEqual(out, solution(input))
        print(solution(input))

        input1 = ['dig1 8 1 5 1', 'let1 art can', 'dig2 3 6', 'let3 own kit dig', 'let2 own kit dig']
        out1 = ['let1 art can', 'let2 own kit dig', 'let3 own kit dig', 'dig1 8 1 5 1', 'dig2 3 6']
        self.assertEqual(out1, solution(input1))
        print(solution(input1))

    def test_performance(self):
        pass
        # str = self.make_rand_str(1000000)
        # self.solution(str)
        # self.solution2(array(str))

    def test_split_and_slice_and_sort(self):
        s = '1 c b a'
        s_list = s.split()[1:]
        self.assertEqual(['c', 'b', 'a'], s_list)
        s_list.sort()
        self.assertEqual(['a', 'b', 'c'], s_list)


if __name__ == '__main__':
    unittest.main()
