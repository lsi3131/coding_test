import unittest
from collections import *
from mycollections import *


def solution(l1: ListNode, l2: ListNode) -> ListNode:
    root = head = ListNode(None)

    carry = 0
    while l1 or l2 or carry:
        adden = 0
        if l1:
            adden += l1.val
            l1 = l1.next
        if l2:
            adden += l2.val
            l2 = l2.next

        carry, val = divmod(adden + carry, 10)
        head.next = ListNode(val)
        head = head.next

    return root.next


class Test(unittest.TestCase):
    def test_example1(self):
        l1 = LinkedList()
        l2 = LinkedList()
        l1.append_list([2, 4, 3])
        l2.append_list([5, 6, 4])

        self.assertEqual([7, 0, 8], listnode_to_list(solution(l1.head, l2.head)))

        l1 = LinkedList()
        l2 = LinkedList()
        l1.append_list([9])
        l2.append_list([9])
        self.assertEqual([8, 1], listnode_to_list(solution(l1.head, l2.head)))

        l1 = LinkedList()
        l2 = LinkedList()
        l1.append_list([9, 9, 9])
        l2.append_list([9, 9, 9])
        self.assertEqual([8, 9, 9, 1], listnode_to_list(solution(l1.head, l2.head)))

        l1 = LinkedList()
        l2 = LinkedList()
        l1.append_list([9, 9, 9, 9])
        l2.append_list([9])
        self.assertEqual([8, 0, 0, 0, 1], listnode_to_list(solution(l1.head, l2.head)))

        l1 = LinkedList()
        l2 = LinkedList()
        l1.append_list([9])
        l2.append_list([9, 9, 9, 9])
        self.assertEqual([8, 0, 0, 0, 1], listnode_to_list(solution(l1.head, l2.head)))

    def test_list(self):
        right = []
        d = deque()
        for i in range(5, -1, -1):
            # right.insert(len(right), i)
            right.insert(0, i)

        print(right)


if __name__ == '__main__':
    unittest.main()
