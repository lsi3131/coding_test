import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


class Codec:

    def serialize(self, root):
        if not root:
            return ''

        node = root
        result = [node.val]
        queue = deque([node])
        while queue:
            node = queue.popleft()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

            if len(queue) > 0:
                result.append(None if node.left is None else node.left.val)
                result.append(None if node.right is None else node.right.val)

        while result and result[-1] is None:
            result.pop()

        result_str = ','.join(map(str, result))
        return result_str

    def deserialize(self, data):
        if len(data) == 0:
            return None

        str_data_list = data.split(',')
        int_data_list = [int(item) if item != 'None' else None for item in str_data_list]

        root = node = TreeNode(int_data_list[0])
        queue = deque([node])

        i = 1
        while i < len(int_data_list):
            current = queue.popleft()
            if int_data_list[i] is not None:
                current.left = TreeNode(int_data_list[i])
                queue.append(current.left)
            i += 1
            if i < len(int_data_list) and int_data_list[i] is not None:
                current.right = TreeNode(int_data_list[i])
                queue.append(current.right)
            i += 1

        return root


def to_str(int_d):
    str_d = map(str, int_d)
    return ','.join(str_d)


class Test(unittest.TestCase):
    def assertSerialAndDeserialize(self, actual_node, data):
        ser = Codec()
        deser = Codec()
        ans = deser.deserialize(ser.serialize(create_tree_node(data)))
        self.assertEqual(convert_tree_to_list_bfs(actual_node), convert_tree_to_list_bfs(ans))

    def test_example1(self):
        actual = to_str([1, 2, 3, None, None, 4, 5, ])
        expected = Codec().serialize(create_tree_node([1, 2, 3, None, None, 4, 5]))
        self.assertEqual(actual, expected)

        self.assertEqual(to_str([1, 2, 3, None, None, 4, 5, ]),
                         Codec().serialize(create_tree_node([1, 2, 3, None, None, 4, 5])))

        self.assertEqual(to_str([3, 4, None, 5, None, 7]),
                         Codec().serialize(create_tree_node([3, 4, None, 5, None, 7])))

        self.assertEqual(to_str([]),
                         Codec().serialize(create_tree_node([])))

        self.assertEqual(to_str(convert_tree_to_list_bfs(Codec().deserialize(to_str([1, 2, 3, None, None, 4, 5, ])))),
                         Codec().serialize(create_tree_node([1, 2, 3, None, None, 4, 5])))

        self.assertEqual(to_str(convert_tree_to_list_bfs(Codec().deserialize(to_str([3, 4, None, 5, None, 7])))),
                         Codec().serialize(create_tree_node([3, 4, None, 5, None, 7])))

    def test_serialize(self):
        int_d = [1, None, 2]
        str_d = map(str, int_d)
        self.assertEqual('1,None,2', ','.join(str_d))


if __name__ == '__main__':
    unittest.main()
