'''
https://www.acmicpc.net/problem/1316

3
happy
new
year

4
aba
abab
abcabc
'''
import unittest

def solution(words):
    if words is None:
        return 0

    def is_sequence_word(word):
        if word is None or len(word) == 0:
            return False

        ch_set = set()
        cur_ch = ''
        for ch in word:
            if ch != cur_ch:
                if ch in ch_set:
                    return False
                ch_set.add(ch)
                cur_ch = ch
        return True

    target = [word for word in words if is_sequence_word(word)]
    return len(target)


count = input()
words = []
for _ in range(int(count)):
    words.append(input())
print(solution(words))

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, solution(None))
        self.assertEqual(0, solution(['']))
        self.assertEqual(2, solution([None, '','a','ab']))
        self.assertEqual(1, solution(['ccazzzzbb']))
        self.assertEqual(0, solution(['aabbbccb']))
        self.assertEqual(0, solution([]))
        self.assertEqual(3, solution(['aa', 'b', 'cc']))
        self.assertEqual(3, solution(['happy', 'new', 'year']))
        self.assertEqual(1, solution(['aba', 'abab', 'abcabc', 'a']))
        self.assertEqual(1, solution(['z']))
        self.assertEqual(2, solution(['aaa', 'aazbz', 'babb', 'aazz', 'azbz', 'aabbaa', 'abacc', 'aba', 'zzaz']))


if __name__ == '__main__':
    unittest.main()
