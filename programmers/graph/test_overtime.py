'''
https://school.programmers.co.kr/learn/courses/30/lessons/12927
'''
import unittest
import heapq


def solution(n, works):
    heap = []
    for w in works:
        heapq.heappush(heap, -w)

    while heap and n > 0:
        w = -heapq.heappop(heap)
        w -= 1
        if w > 0:
            heapq.heappush(heap, -w)
        n -= 1

    result = sum(list(map(lambda x: x ** 2, heap)))
    return result


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(12, solution(4, [4, 3, 3]))
        self.assertEqual(6, solution(1, [2, 1, 2]))
        self.assertEqual(0, solution(3, [1, 1]))


    def test_heap(self):
        d = [3,2,1]
        heapq.heapify(d)
        self.assertEqual(1, heapq.heappop(d))

if __name__ == '__main__':
    unittest.main()
