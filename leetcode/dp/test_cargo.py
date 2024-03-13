'''

'''

import collections
import mycollections
import unittest
import random
import string
import re
from collections import *
from mycollections import *


def zero_one_knapsack(cargo):
    capacity = 16
    pack = []

    # cargo = (가격, 무게)
    for i in range(len(cargo) + 1):
        pack.append([])
        for c in range(capacity + 1):
            cargo_price, cargo_cap = cargo[i - 1]
            if i == 0 or c == 0:
                pack[i].append(0)

            elif cargo_cap <= c:
                pack[i].append(
                    max(cargo_price + pack[i - 1][c - cargo_cap], pack[i - 1][c])
                )
            else:
                pack[i].append(cargo_price)

    return pack[-1][-1]


class Test(unittest.TestCase):
    def test_example1(self):
        cargo = [
            (4, 12),
            (2, 1),
            (10, 4),
            (1, 1),
            (2, 12),
        ]

        r = zero_one_knapsack(cargo)


if __name__ == '__main__':
    unittest.main()
