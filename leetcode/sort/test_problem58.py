import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://leetcode.com/problems/sort-list/

class Solution:
    def mergeTwoLists(self, l1, l2):
        if l1 and l2:
            # 항상 l1은 작은 값을 가리킨다.
            if l1.val > l2.val:
                l1, l2 = l2, l1

            # l1.next는 l1.next, l2 중 더 작은 값을 가리키게 된다.
            l1.next = self.mergeTwoLists(l1.next, l2)

        # 더 작은 값인 l1을 반환하거나 l1이 None이면 l2를 반환한다.
        # 항상 더 작거나 not None인 값을 반환한다
        return l1 or l2

    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 나눠지는 동안은 head == None인 경우는 없으나 외부에서 head = None인 상태로 호출하는 경우를 막을 수 있다.
        if not (head and head.next):
            return head

        # runner를 사용하여 절반으로 나눈다.
        # head->...->half->None / slow->...->None 절반으로 나뉜다.
        fast = slow = head
        half = None
        while fast and fast.next:
            fast, slow, half = fast.next.next, slow.next, slow
        half.next = None

        l1 = self.sortList(head) # 좌측을 재귀 호출
        l2 = self.sortList(slow) # 우측을 재귀 호출

        # 정렬된 두 리스트를 병합하는 mergeTwoLists로 l1, l2를 병합해 나간다.
        return self.mergeTwoLists(l1, l2)



class Test(unittest.TestCase):
    def assertEqualNode(self, n1: ListNode, n2: ListNode):
        self.assertEqual(listnode_to_list(n1), listnode_to_list(n2))

    def test_example1(self):
        self.assertEqualNode(create_linked_node([1, 2, 3, 4]), Solution().sortList(create_linked_node([4, 2, 1, 3])))


if __name__ == '__main__':
    unittest.main()
