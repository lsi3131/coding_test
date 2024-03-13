import collections
import unittest


def solution(inputs: list[str]):
    d = collections.defaultdict(list)
    for input in inputs:
        print(sorted(input))
        key = ''.join(sorted(input))
        d[key].append(input)

    return list(d.values())


class TestProblem5(unittest.TestCase):
    def test_example1(self):
        inputs = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
        self.assertEqual([['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']], solution(inputs))
        print(solution(inputs))

    def test_sort_as_lambda(self):
        d = ['cfe', 'cea', 'abc']
        new_data = sorted(d, key=lambda x: (x[0], x[-1]))
        print(new_data)


if __name__ == '__main__':
    unittest.main()
