import unittest
import collections


def solution(n, computers):
    graph = collections.defaultdict(list)

    for i in range(len(computers)):
        for j in range(len(computers[i])):
            if i != j:
                if computers[i][j] == 1:
                    graph[i].append(j)

    def bfs(graph, v, visited: set):
        queue = collections.deque([v])
        while queue:
            v = queue.popleft()
            visited.add(v)
            for w in graph[v]:
                if w not in visited:
                    queue.append(w)

    visited = set()
    count = 0
    for i in range(n):
        if i not in visited:
            bfs(graph, i, visited)
            count += 1

    return count


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        self.assertEqual(1, solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
        pass


if __name__ == '__main__':
    unittest.main()
