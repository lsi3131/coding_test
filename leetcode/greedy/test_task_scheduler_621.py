'''
https://leetcode.com/problems/task-scheduler/description/
'''

import collections
from typing import List

import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *



class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        idle_duration_time = n
        total_task_time = 0
        while True:
            # idle 시간보다 1개 더 많은 task를 가져온다.
            # 만약 idle_time + 1보다 많은 값이 있으면 idle할 필요가 없다.
            # 만약 더 적게 가져온다면 더 이상 진행할 task가 없으므로 task를 idle_duration_time - task_time + 1 만큼 idle을 진행한다.
            tasks = counter.most_common(idle_duration_time + 1)
            task_time = 0
            for task, _ in tasks:
                task_time += 1  # idle time을 계산하기 위해서 사용.
                total_task_time += 1  # 실제 task가 진행된다.

                # counter에서 task에 해당하는 count를 하나 줄인다.
                # 이는 task가 진행된거로 볼 수 있다.
                counter.subtract(task)

                # counter의 task가 0 이하일 경우 제거한다.
                counter += Counter()

            if not counter:
                break

            # idle_time 계산
            idle_time = idle_duration_time - task_time + 1
            total_task_time += idle_time

        return total_task_time


class Test(unittest.TestCase):
    def test_example1(self):
        s = Solution()
        # A->B->idle->A->B->idle->A->B = 8
        self.assertEqual(8, Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2))

        # A->B->A->B->C->D = 6
        self.assertEqual(6, Solution().leastInterval(['A', 'C', 'A', 'B', 'D', 'B'], 1))

        # A->B->idle->idle->A->B->idle->idle->A->B = 10
        self.assertEqual(10, Solution().leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 3))

    def test_counter(self):
        cnt = Counter(['A', 'C', 'A', 'B', 'D', 'B'])
        print(cnt.most_common(1))
        print(cnt.most_common(2))
        print(cnt.most_common(3))

        self.assertEqual(2, cnt['A'])
        cnt.subtract('A')
        self.assertEqual(1, cnt['A'])
        cnt.subtract('A')
        self.assertEqual(0, cnt['A'])
        cnt.subtract('A')
        self.assertEqual(-1, cnt['A'])
        cnt += Counter()
        self.assertFalse('A' in cnt)

    def test_word(self):
        cnt = Counter(['a', 'b', 'c'])
        cnt.subtract('a')
        self.assertEqual(0, cnt['a'])

        cnt += Counter()

        cnt.subtract('a')
        cnt += Counter()
        self.assertEqual(0, cnt['a'])
        print(cnt)


if __name__ == '__main__':
    unittest.main()
