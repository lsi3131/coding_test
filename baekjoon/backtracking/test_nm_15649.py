'''
https://www.acmicpc.net/problem/15649

3 1

4 2
'''
import unittest


def solution(n, m):
    results = []

    def dfs(path, cur_elements):
        if m == len(path):
            results.append(path)
            return

        for e in cur_elements:
            next_elements = cur_elements[:]
            next_elements.remove(e)
            dfs(path + [e], next_elements)

    dfs([], [i for i in range(1, n + 1)])

    return results


n, m = map(int, input().split())
nums_list = solution(n, m)
for nums in nums_list:
    p_str = ' '.join(map(str, nums))
    print(p_str)


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, 1)


if __name__ == '__main__':
    unittest.main()
