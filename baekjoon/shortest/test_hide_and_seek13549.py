'''
5 17

10 100000
'''
import unittest
import heapq


def solution(N, K):
    time = 0
    visited_time = {}
    remain = abs(K - N)
    heap = [(0, remain, N)]

    def add_to_heap(heap, time, remain, start):
        if start not in visited_time or visited_time[start] > time:
            heapq.heappush(heap, (time, remain, start))
            visited_time[start] = time

    while heap:
        time, remain, start = heapq.heappop(heap)

        if start == K:
            break

        if start > K:
            # walk back
            add_to_heap(heap, time + 1, remain - 1, start - 1)
        elif start < K:
            # teleport
            add_to_heap(heap, time, abs(K - (start * 2)), start * 2)

            # walk front
            add_to_heap(heap, time + 1, remain - 1, start + 1)

            # walk back
            if start > 0:
                add_to_heap(heap, time + 1, remain - 1, start - 1)

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
