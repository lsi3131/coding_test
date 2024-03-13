import collections
import unittest
import random
import string
import re
from collections import *


class ListNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None


class MyHashMap(object):

    def __init__(self):
        self.size = 1000
        self.tables = defaultdict(ListNode)

    def put(self, key, value):
        index = key % self.size
        if self.tables[index].value is None:
            self.tables[index] = ListNode(key, value)
            return

        p = self.tables[index]
        while p:
            if p.key == key:
                p.value = value
                return
            elif p.next is None:
                break
            p = p.next
        p.next = ListNode(key, value)

    def get(self, key):
        index = key % self.size
        if self.tables[index].value is None:
            return -1

        p = self.tables[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1

    def remove(self, key):
        index = key % self.size
        if self.tables[index].value is None:
            return

        p = self.tables[index]
        if p.key == key:
            self.tables[index] = ListNode() if p.next is None else p.next
            return

        prev, p = p, p.next
        while p:
            if p.key == key:
                prev.next = p.next
                return
            prev, p = p, p.next


def solution(nums: list):
    return []


class Test(unittest.TestCase):
    def test_example1(self):
        myHashMap = MyHashMap()
        self.assertEqual(-1, myHashMap.get(1))  # return 1, The map is now [[1,1], [2,2]]
        myHashMap.put(1, 1)  # The map is now [[1,1]]
        myHashMap.put(1001, 2)  # The map is now [[1,1], [2,2]]
        self.assertEqual(1, myHashMap.get(1))  # return 1, The map is now [[1,1], [2,2]]
        self.assertEqual(2, myHashMap.get(1001))  # return 1, The map is now [[1,1], [2,2]]

        myHashMap.remove(1)  # remove the mapping for 2, The map is now [[1,1]]
        self.assertEqual(-1, myHashMap.get(1))  # return 1, The map is now [[1,1], [2,2]]
        # myHashMap.get(2)  # return -1 (i.e., not found), The map is now [[1,1]]
        


if __name__ == '__main__':
    unittest.main()
