import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


class Solution(object):
    def mergeTrees(self, t1, t2):
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTrees(t1.left, t2.left)
            node.right = self.mergeTrees(t1.right, t2.right)
            return node
        else:
            return t1 or t2

    def merge_tree_to_list(self, t1, t2):
        return convert_tree_to_list_bfs(self.mergeTrees(t1, t2))


class Test(unittest.TestCase):
    def test_solution(self):
        node1 = create_tree_node([1, 3, 2, 5])
        node2 = create_tree_node([2, 1, 3, None, 4, None, 7])
        self.assertEqual([3, 4, 5, 5, 4, None, 7], Solution().merge_tree_to_list(node1, node2))

    def test_solution2(self):
        node1 = create_tree_node([1])
        node2 = create_tree_node([1, 2])
        self.assertEqual([2, 2], Solution().merge_tree_to_list(node1, node2))

    def test_solution3(self):
        node1 = create_tree_node([1, 2, None, 3, None])
        node2 = create_tree_node([1, None, 2, None, 3])
        self.assertEqual([2, 2, 2, 3, None, None, 3], Solution().merge_tree_to_list(node1, node2))

    def test_example1(self):
        l1 = [1, None, 3, 5, 6, None, None, 1]
        l2 = [2, 3, 4]

        result = []

        # 음수가 존재할 수 있음
        while l1 or l2:
            l1_num = 0
            l2_num = 0
            if l1:
                l1_num = l1.pop(0)
            if l2:
                l2_num = l2.pop(0)

            if l1_num or l2_num:
                l1_num = 0 if l1_num is None else l1_num
                l2_num = 0 if l2_num is None else l2_num
                result.append(l1_num + l2_num)
            else:
                result.append(None)

        self.assertEqual([3, 3, 7, 5, 6, None, None, 1], result)

    def test_append(self):
        l1 = [1, 2, 3]
        l2 = [4, 5]
        self.assertEqual([1, 2, 3, 4, 5], l1 + l2)



if __name__ == '__main__':
    unittest.main()
