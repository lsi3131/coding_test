# https://www.acmicpc.net/problem/9012

import unittest

'''
3
ABAB
AABB
ABBA

3
AAA
AA
AB

1
ABBABB

1
ABABBABA
'''


def solution(s_list: list[str]):
    cnt = 0
    for s in s_list:
        stack = []
        for i in range(len(s)):
            if stack:
                if s[i] == stack[-1]:
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])

        if not stack:
            cnt += 1
    return cnt

t = int(input())
s_list = [input() for _ in range(t)]
print(solution(s_list))


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, solution(['AAA']))
        self.assertEqual(2, solution(['ABAB', 'AABB', 'ABBA']))
        self.assertEqual(1, solution(['AAA', 'AA', 'AB']))
        self.assertEqual(1, solution(['ABBABB']))
        self.assertEqual(1, solution(['ABBBBABAAB']))
        self.assertEqual(1, solution(['ABABBABA']))


if __name__ == '__main__':
    unittest.main()
