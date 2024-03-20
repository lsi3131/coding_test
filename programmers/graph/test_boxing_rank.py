'''
https://school.programmers.co.kr/learn/courses/30/lessons/49191
'''

import unittest
import collections


def solution(n, results):
    winners = collections.defaultdict(set)
    losers = collections.defaultdict(set)

    for winner, loser in results:
        winners[winner].add(loser)
        losers[loser].add(winner)

    def get_linked_set(graph, v):
        # 시작 위치를 제외한 연결된 노드부터 탐색하기 위해 queue 초기화
        queue = collections.deque()
        for w in graph[v]:
            queue.append(w)

        visited = set()
        while queue:
            nv = queue.popleft()
            visited.add(nv)
            for nw in graph[nv]:
                if nw not in visited:
                    queue.append(nw)

        return visited

    for i in range(1, n + 1):
        winners[i] = get_linked_set(winners, i)
        losers[i] = get_linked_set(losers, i)

    answer = 0
    for i in range(1, n + 1):
        if len(winners[i]) + len(losers[i]) == n - 1:
            answer += 1

    return answer


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]))
        # self.assertEqual(3, solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [1, 3]]))
        # self.assertEqual(2, solution(1, [[4, 3]]))
        # self.assertEqual(2, solution(1, [[4, 3], [1, 2]]))

    def test_set(self):
        set1 = {4, 3, 2, 1}
        set2 = {3, 2, 5}
        print(set1 - set2)


if __name__ == '__main__':
    unittest.main()
