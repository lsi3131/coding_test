'''
https://school.programmers.co.kr/learn/courses/30/lessons/49191
'''

import unittest
from collections import defaultdict


# 예시 n = 5, results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
def solution(n, results):
    answer = 0

    wins = [[] for _ in range(n + 1)]  # 1번 인덱스에는 1이 이긴(1에게 진) 선수가 담김
    loses = [[] for _ in range(n + 1)]  # 1번 인덱스에서는 1이 진(1에게 이긴) 선수가 담김

    for winner, loser in results:
        wins[winner].append(loser)
        loses[loser].append(winner)
    # wins = [[], [2], [5], [2], [3, 2], []]
    # loses = [[], [], [4, 3, 1], [4], [], [2]]

    for i in range(1, n + 1):
        for w in wins[i]:
            # 1 > 2 > 5 (1이 2에게 이겼다면, 2에게 진 애들도 모두 1이 이긴다)
            for a in wins[w]:
                if a not in wins[i]:
                    # 순회 중간에 append를 진행하면 해당 데이터를 포함해서 순회를 한다.
                    wins[i].append(a)
            # 한 바퀴 돌면 [[], [2, 5], [5], [2], [3, 2], []]
        for l in loses[i]:
            for b in loses[l]:
                if b not in loses[i]:
                    loses[i].append(b)
            # 3이 4에게 졌다면, 4에게 이긴 애들도 모두 3을 이긴다 (3이 짐)
    print(wins)
    print(loses)
    # wins = [[], [2, 5], [5], [2, 5], [3, 2, 5], []]
    # loses = [[], [], [4, 3, 1], [4], [], [2, 4, 3, 1]]

    for i in range(1, n + 1):
        if len(wins[i]) + len(loses[i]) == n - 1:
            answer += 1

    return answer


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(2, solution(6, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [5, 6]]))
        # self.assertEqual(3, solution(5, [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5], [1, 3]]))
        # self.assertEqual(2, solution(1, [[4, 3]]))
        # self.assertEqual(2, solution(1, [[4, 3], [1, 2]]))

    def test_set(self):
        set1 = {4, 3, 2, 1}
        set2 = {3, 2, 5}
        print(set1 - set2)

    def test_append_list_in_loop(self):
        data = [1, 2, 3, 4, 5]
        count = 0
        for d in data:
            print(d)
            data.append(6)
            count += 1
            if count > 10:
                break


if __name__ == '__main__':
    unittest.main()
