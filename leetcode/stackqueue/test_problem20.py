import unittest


def solution(s: str):
    closes = [')', ']', '}']
    pairs = {'(': ')', '[': ']', '{': '}'}
    st = []
    for ch in s:
        if ch in pairs:
            st.append(ch)
        if ch in closes:
            if len(st) == 0:
                return False

            if pairs[st.pop()] != ch:
                return False

    return len(st) == 0


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertTrue(solution(""))
        self.assertFalse(solution("("))
        self.assertTrue(solution("()"))
        self.assertTrue(solution("()[]{}"))
        self.assertFalse(solution("(}"))
        self.assertFalse(solution("(abc{def[123}"))
        self.assertTrue(solution("(abc{def[123]def}abc)"))


if __name__ == '__main__':
    unittest.main()
