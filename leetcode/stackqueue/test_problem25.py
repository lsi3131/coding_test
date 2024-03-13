import unittest


class MyCircularQueue(object):
    def __init__(self, k):
        self.q = [None] * k
        self.front = 0
        self.real = 0
        self.max_len = k

    def enQueue(self, value):
        if self.q[self.real] is not None:
            return False

        self.q[self.real] = value
        self.real = (self.real + 1) % self.max_len
        return True

    def deQueue(self):
        if self.q[self.front] is None:
            return False

        self.q[self.front] = None
        self.front = (self.front + 1) % self.max_len
        return True

    def Front(self):
        return -1 if self.isEmpty() else self.q[self.front]

    def Rear(self):
        return -1 if self.isEmpty() else self.q[self.real - 1]

    def isEmpty(self):
        return self.real == self.front and self.q[self.front] is None

    def isFull(self):
        return self.real == self.front and self.q[self.front] is not None


class Test(unittest.TestCase):
    def test_example1(self):
        q = MyCircularQueue(3)
        self.assertEqual(-1, q.Rear())
        self.assertEqual(-1, q.Front())
        self.assertFalse(q.deQueue())
        self.assertFalse(q.isFull())
        self.assertTrue(q.isEmpty())

        self.assertTrue(q.enQueue(1))
        self.assertEqual(1, q.Front())
        self.assertEqual(1, q.Rear())
        self.assertFalse(q.isEmpty())

        self.assertTrue(q.enQueue(2))
        self.assertEqual(1, q.Front())
        self.assertEqual(2, q.Rear())

        self.assertTrue(q.enQueue(3))
        self.assertEqual(1, q.Front())
        self.assertEqual(3, q.Rear())
        self.assertTrue(q.isFull())

        self.assertFalse(q.enQueue(4))

        self.assertTrue(q.deQueue())
        self.assertEqual(2, q.Front())
        self.assertEqual(3, q.Rear())

        self.assertTrue(q.enQueue(4))
        self.assertEqual(2, q.Front())
        self.assertEqual(4, q.Rear())

        q.deQueue()
        q.deQueue()
        q.deQueue()
        self.assertTrue(q.isEmpty())




if __name__ == '__main__':
    unittest.main()
