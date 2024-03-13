import unittest


class MyQueue(object):
    def __init__(self):
        self.st = []

    def push(self, x):
        tmp_st = []
        while self.st:
            tmp_st.append(self.st.pop())
        tmp_st.append(x)

        while tmp_st:
            self.st.append(tmp_st.pop())

    def pop(self):
        return self.st.pop()

    def peek(self):
        return None if len(self.st) == 0 else self.st[-1]

    def empty(self):
        return len(self.st) == 0


class Test(unittest.TestCase):
    def test_example1(self):
        myQueue = MyQueue()
        self.assertTrue(myQueue.empty())
        myQueue.push(1)  # queue is: [1]
        self.assertFalse(myQueue.empty())

        myQueue.push(2)  # queue is: [1, 2] (leftmost is front of the queue)
        self.assertEqual(1, myQueue.peek())

        self.assertEqual(1, myQueue.pop())
        self.assertEqual(2, myQueue.peek())
        self.assertFalse(myQueue.empty())

        self.assertEqual(2, myQueue.pop())
        self.assertTrue(myQueue.empty())

        self.assertIsNone(myQueue.peek())


if __name__ == '__main__':
    unittest.main()
