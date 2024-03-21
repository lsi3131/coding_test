import unittest
import collections


def solution(n, com):
    visited = []
    que = []

    cnt = 0
    for i in range(n):
        if not i in visited:
            que.append(i)
            cnt += 1

            while que:
                x = que.pop(0)
                for i in range(n):
                    if com[x][i] == 1 and i not in visited:
                        visited.append(i)
                        que.append(i)
    return cnt


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
        self.assertEqual(1, solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]))
        pass


if __name__ == '__main__':
    unittest.main()
