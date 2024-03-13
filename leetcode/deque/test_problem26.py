import unittest
from mycollections import *


def solution(nums: list):
    return []


class BiListNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class MyCircularDeque(object):

    def __init__(self, k):
        self.head, self.tail = BiListNode(None), BiListNode(None)
        self.len, self.k = 0, k
        self.head.right, self.tail.left = self.tail, self.head

    def _insert(self, node, value):
        if self.len == self.k:
            return False

        new_node = BiListNode(value)
        n = node.right
        node.right = new_node
        new_node.left, new_node.right = node, n
        n.left = new_node
        self.len = self.len + 1
        return True

    def _del(self, node: BiListNode):
        if self.len <= 0:
            return False

        n = node.right.right
        node.right = n
        n.left = node
        self.len = self.len - 1
        return True

    def insertFront(self, value):
        return self._insert(self.head, value)

    def insertLast(self, value):
        return self._insert(self.tail.left, value)

    def deleteFront(self):
        return self._del(self.head)

    def deleteLast(self):
        return self._del(self.tail.left.left)

    def getFront(self):
        return self.head.right.val if self.len else -1

    def getRear(self):
        return self.tail.left.val if self.len else -1

    def isEmpty(self):
        return self.len == 0

    def isFull(self):
        return self.len == self.k


class Test(unittest.TestCase):
    def test_example1(self):
        d = MyCircularDeque(4)
        self.assertEqual(-1, d.getRear())
        self.assertTrue(-1, d.getFront())

        self.assertTrue(d.insertFront(1))  # 1
        self.assertEqual([1], bilistnode_to_list(d.head))

        self.assertTrue(d.insertFront(4))  # 4,1
        self.assertEqual([4, 1], bilistnode_to_list(d.head))

        self.assertTrue(d.insertLast(3))  # 4,1,3
        self.assertEqual([4, 1, 3], bilistnode_to_list(d.head))

        self.assertTrue(d.insertLast(5))  # 4,1,3,5
        self.assertEqual([4, 1, 3, 5], bilistnode_to_list(d.head))

        self.assertFalse(d.insertLast(5))  # 4,1,3,5
        self.assertTrue(d.isFull())

        self.assertEqual(4, d.getFront())

        self.assertTrue(d.deleteFront())
        self.assertEqual([1, 3, 5], bilistnode_to_list(d.head))

        self.assertTrue(d.deleteLast())
        self.assertEqual([1, 3], bilistnode_to_list(d.head))

        self.assertTrue(d.deleteFront())
        self.assertEqual([3], bilistnode_to_list(d.head))

        self.assertTrue(d.deleteFront())
        self.assertEqual([], bilistnode_to_list(d.head))

        self.assertTrue(d.isEmpty())


if __name__ == '__main__':
    unittest.main()
