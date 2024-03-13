import collections
from typing import Optional


class ListNode:
    def __init__(self, value=0, next=None):
        self.val = value
        self.next = next


class LinkedList:
    def __init__(self, head: ListNode = None):
        self.head = head

    def append(self, value):
        new_node = ListNode(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def append_list(self, values: list):
        for v in values:
            self.append(v)

    def display(self):
        current = self.head
        while current:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


def create_linkedlist(values: list):
    l1 = LinkedList()
    l1.append_list(values)
    return l1


def listnode_to_list(node: ListNode):
    results = []
    it = node
    while it:
        results.append(it.val)
        it = it.next
    return results


def create_linked_node(values: list):
    r = LinkedList()
    r.append_list(values)
    return r.head


class BiListNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def bilistnode_to_list(node: BiListNode):
    results = []
    it = node.right
    while it.right:
        results.append(it.val)
        it = it.right
    return results


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def create_tree_node(data: list) -> Optional[TreeNode]:
    if len(data) == 0:
        return None

    root = TreeNode(data[0])
    queue = [root]
    i = 1

    while i < len(data):
        current = queue.pop(0)
        if data[i] is not None:
            current.left = TreeNode(data[i])
            queue.append(current.left)
        i += 1
        if i < len(data) and data[i] is not None:
            current.right = TreeNode(data[i])
            queue.append(current.right)
        i += 1
    return root


def print_tree(node, indent=0):
    if node is None:
        return
    print(" " * indent + str(node.val))
    print_tree(node.left, indent + 2)
    print_tree(node.right, indent + 2)


def convert_tree_to_list_bfs(root):
    if not root:
        return []

    node = root
    result = [node.val]
    queue = collections.deque([node])
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

    return result

