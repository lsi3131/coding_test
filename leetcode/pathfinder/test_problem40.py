import collections
import heapq

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def networkDelayTime(times, n, k):
    graph = defaultdict(list)
    for u, v, w in times:
        graph[u].append((v, w))

    heap = []
    heapq.heappush(heap, (0, k))

    dist = defaultdict()
    while heap:
        time, node = heapq.heappop(heap)
        if node not in dist:
            dist[node] = time
            for v, w in graph[node]:
                new_time = time + w
                heapq.heappush(heap, (new_time, v))

    if len(dist) == n:
        return max(dist.values())

    return -1


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2))
        self.assertEqual(1, networkDelayTime([[1, 2, 1]], 2, 1))
        self.assertEqual(-1, networkDelayTime([[1, 2, 1]], 2, 2))
        self.assertEqual(-1, networkDelayTime([[1, 2, 1]], 2, 2))
        self.assertEqual(5, networkDelayTime([[3,1,5], [3,4,1], [3,2,2], [4,5,1], [5,6,1], [6,7,1], [7,8,1], [8,1,1], [2,1,2]],
                                             8, 3))


    def test_dict(self):
        pass

if __name__ == '__main__':
    unittest.main()
