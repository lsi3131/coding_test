import unittest
from mycollections import *


def solution(head):
    if head is None or head.next is None:
        return head

    odd = head
    even = head.next
    even_head = even

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next
        # odd.next, even.next = odd.next.next, even.next.next
        odd, even = odd.next, even.next

    odd.next = even_head

    return head


class Test(unittest.TestCase):
    def test_example1(self):
        l1 = LinkedList()
        l1.append_list([1,2,3,4,5])

        l2 = LinkedList()
        l2.append_list([2,1,3,5,6,4,7])

        l3 = LinkedList()
        l3.append_list([])

        self.assertEqual([1,3,5,2,4], listnode_to_list(solution(l1.head)))
        self.assertEqual([2,3,6,7,1,5,4], listnode_to_list(solution(l2.head)))
        self.assertEqual([], listnode_to_list(solution(l3.head)))


if __name__ == '__main__':
    unittest.main()
