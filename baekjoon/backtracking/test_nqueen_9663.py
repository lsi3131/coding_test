import unittest


class Solution:
    def __init__(self, n):
        self.n = n
        self.ans = 0
        self.row = [0] * n

    def is_promising(self, x):
        for i in range(x):
            if self.row[x] == self.row[i] or abs(self.row[x] - self.row[i]) == abs(x - i):
                return False

        return True

    def n_queens(self, x):
        if x == self.n:
            self.ans += 1
            return

        else:
            for y in range(self.n):
                # [x, y]에 퀸을 놓겠다.
                self.row[x] = y
                if self.is_promising(x):
                    self.n_queens(x + 1)

        return self.ans


# --- submit ---
n = int(input())
print(Solution(n).n_queens(0))


class Test(unittest.TestCase):
    def test_example1(self):
        # self.assertEqual(0, solution(1))
        # self.assertEqual(0, solution(2))
        self.assertEqual(2, Solution(4).n_queens(0))
        # self.assertEqual(2, Solution.n_queens(4))
        # self.assertEqual(15, Solution(15).n_queens(0))
        # self.assertEqual(4, solution(6))
        self.assertEqual(40, Solution(7).n_queens(0))
        self.assertEqual(92, Solution(8).n_queens(0))
        # self.assertEqual(352, Solution(9).n_queens(0))
        # self.assertEqual(2, solution(6))
