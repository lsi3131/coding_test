import collections
import heapq
import time

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def check_time(func):
    def wrapper(*args, **kwargs):
        start = time.time() * 1000
        result = func(*args, **kwargs)
        end = time.time() * 1000
        expired_time_ms = end - start

        print(f"{func} - expired time = {expired_time_ms:.05f}ms, args={args}, kwargs={kwargs}")
        return result

    return wrapper


@check_time
def findCheapestPrice_v1(n, flights, src, dst, k):
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    Q = [(0, src, 0)]

    while Q:
        price, node, count = heapq.heappop(Q)
        if node == dst:
            return price

        if k >= count:
            for adj_node, adj_price in graph[node]:
                alt = price + adj_price
                heapq.heappush(Q, (alt, adj_node, count + 1))

    return -1


@check_time
def findCheapestPrice(n, flights, src, dst, k):
    graph = defaultdict(list)
    for u, v, w in flights:
        graph[u].append((v, w))

    Q = [(0, src, 0)]
    min_cost = {}

    # node, price, depth
    while Q:
        price, node, count = heapq.heappop(Q)
        if node == dst:
            return price

        if k >= count:
            for v, w in graph[node]:
                alt = price + w
                if (v, count + 1) not in min_cost or min_cost[(v, count + 1)] > alt:
                    min_cost[(v, count + 1)] = alt
                    heapq.heappush(Q, (alt, v, count + 1))

    return -1


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(700,
                         findCheapestPrice(4, [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]], 0, 3,
                                           1))
        self.assertEqual(200, findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 1))
        self.assertEqual(500, findCheapestPrice(3, [[0, 1, 100], [1, 2, 100], [0, 2, 500]], 0, 2, 0))
        self.assertEqual(7,
                         findCheapestPrice(5, [[0, 1, 5], [1, 2, 5], [0, 3, 2], [3, 1, 2], [1, 4, 1], [4, 2, 1]], 0, 2,
                                           2))

    def test_performance(self):
        self.assertEqual(-1, findCheapestPrice_v1(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 10))
        self.assertEqual(-1, findCheapestPrice_v1(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 20))
        self.assertEqual(-1, findCheapestPrice_v1(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 30))
        self.assertEqual(-1, findCheapestPrice_v1(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 40))
        self.assertEqual(-1, findCheapestPrice_v1(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 50))

        # self.assertEqual(-1, findCheapestPrice(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 10))
        # self.assertEqual(-1, findCheapestPrice(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 20))
        # self.assertEqual(-1, findCheapestPrice(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 30))
        # self.assertEqual(-1, findCheapestPrice(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 40))
        # self.assertEqual(-1, findCheapestPrice(3, [[1, 2, 1], [2, 1, 1], [1, 3, 1], [3, 1, 1]], 1, 4, 50))

        # self.assertEqual(-1,
        #                  findCheapestPrice(13,
        #                                    [[11, 12, 74], [1, 8, 91], [4, 6, 13], [7, 6, 39], [5, 12, 8], [0, 12, 54],
        #                                     [8, 4, 32], [0, 11, 4], [4, 0, 91], [11, 7, 64], [6, 3, 88], [8, 5, 80],
        #                                     [11, 10, 91], [10, 0, 60], [8, 7, 92], [12, 6, 78], [6, 2, 8], [4, 3, 54],
        #                                     [3, 11, 76], [3, 12, 23], [11, 6, 79], [6, 12, 36], [2, 11, 100],
        #                                     [2, 5, 49], [7, 0, 17], [5, 8, 95], [3, 9, 98], [8, 10, 61], [2, 12, 38],
        #                                     [5, 7, 58], [9, 4, 37], [8, 6, 79], [9, 0, 1], [2, 3, 12], [7, 10, 7],
        #                                     [12, 10, 52], [7, 2, 68], [12, 2, 100], [6, 9, 53], [7, 4, 90], [0, 5, 43],
        #                                     [11, 2, 52], [11, 8, 50], [12, 4, 38], [7, 9, 94], [2, 7, 38], [3, 7, 88],
        #                                     [9, 12, 20], [12, 0, 26], [10, 5, 38], [12, 8, 50], [0, 2, 77], [11, 0, 13],
        #                                     [9, 10, 76], [2, 6, 67], [5, 6, 34], [9, 7, 62], [5, 3, 67]], 10, 1,
        #                                    10))


if __name__ == '__main__':
    unittest.main()
