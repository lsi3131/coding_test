import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def reverse_connect(head: ListNode):
    if not head:
        return []

    prev = None
    node = head
    while node:
        node.next, node, prev = prev, node.next, node

    return prev


class Test(unittest.TestCase):
    def test_example1(self):
        l1 = create_linkedlist([1, 2, 3, 4, 5])
        self.assertEqual([5, 4, 3, 2, 1], listnode_to_list(reverse_connect(l1.head)))


if __name__ == '__main__':
    unittest.main()
