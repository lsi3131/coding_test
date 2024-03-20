'''
https://leetcode.com/problems/implement-trie-prefix-tree/
'''

import unittest


class TrieNode:
    def __init__(self):
        self.word = False
        self.children = {}


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.word = True

    def search(self, word: str) -> bool:
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.word

    def startsWith(self, prefix: str) -> bool:
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


class Test(unittest.TestCase):
    def test_example1(self):
        trie = Trie()
        trie.insert("apple")
        self.assertTrue(trie.search("apple"))  # return True
        self.assertFalse(trie.search("app"))  # return False
        self.assertTrue(trie.startsWith("app"))  # return True
        trie.insert("app")
        self.assertTrue(trie.search("app"))  # return True


if __name__ == '__main__':
    unittest.main()
