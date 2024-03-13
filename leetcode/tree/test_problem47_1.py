import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *

# https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/

class Codec:

    def serialize(self, root):
        result = ['#']

        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                queue.append(node.left)
                queue.append(node.right)

                result.append(str(node.val))
            else:
                result.append('#')

        while result and result[-1] == '#':
            result.pop()

        return ' '.join(result)

    def deserialize(self, data):
        if len(data) == 0:
            return None

        data_list = data.split(' ')

        root = TreeNode(int(data_list[1]))
        queue = collections.deque([root])
        idx = 2
        while idx < len(data_list):
            node = queue.popleft()
            if data_list[idx] != '#':
                node.left = TreeNode(int(data_list[idx]))
                queue.append(node.left)
            idx += 1

            if idx < len(data_list) and data_list[idx] != '#':
                node.right = TreeNode(int(data_list[idx]))
                queue.append(node.right)
            idx += 1
        return root


class Test(unittest.TestCase):
    def assertTreeNode(self, actual: TreeNode, expect: TreeNode):
        self.assertEqual(convert_tree_to_list_bfs(actual), convert_tree_to_list_bfs(expect))

    def test_example1(self):
        self.assertEqual('',
                         Codec().serialize(create_tree_node([])))

        self.assertEqual('# 1',
                         Codec().serialize(create_tree_node([1])))

        self.assertEqual('# 1 2 3 # # 4 5',
                         Codec().serialize(create_tree_node([1, 2, 3, None, None, 4, 5])))

        self.assertTreeNode(create_tree_node([]),
                            Codec().deserialize(''))

        self.assertTreeNode(create_tree_node([1, 2, 3, None, None, 4, 5]),
                            Codec().deserialize('# 1 2 3 # # 4 5'))

        # self.assertEqual(to_str([3, 4, None, 5, None, 7]), Codec().serialize(create_tree_node([3, 4, None, 5, None, 7])))
        #
        # self.assertEqual(to_str([]),
        #                  Codec().serialize(create_tree_node([])))
        #
        # self.assertEqual(to_str(convert_tree_to_list_bfs(Codec().deserialize(to_str([1, 2, 3, None, None, 4, 5, ])))),
        #                  Codec().serialize(create_tree_node([1, 2, 3, None, None, 4, 5])))
        #
        # self.assertEqual(to_str(convert_tree_to_list_bfs(Codec().deserialize(to_str([3, 4, None, 5, None, 7])))),
        #                  Codec().serialize(create_tree_node([3, 4, None, 5, None, 7])))


if __name__ == '__main__':
    unittest.main()
