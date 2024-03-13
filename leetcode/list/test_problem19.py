import unittest
from mycollections import *


def reverseBetween(head, left, right):
    if head is None:
        return head

    if left >= right:
        return head

    prev_start = head
    for i in range(left - 1):
        prev_start = head
        head = head.next

    head_start = head
    head, prev = head.next, head
    # print('prev={}, head={}'.format(prev.val, head.val))

    for i in range(right - left):
        next = head.next
        head.next = prev
        head, prev = next, head
        # if head and prev and next:
        #     print('prev={}, head={}, next={}'.format(prev.val, head.val, next.val))

    prev_start.next = prev
    head_start.next = head

    if left == 1:
        root = prev
    else:
        root = prev_start

    return root


class Test(unittest.TestCase):
    def test_example1(self):
        # l1 = LinkedList()
        # l1.append_list([1, 2, 3, 4, 5])
        # self.assertEqual([1, 4, 3, 2, 5], listnode_to_list(reverseBetween(l1.head, 2, 4)))

        l2 = LinkedList()
        l2.append_list([1, 2, 3, 4, 5])
        self.assertEqual([5, 4, 3, 2, 1], listnode_to_list(reverseBetween(l2.head, 1, 5)))

        self.assertEqual([], listnode_to_list(reverseBetween(None, 1, 5)))

        l3 = LinkedList()
        l3.append_list([1, 2, 3, 4, 5])
        self.assertEqual([1, 2, 3, 4, 5], listnode_to_list(reverseBetween(l3.head, 3, 3)))

        l3 = LinkedList()
        l3.append_list([1, 2, 3])
        self.assertEqual([2, 1, 3], listnode_to_list(reverseBetween(l3.head, 1, 2)))

        l4 = LinkedList()
        l4.append_list([1, 2, 3])
        self.assertEqual([1, 3, 2], listnode_to_list(reverseBetween(l4.head, 2, 3)))

        l5 = LinkedList()
        l5.append_list([1, 2, 3, 4, 5])
        self.assertEqual([1, 2, 3, 4, 5], listnode_to_list(reverseBetween(l5.head, 3, 4)))

if __name__ == '__main__':
    unittest.main()
