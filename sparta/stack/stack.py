import unittest


class Stack:
    class ListNode:
        def __init__(self, val):
            self.val = val
            self.prev = None
            self.next = None

    def __init__(self, max_size):
        self.last = Stack.ListNode(None)
        self.max_size = max_size
        self.cur_size = 0

    def is_empty(self) -> bool:
        return self.cur_size == 0

    def is_full(self) -> bool:
        return self.cur_size == self.max_size

    def push(self, val):
        if self.cur_size < self.max_size:
            new_node = Stack.ListNode(val)
            self.last.next = new_node
            new_node.prev = self.last
            self.last = self.last.next
            self.cur_size += 1

    def peek(self):
        return self.last.val

    def pop(self):
        if self.cur_size == 0:
            return None
        pop_val = self.last.val
        prev = self.last.prev
        self.last.prev = None
        prev.next = None
        self.last = prev
        self.cur_size -= 1
        return pop_val

s = Stack(3)
print(s.is_empty())
s.push(3)
print(s.is_empty())
print(s.peek())
s.push(2)
print(s.peek())
s.push(1)
print(s.peek())
s.push(4)
print(s.peek())
print(s.is_full())

print(s.pop())
print(s.is_full())

print(s.pop())
print(s.pop())
print(s.pop())
print(s.is_empty())

class Test(unittest.TestCase):
    def test_example1(self):
        s = Stack(3)
        self.assertEqual(True, s.is_empty())
        s.push(3)
        self.assertEqual(False, s.is_empty())
        self.assertEqual(3, s.peek())
        s.push(2)
        self.assertEqual(2, s.peek())
        s.push(1)
        self.assertEqual(1, s.peek())
        s.push(4)
        self.assertEqual(1, s.peek())
        self.assertEqual(True, s.is_full())

        self.assertEqual(1, s.pop())
        self.assertEqual(False, s.is_full())

        self.assertEqual(2, s.pop())
        self.assertEqual(3, s.pop())
        self.assertEqual(None, s.pop())
        self.assertEqual(True, s.is_empty())

        s.push(10)
        s.push(20)
        s.push(30)
        s.push(40)
        self.assertEqual(30, s.peek())
        self.assertEqual(30, s.pop())
        self.assertEqual(20, s.pop())
        self.assertEqual(10, s.pop())
