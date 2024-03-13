from mycollections import *
import unittest


def solution(head: ListNode):
    fast = slow = head
    rev = None
    while fast and fast.next:
        fast = fast.next.next
        slow.next, slow, rev = rev, slow.next, slow

    if fast:
        slow = slow.next

    while rev and rev.val == slow.val:
        rev = rev.next
        slow = slow.next

    return rev is None


class Test(unittest.TestCase):
    def test_list_node(self):
        self.assertTrue(solution(create_linkedlist([1, 2, 3, 2, 1]).head))
        self.assertTrue(solution(create_linkedlist([1, 2, 2, 1]).head))
        self.assertFalse(solution(create_linkedlist([1, 2, 2]).head))


if __name__ == '__main__':
    unittest.main()
