import collections
import unittest


class MyStack(object):
    def __init__(self):
        self.q = collections.deque()

    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


class Test(unittest.TestCase):
    def test_example1(self):
        s = MyStack()
        s.push(1)
        self.assertEqual(1, s.top())
        s.push(2)
        self.assertEqual(2, s.top())
        self.assertEqual(2, s.pop())
        self.assertFalse(s.empty())


if __name__ == '__main__':
    unittest.main()
