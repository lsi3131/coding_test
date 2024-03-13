import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


# https://leetcode.com/problems/invert-binary-tree/description/

class Solution:
    def invertTree(self, root):
        def invert(node):
            if not node:
                return

            node.left, node.right = node.right, node.left
            invert(node.left)
            invert(node.right)

        invert(root)
        return root


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([4, 7, 2, 9, 6, 3, 1], convert_tree_to_list_bfs(Solution().invertTree(create_tree_node([4, 2, 7, 1, 3, 6, 9]))))
        self.assertEqual([2, 3, 1], convert_tree_to_list_bfs(Solution().invertTree(create_tree_node([2, 1, 3]))))
        self.assertEqual([], convert_tree_to_list_bfs(Solution().invertTree(create_tree_node([]))))



if __name__ == '__main__':
    unittest.main()
