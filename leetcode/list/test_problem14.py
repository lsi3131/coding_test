import unittest
from mycollections import *


def merge_two_list(l1: ListNode, l2: ListNode) -> ListNode:
    if (not l1) or (l1.val > l2.val):
        l1,l2 = l2,l1

    if l1:
        l1.next = merge_two_list(l1.next, l2)

    return l1

class Test(unittest.TestCase):
    def test_example1(self):
        l1 = create_linkedlist([1, 2, 4])
        l2 = create_linkedlist([1, 3, 4])

        self.assertEqual([1, 1, 2, 3, 4, 4], listnode_to_list(merge_two_list(l1.head, l2.head)))

    def test_empty_two_list(self):
        print('')

    def test_range(self):
        d = [1, 2, 3, 4]
        for i in range(0, len(d), 2):
            print(d[i])


if __name__ == '__main__':
    unittest.main()
