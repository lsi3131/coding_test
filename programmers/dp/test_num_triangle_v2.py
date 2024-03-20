'''
https://school.programmers.co.kr/learn/courses/30/lessons/43105
'''

import unittest


def solution(tri):
    for i in range(1, len(tri)):
        for j in range(i + 1):
            if j == 0:
                tri[i][j] += tri[i - 1][0]
            elif j == i:
                tri[i][j] += tri[i - 1][i - 1]
            else:
                tri[i][j] += max(tri[i - 1][j - 1], tri[i - 1][j])

    return max(tri[-1])


# i = 1, j = 0~1
# 1,0 > 0,0 + 1,0
# 1,1 > 0,0 + 1,1

# i = 2, j = 0~2
# 2,0 > 1,0 + 2,0
# 2,1 > 1,0 + 2,1
# 2,1 > 1,1 + 2,1
# 2,2 > 1,1 + 2,2

# 양끝이 아니면 최대값 고민 항상함
# 결론 : 종이에 써보자


class Test(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(30, solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
