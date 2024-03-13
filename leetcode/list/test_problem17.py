import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def solution(head: ListNode):
    if head is None or head.next is None:
        return head

    prev = root = ListNode(None)
    node = head

    while node and node.next:
        prev.next, node.next.next, node.next = node.next, node, node.next.next
        prev, node = node, node.next

    return root.next


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([2, 1, 4, 3], listnode_to_list(solution(create_linkedlist([1, 2, 3, 4]).head)))
        self.assertEqual([2, 1], listnode_to_list(solution(create_linkedlist([1, 2]).head)))
        self.assertEqual([], listnode_to_list(solution(create_linkedlist([]).head)))
        self.assertEqual([1], listnode_to_list(solution(create_linkedlist([1]).head)))
        self.assertEqual([2, 1, 3], listnode_to_list(solution(create_linkedlist([1, 2, 3]).head)))


if __name__ == '__main__':
    unittest.main()
