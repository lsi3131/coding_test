'''
5 17

10 100000
'''
import unittest
import heapq


def solution(N, K):
    def visit(heap, time, x):
        if x not in visited_time or visited_time[x] > time:
            heapq.heappush(heap, (time, x))
            visited_time[x] = time

    time = 0
    visited_time = {}
    heap = [(0, N)]

    while heap:
        time, x = heapq.heappop(heap)

        if x == K:
            break

        if x > K:
            # walk back
            visit(heap, time + 1, x - 1)
        elif x < K:
            # teleport
            visit(heap, time, x * 2)

            # walk front
            visit(heap, time + 1, x + 1)

            # walk back
            if x > 0:
                visit(heap, time + 1, x - 1)

    return time


N, K = map(int, input().split())
print(solution(N, K))


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution(5, 17))
        self.assertEqual(6, solution(10, 100000))
        pass

# heapq.heappush(heap, (time, teleport_dist))
# heapq.heappush(heap, (time + 1, walk_dist + 1))
