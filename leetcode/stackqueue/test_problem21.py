import unittest
from collections import *


def removeDuplicateLetters(s: str):
    stack, seen = [], set()
    counter = Counter(s)

    for ch in s:
        counter[ch] -= 1

        if ch in seen:
            continue

        while stack and ch < stack[-1] and counter[stack[-1]] > 0:
            seen.remove(stack[-1])
            stack.pop()

        seen.add(ch)
        stack.append(ch)

    return ''.join(stack)


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual('a', removeDuplicateLetters('a'))
        self.assertEqual('a', removeDuplicateLetters('aa'))
        self.assertEqual('ab', removeDuplicateLetters('aabb'))
        self.assertEqual('ab', removeDuplicateLetters('bab'))
        self.assertEqual('abc', removeDuplicateLetters('bcabc'))


if __name__ == '__main__':
    unittest.main()
