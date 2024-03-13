import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def maxDepth(root: TreeNode):
    queue = collections.deque([root])
    depth = 0

    while queue:
        depth += 1
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return depth


class Test(unittest.TestCase):
    def test_treenode_init(self):
        input = [3, 9, 20, None, None, 15, 7]
        root = create_tree_node(input)
        print_tree(root)

    def test_example(self):
        root = create_tree_node([3, 9, 20, None, None, 15, 7])

        self.assertEqual(3, maxDepth(root))


if __name__ == '__main__':
    unittest.main()
