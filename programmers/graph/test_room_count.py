'''
https://school.programmers.co.kr/learn/courses/30/lessons/49190
'''

import collections
import unittest


def solution(arrows):
    graph = {(0, 0): []}  # 시작점 (0,0)
    move = {
        0: [0, 1],
        1: [1, 1],
        2: [1, 0],
        3: [1, -1],
        4: [0, -1],
        5: [-1, -1],
        6: [-1, 0],
        7: [-1, 1]
    }

    room = 0
    x, y = 0, 0

    # print((0, 0) in graph) -> True
    # print((1, 0) in graph) -> False

    for arr in arrows:
        for _ in range(1):
            nx, ny = x + move[arr][0], y + move[arr][1]
            if (nx, ny) in graph and (x, y) not in graph[(nx, ny)]:
                room += 1
                graph[(nx, ny)].append((x, y))
                graph[(x, y)].append((nx, ny))
            elif (nx, ny) not in graph:
                graph[(nx, ny)] = [(x, y)]
                graph[(x, y)].append((nx, ny))

            print(f'x={x}, y={y}, nx={nx}, ny={ny}')
            x, y = nx, ny

    # print(graph)

    return room


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(1, solution([2,4,6,2,6, 0]))
        # self.assertEqual(3, solution([6, 6, 6, 4, 4, 4, 2, 2, 2, 0, 0, 0, 1, 6, 5, 5, 3, 6, 0]))
        pass


if __name__ == '__main__':
    unittest.main()
