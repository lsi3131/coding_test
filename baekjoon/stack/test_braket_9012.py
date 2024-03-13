# https://www.acmicpc.net/problem/9012

import unittest

'''
6
(())())
(((()())()
(()())((()))
((()()(()))(((())))()
()()()()(()()())()
(()((())()(

3
((
))
())(()
'''


def find_vps(s: str):
    if len(s) < 2:
        return False
    stack = []

    for ch in s:
        if ch == '(':
            stack.append(ch)
        elif ch == ')':
            if len(stack) == 0:
                return False
            # '('가 존재할 경우 pop한다.
            stack.pop()

    # stack에 '('가 남아 있으면 닫혀있지 않는다는 뜻. 실패
    return len(stack) == 0


def solution(s_list: list[str]):
    result = ['YES' if find_vps(s) else 'NO' for s in s_list]
    return result


t = int(input())
s_list = [input() for _ in range(t)]
results = solution(s_list)
for r in results:
    print(r)

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertFalse(find_vps(''))
        self.assertTrue(find_vps('()'))
        self.assertFalse(find_vps('(('))
        self.assertFalse(find_vps('())'))


if __name__ == '__main__':
    unittest.main()
