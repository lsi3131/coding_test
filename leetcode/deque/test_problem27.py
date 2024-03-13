import heapq

import unittest
from mycollections import *


def mergeKLists(lists: list[ListNode]):
    root = result = ListNode(None)

    heap = []
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(heap,(lists[i].val, i, lists[i]))

    while heap:
        node = heapq.heappop(heap)
        idx = node[1]
        result.next = node[2]

        result = result.next
        if result.next:
            heapq.heappush(heap, (result.next.val, idx, result.next))

    return root.next



class Test(unittest.TestCase):
    def test_example1(self):
        lists1 = [
            create_linked_node([1, 4, 5]),
            create_linked_node([1, 3, 4]),
            create_linked_node([2, 6])
        ]
        self.assertEqual([1, 1, 2, 3, 4, 4, 5, 6], listnode_to_list(mergeKLists(lists1)))

    def test_example2(self):
        lists1 = [
            create_linked_node([1, 4, 5]),
            None,
            create_linked_node([2, 6])
        ]
        self.assertEqual([1, 2, 4, 5, 6], listnode_to_list(mergeKLists(lists1)))



def test_headq2(self):
    heap = []
    n1 = ListNode(1)
    n2 = ListNode(1)
    heapq.heappush(heap, (n1.val, 1, n1))
    heapq.heappush(heap, (n2.val, 0, n2))

    results = []
    while heap:
        results.append(heapq.heappop(heap))

    self.assertEqual(n2, results[0][2])
    self.assertEqual(n1, results[1][2])


def test_headq(self):
    heap = []
    heapq.heappush(heap, (ListNode(4).val, 0, ListNode(4)))
    heapq.heappush(heap, (ListNode(3).val, 1, ListNode(3)))
    heapq.heappush(heap, (ListNode(2).val, 2, ListNode(2)))
    heapq.heappush(heap, (ListNode(5).val, 3, ListNode(5)))

    result = []
    while heap:
        node_tuple = heapq.heappop(heap)
        idx = node_tuple[1]
        val = node_tuple[2].val
        result.append((idx, val))

    self.assertEqual([(2, 2), (1, 3), (0, 4), (3, 5)], result)


def test_set(self):
    my_tuple = (1, 2, 3, 3)
    for s in my_tuple:
        print(s)


if __name__ == '__main__':
    unittest.main()
