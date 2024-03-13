import collections
import heapq

import mycollections
import unittest
import random
import string
import re
from collections import *


def topKFrequent(nums: list, k):
    heap_freq = []
    freqs = Counter(nums)

    for key, value in freqs.items():
        heapq.heappush(heap_freq, (-value, key))

    topk = []
    k = min(k, len(heap_freq))
    for _ in range(k):
        topk.append(heapq.heappop(heap_freq)[1])

    return topk


def topKFrequent2(nums: list, k):
    return list(list(zip(*Counter(nums).most_common(k)))[0])


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual([1, 2], topKFrequent2([1, 1, 1, 2, 2, 3], 2))
        self.assertEqual([1], topKFrequent2([1], 1))
        self.assertEqual([1, 2], topKFrequent2([1, 2], 2))
        self.assertEqual([1, 2], topKFrequent2([1, 2], 3))

    def test_zip(self):
        l1 = [1, 2, 3, 4]
        l2 = [2, 3, 4]
        self.assertEqual([(1, 2), (2, 3), (3, 4)], list(zip(l1, l2)))

        counter = Counter([1, 1, 1, 2, 2, 3])
        print(Counter([1, 1, 1, 2, 2, 3]).most_common(2))
        self.assertEqual([((1, 2),), ((3, 4),)], list(zip([(1, 2), (3, 4)])))
        self.assertEqual([(1, 3), (2, 4)], list(zip(*[(1, 2), (3, 4)])))
        print(list(zip(counter.most_common(2))))
        print(list(zip(*counter.most_common(2))))
        print(list(zip(*counter.most_common(2)))[0])


if __name__ == '__main__':
    unittest.main()
