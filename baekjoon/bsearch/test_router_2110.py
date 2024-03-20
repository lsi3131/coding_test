'''
https://www.acmicpc.net/problem/2110

5 3
1
2
8
4
9
'''
import unittest
import sys


def solution(x_list, C):
    x_list.sort()
    left, right = 1, x_list[-1] - x_list[0]

    result = 0
    while left <= right:
        mid = (right + left) // 2
        i = 0
        count = 1
        while i < len(x_list):
            j = i + 1
            while j < len(x_list) and x_list[i] + mid > x_list[j]:
                j += 1

            if j >= len(x_list):
                break
            count += 1
            i = j
        if count >= C:
            # 개수가 많거나 같으면 거리를 늘린다.
            left = mid + 1
            result = mid
        else:
            # 개수가 적으면 거리를 줄인다
            right = mid - 1

    return result


N, C = map(int, input().split())
x_list = [int(sys.stdin.readline().strip('\n')) for _ in range(N)]
print(solution(x_list, C))

class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(3, solution([1, 2, 8, 4, 9], 3))
        self.assertEqual(8, solution([1, 2, 8, 4, 9], 2))
        pass


if __name__ == '__main__':
    unittest.main()
