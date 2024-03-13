import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def find_itinerary_recursive(tickets):
    # tickets -> graph 변환
    graph = defaultdict(list)
    for t_from, t_to in sorted(tickets, reverse=True):
        graph[t_from].append(t_to)

    print(sorted(tickets, reverse=True))

    results = []

    def dfs(v):
        while graph[v]:
            dfs(graph[v].pop())
        results.append(v)

    dfs('JFK')

    return results[::-1]


def find_itinerary_iter(tickets):
    graph = defaultdict(list)
    for t_from, t_to in sorted(tickets):
        graph[t_from].append(t_to)

    route = []

    stack = ['JFK']
    while stack:
        while graph[stack[-1]]:
            stack.append(graph[stack[-1]].pop(0))

        route.append(stack.pop())

    return route[::-1]


def check_isvalid_ticket(tickets, start):
    return True


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(['JFK', 'MUC', 'LHR', 'SFO', 'SJC'],
                         find_itinerary_recursive([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]))

        self.assertEqual(['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'],
                         find_itinerary_recursive(
                             [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]))

        self.assertEqual(['JFK', 'NRT', 'JFK', 'KUL'],
                         find_itinerary_recursive([['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']]))

        self.assertEqual(['JFK', 'MUC', 'LHR', 'SFO', 'SJC'],
                         find_itinerary_iter([['MUC', 'LHR'], ['JFK', 'MUC'], ['SFO', 'SJC'], ['LHR', 'SFO']]))

        self.assertEqual(['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO'],
                         find_itinerary_iter(
                             [['JFK', 'SFO'], ['JFK', 'ATL'], ['SFO', 'ATL'], ['ATL', 'JFK'], ['ATL', 'SFO']]))

        self.assertEqual(['JFK', 'NRT', 'JFK', 'KUL'],
                         find_itinerary_iter([['JFK', 'KUL'], ['JFK', 'NRT'], ['NRT', 'JFK']]))

    def test_check_is_valid_graph(self):
        self.assertTrue(check_isvalid_ticket([['a', 'b'], ['b', 'c']], 'a'))


if __name__ == '__main__':
    unittest.main()
