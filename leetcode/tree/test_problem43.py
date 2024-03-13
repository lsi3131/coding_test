import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

longest = 0


def diameter_of_binary_tree(root):
    if not root:
        return 0

    def dfs(node: TreeNode):
        global longest
        if not node:
            return 0

        left = dfs(node.left)
        right = dfs(node.right)

        longest = max(longest, left + right)
        return max(left, right) + 1

    dfs(root)
    global longest
    print(f'longest = {longest}')

    return longest


def diameter_of_binary_tree_v2(root):
    if not root:
        return 0

    def dfs(node: TreeNode, depth, max_depth):
        max_depth = max(depth, max_depth)
        print(f'cur node={node.val}, depth={depth}')
        if node.left:
            max_depth = max(max_depth, dfs(node.left, depth + 1, max_depth))
        if node.right:
            max_depth = max(max_depth, dfs(node.right, depth + 1, max_depth))

        return max_depth

    left_depth = right_depth = 0
    if root.left:
        left_depth = dfs(root.left, 1, 1)
    if root.right:
        right_depth = dfs(root.right, 1, 1)

    print(f'left = {left_depth}, right = {right_depth}')

    return left_depth + right_depth


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, diameter_of_binary_tree(create_tree_node([1, 2])))
        self.assertEqual(3, diameter_of_binary_tree(create_tree_node([1, 2, 3, 4, 5])))
        self.assertEqual(0, diameter_of_binary_tree(create_tree_node([])))
        self.assertEqual(4, diameter_of_binary_tree(create_tree_node([1, 2, None, 4, None, 8, None, 9])))
        data = [4, -7, -3, None, None, -9, -3, 9, -7, -4, None, 6, None, -6, -6, None, None, 0, 6, 5, None, 9, None,
                None, -1, -4, None, None, None, -2]
        self.assertEqual(8, diameter_of_binary_tree(create_tree_node(data)))



if __name__ == '__main__':
    unittest.main()
