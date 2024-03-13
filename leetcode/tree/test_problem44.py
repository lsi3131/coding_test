import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

# https://leetcode.com/problems/longest-univalue-path/description/

longest = 0


def longestUnivaluePath(root):
    def dfs(node: TreeNode):
        global longest
        length = 0
        if not node:
            return length, -1

        left_length, left_value = dfs(node.left)
        right_length, right_value = dfs(node.right)

        if node.val == left_value:
            length += left_length

        if node.val == right_value:
            length += right_length

        length += 1
        longest = max(length, longest)
        return length, node.val

    global longest
    dfs(root)
    return longest - 1


class Solution(object):
    longest = 0

    def longestUnivaluePath(self, root):
        if not root:
            return 0

        def dfs(node):
            if not node:
                return None, 0

            left_value, left_length, = dfs(node.left)
            right_value, right_length = dfs(node.right)

            if node.val != left_value:
                left_length = 0

            if node.val != right_value:
                right_length = 0

            self.longest = max(self.longest, left_length + right_length)
            return node.val, max(left_length, right_length) + 1

        dfs(root)
        return self.longest


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(0, Solution().longestUnivaluePath(create_tree_node([])))
        self.assertEqual(0, Solution().longestUnivaluePath(create_tree_node([5])))
        self.assertEqual(1, Solution().longestUnivaluePath(create_tree_node([5, 5])))
        self.assertEqual(0, Solution().longestUnivaluePath(create_tree_node([-1, 4, 4])))
        self.assertEqual(2, Solution().longestUnivaluePath(create_tree_node([5, 4, 5, 1, 1, None, 5])))
        self.assertEqual(2, Solution().longestUnivaluePath(create_tree_node([1, 4, 5, 4, 4, None, 5])))
        self.assertEqual(4, Solution().longestUnivaluePath(create_tree_node([1, None, 1, 1, 1, 1, 1, 1])))
        self.assertEqual(0, Solution().longestUnivaluePath(
            create_tree_node([-9, 5, 0, -2, -6, None, None, 5, None, None, -3, 6, -5, None, None, None, 0])))

    def test_compare(self):
        self.assertNotEquals(0, None)
        self.assertNotEquals(-1, None)
        self.assertFalse(0 == None)


if __name__ == '__main__':
    unittest.main()
